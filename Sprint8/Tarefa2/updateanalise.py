import requests
import pandas as pd
import json
import boto3
import datetime
import io
import tempfile

# função para auxiliar no processamento em lotes
def processar_lote(df_pro_tmdb, headers):
  
  # lista para armazenar os dados gerados durante o loop
  filmes = []
  
  # loop para procurar todos os filmes presentes dentro do df no TMDB
  for indice, linha in df_pro_tmdb.iterrows():
          titulo = linha["movie_title"]
          url = (f"https://api.themoviedb.org/3/search/movie?query={titulo}"
              "&include_adult=false&language=en-US&page=1")
          response = requests.get(url, headers=headers)
          data = response.json()
          
          # loop para percorrer todos os resultados dentro do json
          for filme in data["results"]:
            # condição para retornar apenas os filmes com o titulo certo e que sejam do gênero terror
            if filme["title"] == titulo and 27 in filme["genre_ids"]:
                id = filme["id"] # pegando o id do filme para pesquisar mais detalhes no TMBD
                url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
                response2 = requests.get(url, headers=headers)
                detalhes = response2.json()
                # criando arquivo
                arqv_filme = {'titulo': filme["title"],
                        'diretores': linha["directors"],
                        'popularidade': filme['popularity'],
                        'media_voto': filme['vote_average'],
                        'data_lancamento': filme['release_date'],
                        'rendimento': detalhes['revenue']
                }
                # adicionando à lista
                filmes.append(arqv_filme)
                break

  return filmes


def processar_lote_pessoas(pessoa_lista, df_pro_tmdb, headers):
  # criando DataFrame para registrar os dados gerados na função
  pessoas_df = pd.DataFrame(columns=['nome', 'genero', 'popularidade'])
  
  
  # loop para procurar os atores do df no TMDB
  for pessoa in pessoa_lista:
    url = (f"https://api.themoviedb.org/3/search/person?query={pessoa}&"
          "include_adult=false&language=en-US&page=1")
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # percorrendo todos os resultados retornados
    for resultado in data["results"]:
          # condição que garante que o nome seja o mesmo
          if resultado["name"] == pessoa:
            # percorrendo todos os filmes daquele diretor
            for conhecido in resultado["known_for"]:
              # condição para que o diretor seja registrado apenas se houver os filmes certos na lista
              if conhecido.get('title') or conhecido.get('name') in df_pro_tmdb["movie_title"]:
                # condição para que os nomes não repitam
                if pessoas_df[pessoas_df["nome"] == resultado["name"]].empty:
                  arqv_pessoa = {'nome': resultado['name'],
                              'genero': resultado['gender'],
                              'popularidade': resultado['popularity']
                  }
                  pessoas_df = pd.concat([pessoas_df, pd.DataFrame([arqv_pessoa])], ignore_index=True)
                  break
  return pessoas_df


def lambda_handler(event, context):
    arquivo = 'Raw/Local/CSV/Movies/2023/10/07/rotten_tomatoes_movies.csv'
    bucket = 'desafio-etl-isis'

    # para ter acesso ao bucket
    s3 = boto3.client('s3')

    # baixando o arquivo CSV armazenado no bucket
    response = s3.get_object(Bucket=bucket, Key=arquivo)
    filmes_csv = io.BytesIO(response['Body'].read())

    # lê o arquivo movies.csv
    df = pd.read_csv(filmes_csv, low_memory=False)

    # substituindo os campos nulos
    df['directors'] = df['directors'].replace('NaN', float('nan'))
    df['genres'] = df['genres'].replace('NaN', float('nan'))
    
    # define a condição para filtrar apenas filmes de gênero Horror e linhas
    # não nulas
    cndc = (df['genres'].str.contains('Horror', case=False)
            & (~df['directors'].isna()))

    df_pro_tmdb = df[cndc][["movie_title", "genres", "directors"]]

    # para ter acesso à API
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9."
        "eyJhdWQiOiJiYmQ3Mjc1NWYzZDBjZTU4MzQ5YzVjZGUwNTZkMjgyMyIsInN1YiI6IjY0Z"
        "jcxNGQxZmZjOWRlMDEzOGVhMDdkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJza"
        "W9uIjoxfQ.tPdJmMREcDSuCKPiEw7GY8QQJ2mxRAPQYSjc-FLypcA"
    }

    
    # criando uma lista de diretores de acordo com os nomes em cada linha do dataframe
    diretores_lista = [diretor.strip() for diretor1 in df_pro_tmdb["directors"] for diretor in diretor1.split(',')]
    
    # definindo o tamanho do lote para processamento
    tamanho_lote = 1000
    
    # criando lista e DataFrame para armazenar os dados
    filmes = []
    diretores = pd.DataFrame(columns=['nome', 'genero', 'popularidade'])

    # fazendo processamento do arquivo CSV em lotes de 1000
    for i in range(0, len(df_pro_tmdb), tamanho_lote):
        # separando os dados
        lote_nomes = df_pro_tmdb[i:i + tamanho_lote]
        filmes_lote = processar_lote(lote_nomes, headers) # chamada da função
        filmes.extend(filmes_lote)
        # separando os dados
        lote_diretores = diretores_lista[i:i + tamanho_lote]
        diretores = pd.concat([diretores, processar_lote_pessoas(lote_diretores, df_pro_tmdb, headers)], ignore_index=True) # chamada da função e adição ao DataFrame

    # convertendo em json
    json_diretores = diretores.to_json(orient='records', lines=True)

    # criando um diretório temporário
    temp_dir = tempfile.mkdtemp()

    # definindo o caminho do arquivo JSON temporário
    temp_filme = f"{temp_dir}/filmes.json"
    temp_diretores = f"{temp_dir}/diretores.json"
   
   # salvando os dados em arquivos JSON
    with open(temp_filme, "w") as arquivo_json:
        json.dump(filmes, arquivo_json)

    with open(temp_diretores, 'w') as outfile:
        outfile.write(json_diretores)

    # registra a data atual e formata ela de acordo com o requisitado
    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d/')

    # criando as pastas no S3
    folder_movies = f'Raw/TMDB/JSON/{data_formatada}'
    s3.put_object(Bucket=bucket, Key=folder_movies)

    # especificando o caminho do arquivo
    s3_caminho_filmes = folder_movies + "filmes.json"
    s3_caminho_diretores = folder_movies + "diretores.json"

    # fazendo upload do arquivo para o bucket
    s3.upload_file(temp_filme, bucket, s3_caminho_filmes)
    s3.upload_file(temp_diretores, bucket, s3_caminho_diretores)
