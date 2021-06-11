import requests
import json


def requisicao(titulo):
    try:
        req = requests.get(
            'http://www.omdbapi.com/?apikey=943e3a95&t='+titulo+'&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Nao deu certo')
        return None


def printar_detalhes(filme):

    test_tuple = ['Titulo: '+filme['Title'],
                  'Genero: '+filme['Genre'],
                  'Ano: '+filme['Year'],
                  'Lançamento: '+filme['Released'],
                  'Pais: '+filme['Country'],
                  'Diretor: '+filme['Director'],
                  'Duração: '+filme['Runtime'],
                  'Atores: '+filme['Actors'],
                  'Nota: '+filme['imdbRating'],
                  'Premios: '+filme['Awards'],
                  filme['Poster']]

    return test_tuple
