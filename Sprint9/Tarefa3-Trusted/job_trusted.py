# segue abaixo o codigo usado no AWS Glue no job pra camada Trusted

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DoubleType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# definindo schema do json
schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("titulo", StringType(), nullable=False),
    StructField("data_de_lancamento", StringType(), nullable=False),
    StructField("popularidade", DoubleType(), nullable=False),
    StructField("nota_media", DoubleType(), nullable=False),
    StructField("orcamento", IntegerType(), nullable=False),
])

# lendo JSON com o schema definido
df_json = glueContext.read.json("s3://desafio-etl-isis/Raw/TMDB/JSON/2023/09/28/dados.json", schema=schema)
dynamic_df_json = DynamicFrame.fromDF(df_json, glueContext,"dynamic_df_json")

# tratando os dados e removendo filmes sem registro de nota
dyf_json_filtrado = Filter.apply(frame = dynamic_df_json, 
    f = lambda x: x["nota_media"] > 0)

# escrevendo o parquet na camada Trusted
escrever_parquet_json = glueContext.getSink(
    path="s3://desafio-etl-isis/Trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="gzip",
    enableUpdateCatalog=True,
    transformation_ctx="escrever_parquet_json",
)
escrever_parquet_json.setCatalogInfo(
    catalogDatabase="desafio-etl", catalogTableName="filmes"
)
escrever_parquet_json.setFormat("glueparquet")
escrever_parquet_json.writeFrame(dyf_json_filtrado)

job.commit()