from Tela.telaDefeito import TelaDefeito
from Entidade.defeito import Defeito

class ControladorDefeito:
  def __init__(self, controlador_sistema):
    self.__tela_defeito = TelaDefeito(self)
    self.__controlador_sistema = controlador_sistema
    self.__defeitos = []

  @property
  def defeitos(self):
    return self.__defeitos

  def listar_defeitos(self):
    if len(self.__defeitos) > 0:
      for defeito in self.__defeitos:
        self.__tela_defeito.mostra_defeito({"titulo": defeito.titulo, "descricao": defeito.descricao, "codigo": defeito.codigo})
    else:
      self.__tela_defeito.mostra_mensagem("Aviso!","Não há defeitos cadastrados!")

  def pega_defeito_codigo(self, codigo: str):
    for defeito in self.__defeitos:
      if(defeito.codigo == codigo):
        return defeito
    return None

  def incluir_defeito(self):
    dados_defeito = self.__tela_defeito.pega_dados_defeito()
    titulo = dados_defeito["titulo"]
    descricao = dados_defeito["descricao"]
    codigo = dados_defeito["codigo"]
    defeito = Defeito(titulo, descricao, codigo)
    if isinstance(defeito, Defeito):
      self.defeitos.append(defeito)

  def alterar_titulo(self):
    codigo = self.__tela_defeito.seleciona_defeito()
    defeito = self.pega_defeito_codigo(codigo)
    if isinstance(defeito, Defeito) and defeito in self.__defeitos:
      novo_titulo = self.__tela_defeito.pega_dados_titulo()
      defeito.titulo = novo_titulo
    else:
      self.__tela_defeito.mostra_mensagem("Dados Inválidos!","Por favor repita a operação com dados válidos: Defeito cadastrado no sistema e título válido!")

  def alterar_descricao(self):
    codigo = self.__tela_defeito.seleciona_defeito()
    defeito = self.pega_defeito_codigo(codigo)
    if isinstance(defeito, Defeito) and defeito in self.__defeitos:
      nova_descricao = self.__tela_defeito.pega_dados_descricao()
      defeito.descricao = nova_descricao
    else:
      self.__tela_defeito.mostra_mensagem("Dados Inválidos!","Por favor repita a operação com dados válidos: Defeito cadastrado no sistema e descricao válida!")

  def excluir_defeito(self):
    codigo = self.__tela_defeito.seleciona_defeito()
    defeito = self.pega_defeito_codigo(codigo)
    if isinstance(defeito, Defeito) and defeito in self.__defeitos:
      self.__defeitos.remove(defeito)
    else:
      self.__tela_defeito.mostra_mensagem("Dados inválidos!","Por favor repita a operação com parâmetros válidos: Defeito cadastrado no sistema")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {0: self.retornar, 1: self.incluir_defeito, 2: self.listar_defeitos, 3: self.alterar_titulo, 4: self.alterar_descricao, 5: self.excluir_defeito}
    continua = True
    while continua:       
      lista_opcoes[self.__tela_defeito.tela_opcoes()]()
