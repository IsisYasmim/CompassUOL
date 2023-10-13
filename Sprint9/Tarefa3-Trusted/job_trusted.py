import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# lendo os arquivos JSON
df_filmes = glueContext.read.json("s3://desafio-etl-isis/Raw/TMDB/JSON/2023/10/09/filmes.json")
df_diretores = glueContext.read.json("s3://desafio-etl-isis/Raw/TMDB/JSON/2023/10/09/diretores.json")

# convertendo em DynamicFrame
dyf_filmes = DynamicFrame.fromDF(df_filmes, glueContext,"dyf_filmes")
dyf_diretores = DynamicFrame.fromDF(df_diretores, glueContext,"dyf_diretores")


# função para escrever os parquets na camada Trusted
def escrever_dynamicframe_no_s3(dyf, catalog_table_nome):
    sink = glueContext.getSink(
        path= "s3://desafio-etl-isis/Trusted/",
        connection_type="s3",
        updateBehavior="UPDATE_IN_DATABASE",
        partitionKeys=[],
        compression="gzip",
        enableUpdateCatalog=True,
        transformation_ctx="escrever_parquet_json"
    )
    sink.setCatalogInfo(catalogDatabase="desafio-etl", catalogTableName=catalog_table_nome)
    sink.setFormat("glueparquet")
    sink.writeFrame(dyf)

escrever_dynamicframe_no_s3(dyf_filmes, "filmes")
escrever_dynamicframe_no_s3(dyf_diretores, "diretores")

job.commit()