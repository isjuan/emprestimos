from Tela.telaAbstrata import TelaAbstrata

class TelaFuncionario(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador

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
  
  def pega_dados_funcionario(self):
    print("-------- DADOS FUNCIONARIO ----------")
    nome = input("Nome: ")
    matricula = self.excecao_tipo_int("Matricula: ", int) #input("Matricula: ")
    return {"nome": nome, "matricula": matricula}

  def mostra_funcionario(self, dados_funcionario):
    print("NOME DO FUNCIONARIO: ", dados_funcionario["nome"])
    print("MATRICULA DO FUNCIONARIO: ", dados_funcionario["matricula"])
    print("------------------------------")

  def seleciona_funcionario(self):
    matricula = self.excecao_tipo_int("Matricula: ", int) # matricula = input("Matricula do funcionário: ")
    return matricula
