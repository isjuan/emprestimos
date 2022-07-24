from Tela.telaProduto import TelaProduto
from Entidade.produto import Produto
from Entidade.caracteristica import Caracteristica

class ControladorProduto:
  def __init__(self, controlador_sistema):
    self.__produtos = []
    self.__produtos_emprestados = []
    self.__produtos_estocados = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_produto = TelaProduto(self)

  @property #função usada pelo sistema
  def produtos(self):
    return self.__produtos

  @property #função usada pelo sistema
  def produtos_emprestados(self):
    return self.__produtos_emprestados

  @property #função usada pelo sistema
  def produtos_estocados(self):
    return self.__produtos_estocados

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_produto, 2: self.alterar_produto, 3: self.excluir_produto, 4: self.listar_produtos_estocados, 5: self.listar_produtos_emprestados, 6: self.incluir_caracteristica, 7: self.alterar_caracteristicas, 8: self.excluir_caracteristca, 9: self.listar_caracteristicas, 10: self.marcar_defeito, 11: self.listar_defeitos, 12: self.consertar_produto, 0: self.retornar}
    
    continua = True
    while continua:

      lista_opcoes[self.__tela_produto.tela_opcoes()]()
  
  def pega_produto_numero_serie(self, numero_serie: int):
    for produto in self.__produtos:
      if(produto.numero_serie == numero_serie):
        return produto
    return None

  def incluir_produto(self):
    dados_produto = self.__tela_produto.pega_dados_produto()
    try:
      for produto in self.produtos:
        if produto.numero_serie == dados_produto["numero_serie"]:
          raise EOFError
    except EOFError:
      self.__tela_produto.mostra_mensagem("Erro!","PRODUTO JÁ EXISTE !!!")
    else:
      produto = Produto(dados_produto["nome_produto"], dados_produto["marca"], dados_produto["modelo"], dados_produto["numero_serie"])
      self.__produtos.append(produto)
      self.__produtos_estocados.append(produto)

  def alterar_produto(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)

    if(produto is not None):
      novos_dados_produto = self.__tela_produto.pega_dados_produto()
      nome_produto = novos_dados_produto["nome_produto"]
      marca = novos_dados_produto["marca"]
      modelo = novos_dados_produto["modelo"]
      numero_serie = novos_dados_produto["numero_serie"]
      produto.nome_produto = nome_produto
      produto.marca = marca
      produto.modelo = modelo
      produto.numero_serie = numero_serie
      self.__tela_produto.mostra_mensagem("PRODUTO ALTERADO!", ("NUMERO DE SÉRIE: " + str(produto.numero_serie)))
    else:
      self.__tela_produto.mostra_mensagem("Erro!","PRODUTO NÃO EXISTENTE !!!")

  def listar_produtos_estocados(self):
    dados_produtos_estocados = []
    if len(self.__produtos_estocados) > 0:
      for produto in self.__produtos_estocados:
        dados_produtos_estocados.append({"nome_produto": produto.nome_produto, "marca": produto.marca, "modelo": produto.modelo, "numero_serie":produto.numero_serie})
      self.__tela_produto.mostra_produto(dados_produtos_estocados)
    else:
      self.__tela_produto.mostra_mensagem("Aviso!","!!! NÃO HÁ PRODUTOS EM ESTOQUE !!!")

  def listar_produtos_emprestados(self):
    if len(self.__produtos_emprestados) > 0:
      for produto in self.__produtos_emprestados:
         self.__tela_produto.mostra_produto({"nome_produto": produto.nome_produto, "marca": produto.marca, "modelo": produto.modelo, "numero_serie":produto.numero_serie})
    else:
      self.__tela_produto.mostra_mensagem("Aviso!","NÃO HÁ PRODUTOS EMPRESTADOS!.")

  def marcar_defeito(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    try:
      if produto is not None:
        codigo = self.__tela_produto.pega_codigo_defeito()
        defeito = self.__controlador_sistema.controlador_defeito.pega_defeito_codigo(codigo)
        try:
          if defeito is not None:
            produto.defeitos.append(defeito)
            self.__tela_produto.mostra_mensagem("DEFEITO MARCADO NO PRODUTO!",("Defeito marcado no produto! /n Produto Nº serie: " + str(produto.numero_serie) + "/n Defeito: " + str(defeito.titulo)))
        except:
          self.__tela_produto.mostra_mensagem("Erro!","!!! DEFEITO NÃO CADASTRADO !!!")
    except:
      self.__tela_produto.mostra_mensagem("Erro!","!!! PRODUTO NÃO ENCONTRADO !!!")

  def listar_defeitos(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    try:
      if len(produto.defeitos) > 0:
        for defeito in produto.defeitos:
          self.__tela_produto.mostra_defeitos(defeito)
    except:
      self.__tela_produto.mostra_mensagem("Erro!","!!! O PRODUTO NÃO POSSUI DEFEITOS!!!")

  def consertar_produto(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    try:
      if produto is not None:
        codigo = self.__tela_produto.pega_codigo_defeito()
        defeito = self.__controlador_sistema.controlador_defeito.pega_defeito_codigo(codigo)
        try:
          if defeito is not None:
            try:
              if defeito in produto.defeitos:
                produto.defeitos.remove(defeito)
                self.__tela_produto.mostra_mensagem("PRODUTO CONSERTADO!", ("Produto cosertado com sucesso! /n Produto Nº serie:" + str(produto.numero_serie)))
            except:
              self.__tela_produto.mostra_mensagem("Erro!","!!! O PRODUTO NÃO TEM ESSE DEFEITO !!!")
        except:
          self.__tela_produto.mostra_mensagem("Erro!","!!! DEFEITO NÃO CADASTRADO !!!")
    except:
      self.__tela_produto.mostra_mensagem("Erro!","!!! PRODUTO NÃO ENCONTRADO !!!")

  def incluir_caracteristica(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    dados_caracteristica = self.__tela_produto.pega_dados_nova_caracteristica()
    try:
      if dados_caracteristica is not None:
        valor = dados_caracteristica["valor"]
        descricao = dados_caracteristica["descricao"]
        codigo = dados_caracteristica["codigo"]
        caracteristica = Caracteristica(valor, descricao, codigo)
        produto.caracteristicas.append(caracteristica)
        self.__tela_produto.mostra_mensagem("CARACTERÍSTICA INCLUÍDA!",("Característica inclusa no produto. /n Produto N° serie: " + str(produto.numero_serie)))
        self.__controlador_sistema.controlador_caracteristica.caracteristicas.append(caracteristica)
    except:
      self.__tela_produto.mostra_mensagem("Erro!","!!! DADOS INVÁLIDOS, POR REFAÇA A OPERAÇÃO COM DADOS VÁLIDOS!!!")

  def alterar_caracteristicas(self):
    self.__controlador_sistema.controlador_caracteristica.abre_tela()

  def listar_caracteristicas(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    
    if len(produto.caracteristicas) > 0:
      for caracteristica in produto.caracteristicas:
        self.__tela_produto.mostra_caracteristicas(caracteristica)
    else:
      self.__tela_produto.mostra_mensagem("Erro!","O PRODUTO NÃO POSSUI CARACTERÍSTICAS DEFINIDAS!")

  def excluir_caracteristca(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    codigo = self.__tela_produto.seleciona_caracteristica()
    caracteristica = self.__controlador_sistema.controlador_caracteristica.pega_caracteristica_codigo(codigo)
    if caracteristica is not None:
      if caracteristica in produto.caracteristicas:
        produto.caracteristicas.remove(caracteristica)
        self.__controlador_sistema.controlador_caracteristica.caracteristicas.remove(caracteristica)
      else:
        self.__tela_produto.mostra_mensagem("Erro!","!!! O PRODUTO NÃO TEM ESSA CARACTERÍSTICA !!!")
    else:
      self.__tela_produto.mostra_mensagem("Erro!","!!! CARACTERÍSTICA NÃO EXISTENTE !!!")

  def excluir_produto(self):
    numero_serie = self.__tela_produto.seleciona_produto()
    produto = self.pega_produto_numero_serie(numero_serie)
    if produto in self.__produtos_emprestados:
      self.__tela_produto.mostra_mensagem("Erro!","Não é possível excluir produtos emprestados!")
    elif(produto is not None):
      self.__produtos.remove(produto)
      self.__produtos_estocados.remove(produto)
      self.__tela_produto.mostra_mensagem("PRODUTO EXCLUÍDO!", ("Produto excluído com sucesso /n Produto nº serie: "+str(produto.numero_serie)))
    else:
      self.__tela_produto.mostra_mensagem("Erro!","!!! PRODUTO NÃO EXISTENTE !!!")

  def retornar(self):
    self.__controlador_sistema.abre_tela()