from tkinter import SINGLE
import PySimpleGUI as sg
from Tela.telaAbstrata import TelaAbstrata

class TelaDefeito(TelaAbstrata):
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
    layout = [[sg.Button('Novo defeito', key='1', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Listar defeitos', key='2', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Alterar título', key='3', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Alterar descrição', key='4', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Excluir defeito', key='5', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Retornar', key='0', size=(20, 2), button_color='#500000', font=('Helvetica', 11))],
              ]
    self.__window = sg.Window('DEFEITOS').Layout(layout)

  def pega_dados_defeito(self): #Mudar para adepas descrição/nome e código
    layout = [[sg.Text('Título:', size=(10, 1)), sg.InputText('', key='titulo')],
              [sg.Text('Descrição:', size=(10, 1)), sg.InputText('', key='descricao')],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Submit('Cadastrar', button_color='#008000')]
              ]
    self.__window = sg.Window('NOVO DEFEITO').Layout(layout)

    while True:
      botao, valor = self.open()
      titulo = str(valor['titulo'])
      descricao = str(valor['descricao'])
      codigo = str(valor['codigo'])

      if (titulo != '') and (descricao != '') and (codigo != '') and isinstance(codigo, str):
        self.close()
        return {"titulo": titulo, "descricao": descricao, "codigo": codigo}

  def pega_dados_titulo(self):
    layout = [[sg.Text('Selecione o defeito e insira o novo título', font=("Helvica", 9))],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Text('Título:', size=(10, 1)), sg.InputText('', key='titulo')],
              [sg.Submit('Aplicar', button_color='#008000')]
              ]
    self.__window = sg.Window('Alterar Título').Layout(layout)

    while True:
      botao, valor = self.open()
      titulo = str(valor['titulo'])
      codigo = str(valor['codigo'])

      if (titulo != '') and (codigo != '') and isinstance(codigo, str):
        self.close()
        return {"titulo": titulo, "codigo": codigo}

  def pega_dados_descricao(self):
    layout = [[sg.Text('Selecione o defeito e insira a nova descrição', font=("Helvica", 9))],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Text('Descrição:', size=(10, 1)), sg.InputText('', key='descricao')],
              [sg.Submit('Aplicar', button_color='#008000')]
              ]
    self.__window = sg.Window('Alterar Descrição').Layout(layout)

    while True:
      botao, valor = self.open()
      descricao = str(valor['descricao'])
      codigo = str(valor['codigo'])

      if (descricao != '') and (codigo != '') and isinstance(codigo, str):
        self.close()
        return {"descricao": descricao, "codigo": codigo}

  def seleciona_defeito(self):
    layout = [[sg.Text('Qual defeito deseja selecionar?', font=("Helvica", 9))],
              [sg.Text('Código:', size=(8, 1)), sg.InputText('', key='codigo')],
              [sg.Submit('Selecionar', button_color='#008000')]
              ]
    self.__window = sg.Window('Seleciona Defeito').Layout(layout)

    botao, valor = self.open()
    codigo = str(valor['codigo'])
    self.close()

    return codigo

  def lista_defeitos(self, controlador):
    dados = 'Código - Descrição do defeito: \n\n'
    for defeito in controlador.defeitos:
      dados += (str(defeito.codigo) + ' - ' + str(defeito.descricao) + '\n')
    sg.Popup('Lista de Defeitos', dados)

  def pega_dados_codigo(self):
    print("-------- NOVO CÓDIGO ----------")
    codigo = input("Novo Código: ")
    return codigo
