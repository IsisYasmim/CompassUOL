import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, expr, substring, floor
from pyspark.sql.types import IntegerType
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dyf_filmes = glueContext.create_dynamic_frame.from_options(
    connection_type = "s3", 
    connection_options = {"paths": ["s3://desafio-etl-isis/Trusted/"]}, 
    format = "parquet"
)

# registrando apenas o ano do lançamento dos filmes
df_ano = dyf_filmes.toDF().withColumn("ano", substring(col("data_de_lancamento"), 1, 4)).selectExpr("ano").withColumn("ano",col("ano").cast(IntegerType()))
df_ano = df_ano.repartition(1)

# registrando apenas a nota media dos filmes
dyf_notamedia = dyf_filmes.drop_fields(['data_de_lancamento','titulo','popularidade','orcamento','id'])
df_notamedia = dyf_notamedia.toDF().repartition(1)

# registrando os orçamentos medios e notas medias de agrupados por ano
df_media_por_ano = dyf_filmes.toDF() \
        .groupBy(expr("substring(data_de_lancamento, 1, 4)").alias('ano')) \
        .agg(expr('avg(nota_media)').alias('nota_media'), 
             expr('avg(orcamento)').alias('orcamento_medio')) \
        .selectExpr('ano', 'nota_media', 'orcamento_medio') \
        .withColumn("ano",col("ano").cast(IntegerType()))
df_media_por_ano = df_media_por_ano.repartition(1)

# convertendo DataFrame para DynamicFrame
dyf_media_por_ano = DynamicFrame.fromDF(df_media_por_ano, glueContext, 'dyf_media_por_ano')
dyf_ano = DynamicFrame.fromDF(df_ano, glueContext, 'dyf_ano')
dyf_notamedia = DynamicFrame.fromDF(df_notamedia, glueContext, 'dyf_notamedia')

# escrevendo o parquet de dyf_ano na camada Refined
glueContext.write_dynamic_frame.from_options(
        frame = dyf_ano,
        connection_type = "s3",    
        connection_options = {"path": "s3://desafio-etl-isis/Refined/"},
        format = "glueparquet")


# escrevendo o parquet de dyf_notamedia na camada Refined
glueContext.write_dynamic_frame.from_options(
        frame = dyf_notamedia,
        connection_type = "s3",    
        connection_options = {"path": "s3://desafio-etl-isis/Refined/"},
        format = "glueparquet")

# escrevendo o parquet de dyf_media_por_ano na camada Refined
glueContext.write_dynamic_frame.from_options(
        frame = dyf_media_por_ano,
        connection_type = "s3",    
        connection_options = {"path": "s3://desafio-etl-isis/Refined/"},
        format = "glueparquet")


job.commit()