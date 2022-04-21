from datetime import date, datetime, timedelta
from calendar import monthrange, day_name
from dis import dis
import holidays
import PySimpleGUI as sg


feriados = holidays.Brazil()
folga_impar = {}
folga_par = {}
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
                sg.popup("você digitou um ano que já passou")
        else:
            sg.popup("Porfavor digiter um mês valido")
               
    else:
        sg.popup("Porfavor verifique se você digitou um ano ")
        
def traduzir_dia(dia):
    nome_do_dia = day_name[dia.weekday()]
    if nome_do_dia == "Monday":
        nome_do_dia = "Segunda-feira"
        return nome_do_dia
    elif nome_do_dia == "Tuesday":
        nome_do_dia = "Terça-feira"
        return nome_do_dia
    elif nome_do_dia == "Wednesday":
        nome_do_dia = "Quarta-feira"
        return nome_do_dia
    elif nome_do_dia == "Thursday":
        nome_do_dia = "Quinta-feira"
        return nome_do_dia
    elif nome_do_dia == "Friday":
        nome_do_dia = "Sexta-feira"
        return nome_do_dia
    elif nome_do_dia == "Saturday":
        nome_do_dia = "Sábado"
        return nome_do_dia
    nome_do_dia = "Domingo"
    return nome_do_dia

        
def adiciona_folga_impar(dia):
    impar = ["rafael" , "neto", "henrique"]
    
    dia_somar = timedelta(days=1)
    while len(impar) !=0:
        nome_do_dia = traduzir_dia(dia)
        if dia.day % 2 != 0:
            while True:
                alguem_quer_folga = sg.popup_yes_no(f"Clique em yes se alguem quiser folgar no dia {dia} ou então clique em no se ninguem quiser: ")
                if alguem_quer_folga == "Yes":
                    while True:
                        quem_quer_folga = sg.popup_get_text("Digite o nome de quem quer folga: ")
                        if quem_quer_folga in impar:
                            if f"{nome_do_dia}-{dia.day}" not in folga_impar:
                                folga_impar.update({f"{nome_do_dia}-{dia.day}" : f"{quem_quer_folga}"})
                                impar.remove(quem_quer_folga)
                                break
                            else:
                                sg.popup(f"já tem alguem de folga no dia {nome_do_dia}-{dia.day}")
                                break
                        sg.popup(f"Porfavor verifique se você digitou o nome certo na lista {impar}")
                    break         
                break
        dia+= dia_somar
        
    return folga_impar
        
def adiciona_folga_par(dia):
    par = ["Deyllon", "Bruno", "Vila"]
    
    dia_somar = timedelta(days=1)
    while len(par) !=0:
        nome_do_dia = traduzir_dia(dia)
        if dia.day % 2 == 0:
            while True:
                alguem_quer_folga = sg.popup_yes_no(f"Clique em yes se alguem quiser folgar no dia {dia} ou então clique em no se ninguem quiser: ")
                if alguem_quer_folga == "Yes":
                    while True:
                        quem_quer_folga = sg.popup_get_text("Digite o nome de quem quer folga: ")
                        if quem_quer_folga in par:
                            if f"{nome_do_dia}-{dia.day}" not in folga_par:
                                folga_par.update({f"{nome_do_dia}-{dia.day}" : f"{quem_quer_folga}"})
                                par.remove(quem_quer_folga)
                                break
                            else:
                                sg.popup(f"já tem alguem de folga no dia {nome_do_dia}-{dia.day}")
                                break
                        sg.popup(f"Porfavor verifique se você digitou o nome certo na lista {par}")
                    break    
                break
        dia+= dia_somar
        
    return folga_par
                 

def verifica_se_domingo_e_impar(dia, feriados):

    numero_do_dia = dia.day
    if (numero_do_dia % 2 != 0 and day_name[dia.weekday()] == "Sunday") or (numero_do_dia % 2 != 0 and dia in feriados ):
       return True
        
def verific_se_domingo_e_par(dia, feriado):
    numero_do_dia = dia.day
    if (numero_do_dia % 2 == 0 and day_name[dia.weekday()] == "Sunday") or (numero_do_dia % 2 == 0 and dia in feriados ):
        return True

def folga(resultado):
    
    dias = timedelta(days=1)
    
    inicio_do_mes = resultado[1]
    fim_do_mes = resultado[2]
    folga_para_impares=[]
    folga_para_pares=[]
    while inicio_do_mes <= fim_do_mes:
        if verifica_se_domingo_e_impar(inicio_do_mes, resultado[0]) == True:
            folga_para_impares.append(adiciona_folga_impar(inicio_do_mes))
        
        if verific_se_domingo_e_par(inicio_do_mes, resultado[0]) == True:
            folga_para_pares.append(adiciona_folga_par(inicio_do_mes))
      
        inicio_do_mes += dias
    return folga_para_impares[-1], folga_para_pares[-1]


def trata_retorno_folga(retorno):
    for chave, valor in  retorno[0].items():
        print(f"No dia: {chave} o funcionario: {valor} ira folgar")
    for chave, valor in retorno[1].items():
        print(f"No dia: {chave} o funcionario: {valor} ira folgar")
        

