import requests
import pandas as pd
import json
import boto3
import datetime
import io
import tempfile


# função para auxiliar no processamento em lotes
def processar_lote(ids, headers):

    filmes = []

    # procura todos os ids presentes na lista no TMDB
    for movieid in ids:
        url = (
            f"https://api.themoviedb.org/3/find/{movieid}"
            "?external_source=imdb_id"
        )
        response = requests.get(url, headers=headers)
        data = response.json()

        # só entra na condição os filmes que não retornarem vazios
        if data['movie_results']:
            id_tmdb = data['movie_results'][0]['id']

        # procura detalhes mais específicos do filme usando outro link da API
            url = ("https://api.themoviedb.org/3/movie/"
                   f"{id_tmdb}?language=en-US")
            response = requests.get(url, headers=headers)
            data = response.json()

            # filtra os filmes com budget abaixo de 500000 e maior que 0
            if 0 < data['budget'] < 500000:
                arqv = {'Titulo': data['title'],
                        'Data de Lancamento': data['release_date'],
                        'Popularidade': data['popularity'],
                        'Nota Media': data['vote_average'],
                        'Orcamento': data['budget']
                        }
                filmes.append(arqv)

    return filmes


def lambda_handler(event, context):
    arquivo = 'Raw/Local/CSV/Movies/2023/09/04/movies.csv'
    bucket = 'desafio-etl-isis'

    # para ter acesso ao bucket
    s3 = boto3.client('s3')

    # baixando o arquivo CSV
    response = s3.get_object(Bucket=bucket, Key=arquivo)
    movies_csv = io.BytesIO(response['Body'].read())

    # lê o arquivo movies.csv
    df = pd.read_csv(movies_csv, sep='|', low_memory=False)
    df['notaMedia'] = df['notaMedia'].replace('\\N', float('nan'))

    # define a condição para filtrar apenas filmes de gênero Horror
    condicao = (df['genero'].str.contains('Horror', case=False)
                & (~df['notaMedia'].isna())
                & (df['notaMedia'].astype(float) > 8))

    ids = sorted(set(df.loc[condicao, 'id'].tolist()))

    # para ter acesso à API
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9."
        "eyJhdWQiOiJiYmQ3Mjc1NWYzZDBjZTU4MzQ5YzVjZGUwNTZkMjgyMyIsInN1YiI6IjY0Z"
        "jcxNGQxZmZjOWRlMDEzOGVhMDdkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJza"
        "W9uIjoxfQ.tPdJmMREcDSuCKPiEw7GY8QQJ2mxRAPQYSjc-FLypcA"
    }

    # fazendo processamento do arquivo CSV em lotes de 1000
    tamanho_lote = 1000
    filmes = []

    for i in range(0, len(ids), tamanho_lote):
        lote_ids = ids[i:i + tamanho_lote]
        filmes_lote = processar_lote(lote_ids, headers)
        filmes.extend(filmes_lote)

    # criando um diretório temporário
    temp_dir = tempfile.mkdtemp()

    # definindo o caminho do arquivo JSON temporário
    temp_caminho = f"{temp_dir}/dados.json"

    # salvando os dados no arquivo JSON
    with open(temp_caminho, "w") as arquivo_json:
        json.dump(filmes, arquivo_json)

    # registra a data atual e formata ela de acordo com o requisitado
    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d/')

    # criando as pastas no S3
    folder_movies = f'Raw/TMDB/JSON/{data_formatada}'
    s3.put_object(Bucket=bucket, Key=folder_movies)

    # especificando o caminho do arquivo
    s3_caminho_arquivo = folder_movies + "dados.json"

    # fazendo upload do arquivo para o bucket
    s3.upload_file(temp_caminho, bucket, s3_caminho_arquivo)
