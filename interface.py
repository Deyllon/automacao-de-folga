import imp
import PySimpleGUI as sg
sg.theme("DarkTeal12")
from main import *


class TelaPython:
    def __init__(self):
        l= [[sg.Text("Ano ", size=(10,0)), sg.Text("Mês ", size=(10,0), justification="right")],
            [ sg.Input(size=(20,0), key="ano"),sg.Input(size=(20,0), key="mes")],
            [sg.Button("Verificar Folgas", size=(25,0))]]
        layout = [[sg.Column(l, element_justification="center")]]
        
        self.janela= sg.Window("Adicionar Folgas",  layout=layout, margins=(0,0), resizable=True
                               ,return_keyboard_events=False)
        
      
        
    
     
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            ano = self.values["ano"]
            mes = self.values["mes"]
            resultado = verifica_ano(ano, mes)
            if resultado:
                print(folga(resultado))
                break
            
            
            
              
tela = TelaPython()
tela.Iniciar()

