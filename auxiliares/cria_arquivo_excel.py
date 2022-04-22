import PySimpleGUI as sg
import xlsxwriter 


def cria_arquivo_excel(retorno):
    
    nome_arquivo = sg.popup_get_text("Digite o nome do arquivo a ser criado", title="Titulo do arquivo", )
    
    arquivo = xlsxwriter.Workbook(f"{nome_arquivo}.xlsx")
    
    tabela = arquivo.add_worksheet("Folga")
    
    nome_colunas = ["Dia", "Numero do dia", "Funcionario"]
    
    linha = 0
    coluna = 0
    
    tabela.write(linha, coluna, nome_colunas[0])
    tabela.write(linha, coluna+1, nome_colunas[1])
    tabela.write(linha, coluna+2, nome_colunas[2])
    
    linha+=1
    
    for chave, valor in retorno[0].items():
        chave = chave.split("-")
        tabela.write(linha,coluna,chave[0])
        tabela.write(linha,coluna+1,chave[1])
        tabela.write(linha,coluna+2,valor)
        linha+=1
    
    for chave, valor in retorno[1].items():
        chave = chave.split("-")
        tabela.write(linha,coluna,chave[0])
        tabela.write(linha,coluna+1,chave[1])
        tabela.write(linha,coluna+2,valor)
        linha+=1
    
    arquivo.close()