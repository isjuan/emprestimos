from Tela.telaAbstrata import TelaAbstrata

class TelaProduto(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador
  
  def tela_opcoes(self):
    print("-------- PRODUTOS ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar produto")
    print("2 - Alterar produto")
    print("3 - Excluir produto")
    print("4 - Produtos em estoque")
    print("5 - Produtos emprestados")
    print("6 - Incluir característica")
    print("7 - Alterar característica")
    print("8 - Excluir caracteristica")
    print("9 - Listar caracteristicas")
    print("10 - Marcar defeito")
    print("11 - Listar defeitos")
    print("12 - Consertar produto")
    print("0 - Retornar")
    
    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,5,6,7,8,9,10,11,12,0])
    return opcao

# nome_produto: str, marca: str, modelo: str, numero_serie: int
  def pega_dados_produto(self):
    print("-------- INSIRA OS DADOS DO PRODUTO ----------")
    nome_produto = input("Nome: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    numero_serie = int(input("Número de série:"))
    return {"nome_produto": nome_produto, "marca": marca, "modelo": modelo, "numero_serie": numero_serie}

  def mostra_produto(self, dados_produto):
    print("Nome do produto: ", dados_produto["nome_produto"])
    print("Marca do Produto: ", dados_produto["marca"])
    print("Modelo: ", dados_produto["modelo"])
    print("Número de série: ", dados_produto["numero_serie"])
    print("----------------------")

  def seleciona_caracteristica(self):
    codigo = input("Código da caracteristica a ser selecionada: ")
    return codigo

  def mostra_caracteristicas(self, caracteristica):
    print("Descrição: ", caracteristica.descricao)
    print("Valor: ", caracteristica.valor)
    print("Código: ", caracteristica.codigo)
    print("----------------------")

  def pega_dados_nova_caracteristica(self):
    print("-------- INSIRA OS DADOS DA CARACTERÍSTICA ----------")
    valor = str(input("Valor: "))
    descricao = input("Descrição: ")
    codigo = str(input("Codigo: "))
    if isinstance(valor, str) and isinstance(descricao, str) and isinstance(codigo, str):
      return {"valor": valor, "descricao": descricao, "codigo": codigo}
    else:
      self.mostra_mensagem("Entradas inválidas, por favor repita a operação!")
      return None

  def pega_caracteristica_no_produto(self):
    print("-------- INDIQUE A CARACTERÍSTICA DO PRODUTO ----------")
    codigo = input("Código da Característica: ")

    return {"codigo": codigo}

  def pega_codigo_defeito(self):
    print("-------- INDIQUE O CÓDIGO DO DEFEITO ----------")
    codigo = str(input("Código do defeito: "))

    return codigo

  def mostra_defeitos(self, defeito):
    print("Título: ", defeito.titulo)
    print("Descrição: ", defeito.descricao)
    print("Código: ", defeito.codigo)
    print("----------------------")

  def seleciona_produto(self):
    numero_serie = input("Número de série que deseja selecionar: ")
    return int(numero_serie)
