import PySimpleGUI as sg
from auxiliares.verifica_ano import verifica_ano
from folga.folga import folga
from trata_retorno import *


sg.theme("LightBlue4")
class TelaPython:
    def __init__(self):
        layouts= [[sg.Text("Ano ", size=(10,0)), sg.Text("Mês ", size=(10,0), justification="right")],
            [ sg.Input(size=(20,0), key="ano"),sg.Input(size=(20,0), key="mes")],
            [sg.Button("Verificar Folgas", size=(25,0))],
            [sg.Output(size=(50,20), key="output")],
            [sg.Button('Fechar', size=(20,0))]]
        
        layout = [[sg.Column(layouts, element_justification="center")]]
        
        self.janela= sg.Window("Adicionar Folgas",  layout=layout, margins=(0,0), resizable=True
                               ,return_keyboard_events=False).Finalize()
           
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            
            if self.event == "Fechar":
                self.janela.close()
                break
            
            ano = self.values["ano"]
            mes = self.values["mes"]
            
            resultado = verifica_ano(ano, mes)
            
            if resultado:
                retorno = folga(resultado)
                trata_retorno_folga(retorno)
                                     
tela = TelaPython()
tela.Iniciar()

