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
              [sg.Button('Retornar', key='0', size=(20, 2), button_color='#500000', font=('Helvetica', 11))],
              ]
    self.__window = sg.Window('CARACTERÍSTICA').Layout(layout)

  def pega_dados_valor(self):
    layout = [[sg.Text('Selecione a característica e insira o novo valor', font=("Helvica", 9))],
              [sg.Text('Nº Série:', size=(10, 1)), sg.InputText('', key='numero_serie')],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Text('Valor:', size=(10, 1)), sg.InputText('', key='valor')],
              [sg.Submit('Aplicar', button_color='#008000')]
              ]
    self.__window = sg.Window('Alterar Descrição').Layout(layout)

    while True:
      botao, valores = self.open()
      numero_serie = self.excecao_tipo_int(valores['numero_serie'], int)
      valor = valores['valor']
      codigo = str(valores['codigo'])

      if ((numero_serie != '') and isinstance(numero_serie, int)) and (valor != '') and ((codigo != '') and isinstance(codigo, str)):
        self.close()
        return {"numero_serie": numero_serie, "valor": valor, "codigo": codigo}

  def pega_dados_descricao(self):
    layout = [[sg.Text('Selecione a característica e insira a nova descrição', font=("Helvica", 9))],
              [sg.Text('Nº Série:', size=(10, 1)), sg.InputText('', key='numero_serie')],
              [sg.Text('Codigo:', size=(10, 1)), sg.InputText('', key='codigo')],
              [sg.Text('Descrição:', size=(10, 1)), sg.InputText('', key='descricao')],
              [sg.Submit('Aplicar', button_color='#008000')]
              ]
    self.__window = sg.Window('Alterar Descrição').Layout(layout)

    while True:
      botao, valores = self.open()
      numero_serie = self.excecao_tipo_int(valores['numero_serie'], int)
      descricao = str(valores['descricao'])
      codigo = str(valores['codigo'])

      if ((numero_serie != '') and isinstance(numero_serie, int)) and (descricao != '') and ((codigo != '') and isinstance(codigo, str)):
        self.close()
        return {"numero_serie": numero_serie, "descricao": descricao, "codigo": codigo}

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
