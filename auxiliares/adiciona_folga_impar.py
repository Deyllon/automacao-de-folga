from datetime import  timedelta
from traduzir_dia import *
import PySimpleGUI as sg
folga_impar = {}



def adiciona_folga_impar(dia):
    impar = ["rafael" , "neto", "henrique"]
    
    dia_somar = timedelta(days=1)
    
    while len(impar) !=0:
        nome_do_dia = traduzir_dia(dia)
        
        if dia.day % 2 != 0:
            while True:
                alguem_quer_folga = sg.popup_yes_no(f"Clique em yes se alguem quiser folgar no dia {dia} ou então clique em no se ninguem quiser: ", title="Escolher folga")
                
                if alguem_quer_folga == "Yes":
                    while True:
                       
                        quem_quer_folga = sg.popup_get_text("Digite o nome de quem quer folga: ", title="Quem vai folgar")
                        
                        if quem_quer_folga in impar:
                            if f"{nome_do_dia}-{dia.day}" not in folga_impar:
                                folga_impar.update({f"{nome_do_dia}-{dia.day}" : f"{quem_quer_folga}"})
                                impar.remove(quem_quer_folga)
                                break
                            
                            else:
                                sg.popup(f"já tem alguem de folga no dia {nome_do_dia}-{dia.day}", title="Erro, folga já adicionada")
                                break
                        
                        sg.popup(f"Porfavor verifique se você digitou o nome certo na lista {impar}", title="Erro, nome errado")
                    break         
                break
        dia+= dia_somar
        
    return folga_impar