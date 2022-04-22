from datetime import date, datetime, timedelta
from calendar import monthrange, day_name
import holidays
import PySimpleGUI as sg


feriados = holidays.Brazil()

def verifica_ano(ano, mes):  
    if len(ano) == 4 and ano.isnumeric(): 
        anoconvertido = int(ano)
        if mes.isnumeric() and 1<= int(mes)<=12:
            mesconvertido = int(mes)
            if datetime.today().year <= anoconvertido:
                feriado= feriados[f"{anoconvertido}-01-01": f"{anoconvertido}-12-31"]
                    
                inicio = date(anoconvertido, mesconvertido,1)
                dias = monthrange(anoconvertido, mesconvertido)[1]
                fim= date(anoconvertido, mesconvertido, dias)
                return feriado, inicio, fim
            else:
                sg.popup("você digitou um ano que já passou", title="Erro, ano já passou")
        else:
            sg.popup("Porfavor digiter um mês valido", title= "Erro, mês invalido")
               
    else:
        sg.popup("Porfavor verifique se você digitou um ano ")