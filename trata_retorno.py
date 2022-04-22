from auxiliares.cria_arquivo_excel import cria_arquivo_excel
import PySimpleGUI as sg
  

def trata_retorno_folga(retorno):
    for chave, valor in  retorno[0].items():
        print(f"No dia: {chave} o funcionario: {valor} ira folgar")
    for chave, valor in retorno[1].items():
        print(f"No dia: {chave} o funcionario: {valor} ira folgar")
    criar_arquivo = sg.popup_yes_no("Você deseja criar uma planilha excel?")
    if criar_arquivo == "Yes":
        cria_arquivo_excel(retorno)
