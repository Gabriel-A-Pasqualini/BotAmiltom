import time
import psycopg2
import datetime
from datetime import date
from federal import primeiro


banco = psycopg2.connect(
    user="postgres",
    password="123",
    host="127.0.0.1",
    port="5432",
    database="discord"
)

hora = list(time.localtime())

hour = int(hora[3])

dt = datetime.datetime.now()
str_dt = dt.strftime("%A")
print(hour)


def pagamento(target_id):
    if (str_dt == 'Wednesday') or (str_dt == 'Saturday'):

        if (hour >= 19):

            comando = "SELECT id_user, bicho, dinheiroapostado, data FROM aposta WHERE bicho =  '" + \
                primeiro+"'"  # primeiro é uma variavel da 'federal'

            cursor = banco.cursor()

            cursor.execute(comando)
            comando = cursor.fetchall()
            banco.commit()

            i = len(comando)

            print(i)
            print(type(i))

            soma = "SELECT SUM(dinheiroapostado) FROM aposta"

            cursor = banco.cursor()

            cursor.execute(soma)
            soma = cursor.fetchall()
            banco.commit()

            pote = str(soma)

            patedeatum = str(pote).strip("[()]")

            a = patedeatum.strip("Decimal(''),")

            valor_pote = float(a)
            print(type(valor_pote))
            print(valor_pote)
            
            
            cursor = banco.cursor()

            selct_din = "SELECT SUM(dinheiroapostado) FROM aposta WHERE id_user = (%s)"
            insert = str(target_id)
           
            
            cursor = banco.cursor()

            cursor.execute(selct_din, insert)

            banco.commit()

           
            return selct_din
            

            

        else:
            return 'não é hora'

    else:
        return 'não é dia'



