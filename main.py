from datetime import date, datetime, timedelta
from calendar import monthrange, day_name
from dis import dis
import holidays


feriados = holidays.Brazil()
folga_impar = {}
folga_par = {}
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
        
def adiciona_folga_impar(dia):
    impar = ["rafael" , "neto", "henrique"]
    
    dia_somar = timedelta(days=1)
    while len(impar) !=0:
        nome_do_dia = day_name[dia.weekday()]
        if dia.day % 2 != 0:
            while True:
                alguem_quer_folga = input(f"Digite 1 se alguem quiser folgar no dia {dia} ou então 2 se ninguem quiser: ")
                if alguem_quer_folga == "1":
                    while True:
                        quem_quer_folga = input("Digite o nome de quem quer folga : ")
                        if quem_quer_folga in impar:
                            if f"{nome_do_dia}-{dia.day}" not in folga_impar:
                                folga_impar.update({f"{nome_do_dia}-{dia.day}" : f"{quem_quer_folga}"})
                                impar.remove(quem_quer_folga)
                                break
                            else:
                                print(f"já tem alguem de folga no dia {nome_do_dia}-{dia.day}")
                                break
                        print(f"Porfavor verifique se você digitou o nome certo na lista {impar}")
                    break
                elif alguem_quer_folga == "2":
                    break
                
                print("Porfavor digite um digito valido")
        dia+= dia_somar
        
    return folga_impar
        
def adiciona_folga_par(dia):
    par = ["Deyllon", "Bruno", "Vila"]
    
    dia_somar = timedelta(days=1)
    while len(par) !=0:
        nome_do_dia = day_name[dia.weekday()]
        if dia.day % 2 == 0:
            while True:
                alguem_quer_folga = input(f"Digite 1 se alguem quiser folgar no dia {dia} ou então 2 se ninguem quiser: ")
                if alguem_quer_folga == "1":
                    while True:
                        quem_quer_folga = input("Digite o nome de quem quer folga : ")
                        if quem_quer_folga in par:
                            if f"{nome_do_dia}-{dia.day}" not in folga_par:
                                folga_par.update({f"{nome_do_dia}-{dia.day}" : f"{quem_quer_folga}"})
                                par.remove(quem_quer_folga)
                                break
                            else:
                                print(f"já tem alguem de folga no dia {nome_do_dia}-{dia.day}")
                                break
                        print(f"Porfavor verifique se você digitou o nome certo na lista {par}")
                    break
                elif alguem_quer_folga == "2":
                    break
                
                print("Porfavor digite um digito valido")
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

def ip():
    
    dias = timedelta(days=1)
    resultado = verifica_ano()
    inicio_do_mes = resultado[1]
    fim_do_mes = resultado[2]
    a=[]
    b=[]
    while inicio_do_mes <= fim_do_mes:
        if verifica_se_domingo_e_impar(inicio_do_mes, resultado[0]) == True:
            a.append(adiciona_folga_impar(inicio_do_mes))

        if verific_se_domingo_e_par(inicio_do_mes, resultado[0]) == True:
            b.append(adiciona_folga_par(inicio_do_mes))
            
        inicio_do_mes += dias
    return a, b
print(ip())