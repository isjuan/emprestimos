import PySimpleGUI as sg
from Tela.telaAbstrata import TelaAbstrata

class TelaEmprestimo(TelaAbstrata):
#  def __init__(self, controlador):
#    super().__init__()
#    self.__controlador = controlador
#
#  def tela_opcoes(self):
#    print("-------- EMPRÉSTIMOS ----------")
#    print("Escolha a opcao")
#    print("1 - Emprestar produto")
#    print("2 - Devolver produto")
#    print("3 - Listar empréstimo")
#    print("0 - Retornar")
#
#    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,0])
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

  def close(self):
    self.__window.Close()

  def init_components(self):
    #sg.theme_previewer()
    layout = [[sg.Button('Emprestar Produto', key='1', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Devolver Produto', key='2', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Listar Empréstimos', key='3', size=(20, 2), font=('Helvetica', 11))],
              [sg.Button('Retornar', key='0', size=(20, 2), button_color='#500000', font=('Helvetica', 11))],
              ]
    self.__window = sg.Window('EMPRÉSTIMO').Layout(layout)

  def pega_codigo_emprestimo(self):
    print("-------- INSIRA O CÓDIGO DO EMPRÉSTIMO ----------")
    codigo = input("Codigo do Empréstimo: ")
    return codigo

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_emprestimo(self, emprestimo):
    print("\n")
    print("Produto: ", emprestimo.produto.nome_produto) 
    print("Nome do funcionário: ", emprestimo.funcionario.nome)
    print("Código de empréstimo: ", emprestimo.codigo)
    print("\n")
  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_emprestimo(self):
    codigo = input("Código do emprestimo que deseja selecionar: ")
    return codigo

  def seleciona_funcionario(self):
    #matricula = self.excecao_tipo_int("Matricula: ", int)
    matricula = input("Matricula do funcionário: ")
    return int(matricula)

  def seleciona_produto(self):
    numero_serie = input("Número de série que deseja selecionar: ")
    return int(numero_serie)
