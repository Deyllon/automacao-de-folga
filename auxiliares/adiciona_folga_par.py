from datetime import  timedelta
from traduzir_dia import *
import PySimpleGUI as sg


folga_par = {}

def adiciona_folga_par(dia):
    par = ["Deyllon", "Bruno", "Vila"]
    
    dia_somar = timedelta(days=1)
    
    while len(par) !=0:
        nome_do_dia = traduzir_dia(dia)
        
        if dia.day % 2 == 0:
            while True:
                alguem_quer_folga = sg.popup_yes_no(f"Clique em Yes se alguem quiser folgar no dia {dia} ou então clique em NO se ninguem quiser: ", title="Escolher folga")
                
                if alguem_quer_folga == "Yes":
                    while True:
                        quem_quer_folga = sg.popup_get_text("Digite o nome de quem quer folga: ", title="Quem vai folgar")
                        
                        if quem_quer_folga in par:
                            if f"{nome_do_dia}-{dia.day}" not in folga_par:
                                folga_par.update({f"{nome_do_dia}-{dia.day}" : f"{quem_quer_folga}"})
                                par.remove(quem_quer_folga)
                                break
                            
                            else:
                                sg.popup(f"já tem alguem de folga no dia {nome_do_dia}-{dia.day}", title="Erro, folga já adicionada")
                                break
                        
                        sg.popup(f"Porfavor verifique se você digitou o nome certo na lista {par}", title="Erro, nome errado")
                    break    
                break
        dia+= dia_somar
    return folga_par