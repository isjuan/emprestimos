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
    print("4 - Data dos empréstimos")
    print("0 - Retornar")

    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,0])
    return opcao

  def pega_dados_emprestimo(self):
    print("-------- INSIRA OS DADOS EMPRESTIMO ----------")
    numero_serie = input("Número de série: ")
    matricula = input("Matrícula do funcionário: ")
    codigo = input("Codigo do Empréstimo: ")

    return {"numero_serie": numero_serie, "matricula": matricula, "codigo": codigo}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_emprestimo(self, emprestimo):
    print("\n")
    print("Produto: ", emprestimo.produto) 
    print("Nome do funcionário: ", emprestimo.funcionario)
    print("Código de empréstimo: ", emprestimo.codigo)
    print("\n")
  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_emprestimo(self):
    codigo = input("Código do emprestimo que deseja selecionar: ")
    return codigo
