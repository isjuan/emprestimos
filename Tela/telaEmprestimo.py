from Tela.telaAbstrata import TelaAbstrata

class TelaEmprestimo(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador

  def tela_opcoes(self):
    print("-------- EMPRÉSTIMOS ----------")
    print("Escolha a opcao")
    print("1 - Emprestar produto")
    print("2 - Devolver produto")
    print("3 - Listar empréstimo")
    print("0 - Retornar")

    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,0])
    return opcao

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
    matricula = self.excecao_tipo_int("Matricula: ", int) # matricula = input("Matricula do funcionário: ")
    return matricula

  def seleciona_produto(self):
    numero_serie = input("Número de série que deseja selecionar: ")
    return int(numero_serie)
