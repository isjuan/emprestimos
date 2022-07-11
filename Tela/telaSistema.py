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
