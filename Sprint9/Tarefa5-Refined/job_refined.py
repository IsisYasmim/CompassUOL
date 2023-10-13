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

# lendo os parquets na camada trusted
df_filmes = glueContext.read.parquet("s3://desafio-etl-isis/Trusted/run-1696893832141-part-block-0-r-00000-snappy.parquet")
df_diretores = glueContext.read.parquet("s3://desafio-etl-isis/Trusted/run-1696893837222-part-block-0-r-00000-snappy.parquet")
df_diretores = df_diretores.dropDuplicates()

# registrando os DataFrames como tabelas temporárias para usar SQL
df_filmes.createOrReplaceTempView("filmes")
df_diretores.createOrReplaceTempView("diretores")

# consulta SQL para criar o DataFrame df_fatorendimento
consulta_sql = """
  SELECT
      f.titulo,
      f.media_voto,
      YEAR(f.data_lancamento) AS ano_lancamento,
      f.rendimento,
      f.popularidade,
      CASE
        WHEN SUM(CASE WHEN d.genero = 1 THEN 1 ELSE 0 END) > 0 THEN 'Feminino'
        WHEN SUM(CASE WHEN d.genero = 2 THEN 1 ELSE 0 END) > 0 THEN 'Masculino'
        ELSE 'Nenhum'
      END AS genero_diretor
  FROM filmes f
  LEFT JOIN diretores d ON ARRAY_CONTAINS(SPLIT(f.diretores, ','), d.nome)
  WHERE f.rendimento > 0
  GROUP BY f.titulo, f.media_voto, YEAR(f.data_lancamento), f.rendimento, f.popularidade
  HAVING genero_diretor IN ('Feminino', 'Masculino')
"""
# executando a consulta SQL e criando o DataFrame df_fatorendimento
df_fatorendimento = spark.sql(consulta_sql)

# criando apenas uma repartição
df_filmes = df_filmes.repartition(1)
df_diretores = df_diretores.repartition(1)
df_fatorendimento = df_fatorendimento.repartition(1)

# convertendo DataFrame para DynamicFrame
dyf_filmes = DynamicFrame.fromDF(df_filmes, glueContext, 'dyf_filmes')
dyf_diretores = DynamicFrame.fromDF(df_diretores, glueContext, 'dyf_diretores')
dyf_fatorendimento = DynamicFrame.fromDF(df_fatorendimento, glueContext, 'dyf_fatorendimento')

# escrevendo o parquet na camada Refined
def escrever_dynamicframe_no_s3(dyf, catalog_table_nome, caminho):
    sink = glueContext.getSink(
        path= caminho,
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

# chamada da função
escrever_dynamicframe_no_s3(dyf_filmes, "dim_filmes", "s3://desafio-etl-isis/Refined/dim_filmes")
escrever_dynamicframe_no_s3(dyf_diretores, "dim_diretores", "s3://desafio-etl-isis/Refined/dim_diretores")
escrever_dynamicframe_no_s3(dyf_fatorendimento, "fato_rendimento", "s3://desafio-etl-isis/Refined/fato_rendimento")


job.commit()