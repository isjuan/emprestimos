import PySimpleGUI as sg
from Tela.telaAbstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()


    def tela_opcoes(self):
        self.init_components()
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        self.close()
        return int(botao)

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        layout = [[sg.Button('Funcionário', key='1', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Produto', key='2', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Empréstimo', key='3', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Defeito', key='4', size=(20, 2), font=('Helvetica', 11))],
                  [sg.Button('Finalizar sistema', key='0', size=(22, 1), button_color='#500000')],
                  ]
        self.__window = sg.Window('HOME').Layout(layout)


''' 
from Tela.telaAbstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador

  def tela_opcoes(self):
    print("-------- HOME ---------")
    print("")
    print("Escolha sua opcao:")
    print("1 - Funcionário")      
    print("2 - Produto")
    print("3 - Empréstimo")
    print("4 - Defeito")
    print("0 - Finalizar")
    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,0])
    print("------------------------")
    
    return opcao
'''
