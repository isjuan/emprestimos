import PySimpleGUI as sg
from Tela.telaAbstrata import TelaAbstrata

class TelaCaracteristica(TelaAbstrata):
  def __init__(self, controlador):
    self.__window = None
    self.init_components()
    super().__init__()
    self.__controlador = controlador

  def tela_opcoes(self):
    self.init_components()
    botao, valores = self.__window.Read()
    if botao is None:
      botao = 0
    self.close()
    return int(botao)

  def open(self):
    botao, valor = self.__window.Read()
    return botao, valor

  def close(self):
    self.__window.Close()

  def init_components(self):
    #sg.theme_previewer()
    layout = [[sg.Button('Alterar Valor', key='1', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Alterar Descrição', key='2', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Alterar Código', key='3', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Retornar', key='0', size=(20, 2), button_color='#500000', font=('Helvetica', 11))],
              ]
    self.__window = sg.Window('CARACTERÍSTICA').Layout(layout)

#  def tela_opcoes(self):
#    print("-------- CARACTERÍSTICAS ----------")
#    print("Escolha a opcao")
#    print("1 - Alterar Valor")
#    print("2 - Alterar Descrição")
#    print("3 - Alterar Código")
#    print("0 - Retornar")
#
#    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,0])
#    return opcao

  def pega_dados_valor(self):
    print("-------- NOVO VALOR ----------")
    valor = input("Novo Valor: ")
    return valor

  def pega_dados_descricao(self):
    print("-------- NOVA DESCRIÇÃO ----------")
    descricao = input("Nova Descrição: ")
    return descricao

  def pega_dados_codigo(self):
    print("-------- NOVO CÓDIGO ----------")
    codigo = input("Novo Código: ")
    return codigo

  def seleciona_caracteristica(self):
    codigo = input("Código da característica: ")
    return str(codigo)

  def seleciona_produto(self):
    numero_serie = input("Número de série que deseja selecionar: ")
    return int(numero_serie)
