from tkinter import SINGLE
import PySimpleGUI as sg
from Tela.telaAbstrata import TelaAbstrata

class TelaDefeito(TelaAbstrata):
#  def __init__(self, controlador):
#    super().__init__()
#    self.__controlador = controlador
#
#  def tela_opcoes(self):
#    print("-------- DEFEITO ----------")
#    print("Escolha a opcao")
#    print("1 - Novo defeito")
#    print("2 - Listar defeitos")
#    print("3 - Alterar titulo")
#    print("4 - Alterar descrição")
#    print("5 - Excluir defeito")
#    print("0 - Retornar")
#
#    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,5,0])
#    return opcao
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
              [sg.Text('Descriço:', size=(10, 1)), sg.InputText('', key='descricao')],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Cadastrar', button_color='#008000')]
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
              [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Aplicar', button_color='#008000')]
              ]
    self.__window = sg.Window('Alterar Título').Layout(layout)

    while True:
      botao, valor = self.open()
      titulo = str(valor['titulo'])
      codigo = str(valor['codigo'])

      if (titulo != '') and (codigo != '') and isinstance(codigo, str):
        self.close()
        return {"titulo": titulo, "codigo": codigo}
#    print("-------- NOVO TÍTULO ----------")
#    titulo = input("Titulo: ")
#    return titulo

  def pega_dados_descricao(self):
    layout = [[sg.Text('Selecione o defeito e insira a nova descrição', font=("Helvica", 9))],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Text('Descrição:', size=(10, 1)), sg.InputText('', key='descricao')],
              [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Aplicar', button_color='#008000')]
              ]
    self.__window = sg.Window('Alterar Descrição').Layout(layout)

    while True:
      botao, valor = self.open()
      descricao = str(valor['descricao'])
      codigo = str(valor['codigo'])

      if (descricao != '') and (codigo != '') and isinstance(codigo, str):
        self.close()
        return {"descricao": descricao, "codigo": codigo}
#    print("-------- NOVA DESCRIÇÃO ----------")
#    descricao = input("Descricao: ")
#    return descricao

  def seleciona_defeito(self):
    layout = [[sg.Text('Qual defeito deseja selecionar?', font=("Helvica", 9))],
              [sg.Text('Código:', size=(8, 1)), sg.InputText('', key='codigo')],
              [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Selecionar', button_color='#008000')]
              ]
    self.__window = sg.Window('Seleciona Defeito').Layout(layout)

    botao, valor = self.open()
    codigo = str(valor['codigo'])
    self.close()

    return codigo
#    codigo = input("Código do Defeito: ")
#    return codigo

  def lista_defeitos(self, controlador):
    dados = 'Código - Descrição do defeito: \n\n'
    for defeito in controlador.defeitos:
      dados += (str(defeito.codigo) + ' - ' + str(defeito.descricao) + '\n')
    sg.Popup('Lista de Defeitos', dados)
#    defeitos = []
#    for defeito in controlador.defeitos:
#      texto = ("Código: " + str(defeito.codigo))
#      defeitos.append(defeito.codigo)
#    layout = [[sg.Listbox(values=defeitos, select_mode=SINGLE, size=(20, len(defeitos)), key='1b_itens')],
#              [sg.Ok('<< Retornar <<', button_color='#500000'), sg.Open('Selecionar', button_color='#008000')]
#              ]
#    self.__window = sg.Window('Lista de Defeitos').Layout(layout)
#
#    while True:
#      botao, valor = self.open()
#      if botao == sg.Ok:
#        self.close()
#      elif botao == sg.Open:
#        self.mostra_defeito(dados_defeito={"titulo": defeito.titulo, "descricao": defeito.descricao, "codigo": defeito.codigo})

#  def mostra_defeito(self, dados_defeito):
#    dados = ''
#    for dado in dados_defeito:
#      dados += ("TÍTUTLO: " + str(dados_defeito['titulo']) + '\n')
#      dados += ("DESCRIÇÃO: " + str(dados_defeito["descricao"]) + '\n')
#      dados += ("CÓDIGO: " + str(dados_defeito["codigo"]) + '\n\n')
#    sg.Popup('Dados do Defeito', dados)
#    print("\n")
#    print("-------DEFEITOS CADASTRADOS-----")
#    print("TITULO: ", dados_defeito["titulo"])
#    print("DESCRIÇÃO: ", dados_defeito["descricao"])
#    print("CÓDIGO: ", dados_defeito["codigo"])
#    print("\n")

#  def pega_dados_defeito(self):
#    print("-------- NOVO DEFEITO ----------")
#    titulo = input("Titulo: ")
#    descricao = input("Descricao: ")
#    codigo = input("Codigo: ")
#    return {"titulo": titulo, "descricao": descricao, "codigo": codigo}
#Funções antigas não utilizadas:
  def pega_dados_codigo(self):
    print("-------- NOVO CÓDIGO ----------")
    codigo = input("Novo Código: ")
    return codigo
