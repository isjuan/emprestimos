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

  def pega_caracteristica_codigo(self, codigo: int):
    for caracteristica in self.__caracteristicas:
      if(caracteristica.codigo == codigo):
          return caracteristica
      else:
        self.__tela_caracteristica.mostra_mensagem("ESTA CARACTERÍSTICA NÃO EXISTE!!!")

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
              if caracteristica in produto.__caracteristicas:
                novo_valor = self.__tela_caracteristica.pega_dados_valor()
                caracteristica.__valor = novo_valor
                self.__tela_caracteristica.mostra_mensagem("Valor da característica alterado")
            except:
              self.__tela_caracteristica.mostra_mensagem("ESTE PRODUTO NÃO POSSUI ESSA CARACTERÍSTICA!!!")
        except:
          self.__tela_caracteristica.mostra_mensagem("ESTE PRODUTO NÃO EXISTE!!!")
    except:
      self.__tela_caracteristica.mostra_mensagem("ESTA CARACTERÍSTICA NÃO EXISTE!!!")

  def alterar_descricao(self):
    codigo = self.__tela_caracteristica.seleciona_caracteristica()
    numero_serie = self.__tela_caracteristica.seleciona_produto()
    caracteristica = self.pega_caracteristica_codigo(codigo)
    try:
      if caracteristica in self.__caracteristicas:
        produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
        try:
          if produto in self.__controlador_sistema.controlador_produto.produtos:
            try:
              if caracteristica in produto.__caracteristicas:
                nova_descricao = self.__tela_caracteristica.pega_dados_descricao()
                caracteristica.descricao = nova_descricao
                self.__tela_caracteristica.mostra_mensagem("Descrição da característica alterada")
            except:
              self.__tela_caracteristica.mostra_mensagem("!!! ESTE PRODUTO NÃO POSSUI ESSA CARACTERÍSTICA !!!")
        except:
          self.__tela_caracteristica.mostra_mensagem("!!! ESTE PRODUTO NÃO EXISTE !!!")
    except:
      self.__tela_caracteristica.mostra_mensagem("!!! ESTA CARACTERÍSTICA NÃO EXISTE !!!")

  def alterar_codigo(self):
    codigo = self.__tela_caracteristica.seleciona_caracteristica()
    numero_serie = self.__tela_caracteristica.seleciona_produto()
    caracteristica = self.pega_caracteristica_codigo(codigo)
    try:
      if caracteristica in self.__caracteristicas:
        produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
        try:
          if produto in self.__controlador_sistema.controlador_produto.produtos:
            try:
              if caracteristica in produto.__caracteristicas:
                novo_codigo = self.__tela_caracteristica.pega_dados_codigo()
                caracteristica.codigo = novo_codigo
                self.__tela_caracteristica.mostra_mensagem("Codigo da característica alterado")
            except:
              self.__tela_caracteristica.mostra_mensagem("!!! ESTE PRODUTO NÃO POSSUI ESSA CARACTERÍSTICA !!!")
        except:
          self.__tela_caracteristica.mostra_mensagem("!!! ESTE PRODUTO NÃO EXISTE !!!")
    except:
      self.__tela_caracteristica.mostra_mensagem("!!! ESTA CARACTERÍSTICA NÃO EXISTE !!!")

  def retornar(self):
    self.__controlador_sistema.controlador_produto.abre_tela()

  def abre_tela(self):
    lista_opcoes = {0: self.retornar,1: self.alterar_valor, 2: self.alterar_descricao, 3: self.alterar_codigo}
    continua = True
    while continua:       
      lista_opcoes[self.__tela_caracteristica.tela_opcoes()]()
