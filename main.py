from datetime import date, datetime, timedelta
from calendar import monthrange, day_name
from dis import dis
import holidays


feriados = holidays.Brazil()

def verifica_ano():
    a=[]
    while len(a) == 0:
        ano = input("Digite o ano: ")
        mes = input("Digite o mês: ")
        if len(ano) == 4 and ano.isnumeric(): 
            anoconvertido = int(ano)
            if mes.isnumeric() and 1<= int(mes)<=12:
                mesconvertido = int(mes)
                if datetime.today().year <= anoconvertido:
                    a= feriados[f"{anoconvertido}-01-01": f"{anoconvertido}-12-31"]
                    
                    inicio = date(anoconvertido, mesconvertido,1)
                    dias = monthrange(anoconvertido, mesconvertido)[1]
                    fim= date(anoconvertido, mesconvertido, dias)
                    return a, inicio, fim
                else:
                    print("você digitou um ano que já passou")
            else:
                print("Porfavor digiter um mês valido")
               
        else:
            print("Porfavor verifique se você digitou um ano ")
        
        
impar = ["Rafael" , "Neto", "Henrique"]
par = ["Deyllon", "Bruno", "Vila"]

def verifica_se_domingo_e_impar(dia, feriados):
    numero_do_dia = dia.day
    if (numero_do_dia % 2 != 0 and day_name[dia.weekday()] == "Sunday") or (numero_do_dia % 2 != 0 and dia in feriados ):
        print(dia)

def verific_se_domingo_e_par(dia, feriado):
    numero_do_dia = dia.day
    if (numero_do_dia % 2 == 0 and day_name[dia.weekday()] == "Sunday") or (numero_do_dia % 2 == 0 and dia in feriados ):
        print(dia)

def ip():
    dias = timedelta(days=1)
    resultado = verifica_ano()
    inicio_do_mes = resultado[1]
    fim_do_mes = resultado[2]
    while inicio_do_mes <= fim_do_mes:
        verifica_se_domingo_e_impar(inicio_do_mes, resultado[0])
        verific_se_domingo_e_par(inicio_do_mes, resultado[0])
        inicio_do_mes += dias

ip()