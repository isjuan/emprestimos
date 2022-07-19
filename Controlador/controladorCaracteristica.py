from Tela.telaCaracteristica import TelaCaracteristica
from Entidade.caracteristica import Caracteristica
from Entidade.produto import Produto

class ControladorCaracteristica:
  def __init__(self, controlador_sistema):
    self.__tela_caracteristica = TelaCaracteristica(self)
    self.__controlador_sistema = controlador_sistema
    self.__caracteristicas = []

  @property
  def caracteristicas(self):
    return self.__caracteristicas

  def pega_caracteristica_codigo(self, codigo: str):
    for caracteristica in self.__caracteristicas:
      if(caracteristica.codigo == codigo):
        return caracteristica
    return None

  def pega_caracteristica_no_produto(self, codigo: str, produto: Produto):
    for caracteristica in produto.caracteristicas:
      if(caracteristica.codigo == codigo):
        return caracteristica
    return None

  def alterar_valor(self):
    codigo = self.__tela_caracteristica.seleciona_caracteristica()
    numero_serie = self.__tela_caracteristica.seleciona_produto()
    caracteristica = self.pega_caracteristica_codigo(codigo)
    try:
      if caracteristica is not None:
        produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
        try:
          if produto is not None:
            try:
              caracteristica_no_produto = self.pega_caracteristica_no_produto(codigo, produto)
              if caracteristica_no_produto is not None:
                novo_valor = self.__tela_caracteristica.pega_dados_valor()
                caracteristica.valor = novo_valor
                self.__tela_caracteristica.mostra_mensagem("Valor Alterado!", ("Valor da caracteristica alterado com sucesso! /n Valor: " + str(caracteristica.valor)))
            except:
              self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTE PRODUTO NÃO POSSUI ESSA CARACTERÍSTICA !!!")
        except:
          self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTE PRODUTO NÃO EXISTE !!!")
    except:
      self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTA CARACTERÍSTICA NÃO EXISTE !!!")

  def alterar_descricao(self):
    codigo = self.__tela_caracteristica.seleciona_caracteristica()
    numero_serie = self.__tela_caracteristica.seleciona_produto()
    caracteristica = self.pega_caracteristica_codigo(codigo)
    try:
      if caracteristica is not None:
        produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
        try:
          if produto is not None:
            try:
              caracteristica_no_produto = self.pega_caracteristica_no_produto(codigo, produto)
              if caracteristica_no_produto is not None:
                nova_descricao = self.__tela_caracteristica.pega_dados_descricao()
                caracteristica.descricao = nova_descricao
                self.__tela_caracteristica.mostra_mensagem("DESCRIÇÃO ALTERADA!", ("Descrição da caracteristica alterada com sucesso! /n Descrição: " + str(caracteristica.descricao)))
            except:
              self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTE PRODUTO NÃO POSSUI ESSA CARACTERÍSTICA !!!")
        except:
          self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTE PRODUTO NÃO EXISTE !!!")
    except:
      self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTA CARACTERÍSTICA NÃO EXISTE !!!")

  def alterar_codigo(self):
    codigo = self.__tela_caracteristica.seleciona_caracteristica()
    numero_serie = self.__tela_caracteristica.seleciona_produto()
    caracteristica = self.pega_caracteristica_codigo(codigo)
    try:
      if caracteristica is not None:
        produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
        try:
          if produto is not None:
            try:
              caracteristica_no_produto = self.pega_caracteristica_no_produto(codigo, produto)
              if caracteristica_no_produto is not None:
                novo_codigo = self.__tela_caracteristica.pega_dados_codigo()
                caracteristica.codigo = novo_codigo
                self.__tela_caracteristica.mostra_mensagem("CÓDIGO ALTERADO!", ("Código da caracteristica alterado com sucesso! /n Código: " + str(caracteristica.codigo)))
            except:
              self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTE PRODUTO NÃO POSSUI ESSA CARACTERÍSTICA !!!")
        except:
          self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTE PRODUTO NÃO EXISTE !!!")
    except:
      self.__tela_caracteristica.mostra_mensagem("ERRO!","!!! ESTA CARACTERÍSTICA NÃO EXISTE !!!")

  def retornar(self):
    self.__controlador_sistema.controlador_produto.abre_tela()

  def abre_tela(self):
    lista_opcoes = {0: self.retornar,1: self.alterar_valor, 2: self.alterar_descricao, 3: self.alterar_codigo}
    continua = True
    while continua:       
      lista_opcoes[self.__tela_caracteristica.tela_opcoes()]()
