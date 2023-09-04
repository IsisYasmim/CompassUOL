import boto3
import datetime

# registra a data atual e formata ela de acordo com o requisitado
data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime('%Y/%m/%d/')

# definindo o nome do bucket S3 e o caminho das pastas a serem criadas no S3
bucket_nome = 'desafio-etl-isis'
folder_movies = f'Raw/Local/CSV/Movies/{data_formatada}'
folder_series = f'Raw/Local/CSV/Series/{data_formatada}'

# cria uma sessão do S3
s3 = boto3.client('s3')

# lista de arquivos CSV
arquivos = ['movies.csv', 'series.csv']

# faz o upload dos arquivos para o S3 e cria as pastas
for arquivo in arquivos:
    if arquivo == 'movies.csv':
        # criando as pastas
        s3.put_object(Bucket=bucket_nome, Key=folder_movies)
        # especificando o caminho da object key
        s3_object_key = folder_movies + arquivo
    elif arquivo == 'series.csv':
        s3.put_object(Bucket=bucket_nome, Key=folder_series)
        s3_object_key = folder_series + arquivo
    # fazen o upload do arquivo para o bucket
    try:
        s3.upload_file(arquivo, bucket_nome, s3_object_key)
        print(f"Arquivo '{arquivo}' enviado com sucesso para "
              f"'{bucket_nome}/{s3_object_key}'")
    except Exception as e:
        print(f"Erro ao enviar o arquivo '{arquivo}' para o S3: {e}")
