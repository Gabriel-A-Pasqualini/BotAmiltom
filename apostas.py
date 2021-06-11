import discord
import psycopg2


from PIL import Image


banco = psycopg2.connect(
    user="postgres",
    password="123",
    host="127.0.0.1",
    port="5432",
    database="discord"
)


def Saldo(target):

    # print(target)

    comando_SQL = "SELECT dinheiro FROM user_discord WHERE id = '" + \
        str(target)+"'"

    cursor = banco.cursor()

    cursor.execute(comando_SQL)
    comando_SQL = cursor.fetchall()
    banco.commit()

    # print(str(comando_SQL))

    return comando_SQL[0]


def Bicho(bicho):

    if (bicho == '1') or (bicho == '01'):
        # avestruz = {'1', '2', '3', '4'}
        nome = 'avestruz'
        return nome  # , avestruz

    if (bicho == '2') or (bicho == '02'):
        #aguia = {'5', '6', '7', '8'}
        nome = 'aguia'
        return nome  # , aguia

    if (bicho == '3') or (bicho == '03'):
        # burro = {'9', '10', '11', '12'}
        nome = 'burro'
        return nome  # , burro

    if (bicho == '4') or (bicho == '04'):
        #borboleta = {'13', '14', '15', '16'}
        nome = 'borboleta'
        return nome  # , borboleta

    if (bicho == '5') or (bicho == '05'):
        #cachorro = {'17', '18', '19', '20'}
        nome = 'cachorro'
        return nome  # , cachorro

    if (bicho == '6') or (bicho == '06'):
        #cabra = {'21', '22', '23', '24'}
        nome = 'cabra'
        return nome  # , cabra

    if (bicho == '7') or (bicho == '07'):
        #carneiro = {'25', '26', '27', '28'}
        nome = 'carneiro'
        return nome  # , carneiro

    if (bicho == '8') or (bicho == '08'):
        #camelo = {'29', '30', '31', '32'}
        nome = 'camelo'
        return nome  # , camelo

    if (bicho == '9') or (bicho == '09'):
        #cobra = {'21', '22', '23', '24'}
        nome = 'cobra'
        return nome  # , cobra

    if bicho == '10':
        #coelho = {'37', '38', '39', '40'}
        nome = 'coelho'
        return nome  # , coelho

    if bicho == '11':
        #cavalo = {'41', '42', '43', '44'}
        nome = 'cavalo'
        return nome  # , cavalo

    if bicho == '12':
        #elefante = {'45', '46', '47', '48'}
        nome = 'elefante'
        return nome  # , elefante

    if bicho == '13':
        #galo = {'49', '50', '51', '52'}
        nome = 'galo'
        return nome  # , galo

    if bicho == '14':
        #gato = {'53', '54', '55', '56'}
        nome = 'gato'
        return nome  # , gato

    if bicho == '15':
        #jacare = {'57', '58', '59', '60'}
        nome = 'jacare'
        return nome  # , jacare

    if bicho == '16':
        #leao = {'61', '62', '63', '64'}
        nome = 'leao'
        return nome  # , leao

    if bicho == '17':
        #macaco = {'65', '66', '67', '68'}
        nome = 'macaco'
        return nome  # , macaco

    if bicho == '18':
        #porco = {'69', '70', '71', '72'}
        nome = 'porco'
        return nome  # , porco

    if bicho == '19':
        #pavao = {'73', '74', '75', '76'}
        nome = 'pavao'
        return nome  # , pavao

    if bicho == '20':
        #peru = {'77', '78', '79', '80'}
        nome = 'peru'
        return nome  # , peru

    if bicho == '21':
        #touro = {'81', '82', '83', '84'}
        nome = 'touro'
        return nome  # , touro

    if bicho == '22':
        #tigre = {'85', '86', '87', '88'}
        nome = 'tigre'
        return nome  # , tigre

    if bicho == '23':
        #urso = {'89', '90', '91', '92'}
        nome = 'urso'
        return nome  # , urso

    if bicho == '24':
        #veado = {'93', '94', '95', '96'}
        nome = 'veado'
        return nome  # , veado

    if bicho == '25':
        #vaca = {'97', '98', '99', '00'}
        nome = 'vaca'
        return nome  # , vaca

    else:
        return 0
