from Tela.telaAbstrata import TelaAbstrata

class TelaCaracteristica(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador

  def tela_opcoes(self):
    print("-------- CARACTERÍSTICAS ----------")
    print("Escolha a opcao")
    print("1 - Alterar Valor")
    print("2 - Alterar Descrição")
    print("3 - Alterar Código")
    print("0 - Retornar")

    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,0])
    return opcao

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
