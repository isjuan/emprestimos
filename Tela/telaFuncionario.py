from Tela.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaFuncionario(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador
    self.__window = None
    self.init_components()

  def init_components(self):
    layout = [#[sg.Listbox(values=('funcionario 2', 'funcionario3'), size=(30, 3))],
              [sg.Button('Cadastrar funcionário', key='1', size=(15, 2), button_color='#008015'),
               sg.Button('Excluir funcinário', key='4', size=(15, 2), button_color='#d5001d')],
              [sg.Button('Editar funcionário', key='3', size=(32, 2))],
              [sg.Button('Listar funcionários', key='2', size=(32, 2))],
              [sg.Button('<< Retornar <<', key='0', size=(15, 1), button_color='#500000')]
              ]
    self.__window = sg.Window('Funcionarios').Layout(layout)

  def tela_opcoes(self):
    self.init_components()
    botao, valores = self.__window.Read()
    if botao is None:
      botao = 0
    self.close()
    return int(botao)

  def close(self):
    self.__window.close()

  '''
  def tela_opcoes(self):
    print("-------- TELA FUNCIONARIOS ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Editar Funcionário")
    print("4 - Excluir funcionario")
    print("0 - Retornar")
    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,0])
    print("-------------------------------------")
    return opcao
  '''
  def pega_dados_funcionario(self):
    layout = [[sg.Text('Nome:', size=(8, 1)), sg.InputText('', key='nome')],
              [sg.Text('Matrícula:', size=(8, 1)), sg.InputText('', key='matricula')],
              [sg.Cancel('<< Retornar <<', button_color='#500000'), sg.Submit('Cadastrar', button_color='#008000')]
              ]
    self.__window = sg.Window('Cadastrar funcionario').Layout(layout)

    while True:
      botao, valor = self.open()
      nome = valor['nome']
      matricula = self.excecao_tipo_int(valor['matricula'], int)

      if nome != '' and isinstance(matricula, int):
        self.close()
        return {"nome": nome, "matricula": matricula}
      # matricula = valor['matricula']

  def seleciona_funcionario(self):
    matricula = input('Matricula: ')
    matricula = self.excecao_tipo_int("Matricula: ", int) # matricula = input("Matricula do funcionário: ")
    return matricula

  def old_pega_dados_funcionario(self):
    print("-------- DADOS FUNCIONARIO ----------")
    nome = input("Nome: ")
    matricula = self.excecao_tipo_int("Matricula: ", int) #input("Matricula: ")
    return {"nome": nome, "matricula": matricula}

  def mostra_funcionario(self, dados_funcionario):
    print("NOME DO FUNCIONARIO: ", dados_funcionario["nome"])
    print("MATRICULA DO FUNCIONARIO: ", dados_funcionario["matricula"])
    print("------------------------------")

  def seleciona_funcionario_old(self):
    matricula = input('Matricula: ')
    matricula = self.excecao_tipo_int("Matricula: ", int) # matricula = input("Matricula do funcionário: ")
    return matricula

  def open(self):
    botao, valor = self.__window.Read()
    return botao, valor