from Tela.telaDefeito import TelaDefeito
from Entidade.defeito import Defeito
from DAOs.defeito_dao import DefeitoDAO

class ControladorDefeito:
  def __init__(self, controlador_sistema):
    self.__defeito_DAO = DefeitoDAO()
    self.__tela_defeito = TelaDefeito(self)
    self.__controlador_sistema = controlador_sistema
    #self.__defeitos = []

  @property
  def defeitos(self):
    return self.__defeito_DAO.get_all()

  def listar_defeitos(self):
    if len(self.__defeito_DAO.get_all()) > 0:
      self.__tela_defeito.lista_defeitos(self)
#      for defeito in self.__defeitos:
#        self.__tela_defeito.mostra_defeito({"titulo": defeito.titulo, "descricao": defeito.descricao, "codigo": defeito.codigo})
    else:
      self.__tela_defeito.mostra_mensagem("Aviso!","Não há defeitos cadastrados!")

  def pega_defeito_codigo(self, codigo: str):
    for defeito in self.__defeito_DAO.get_all():
      if(defeito.codigo == codigo):
        return defeito
    return None

  def incluir_defeito(self):
    dados_defeito = self.__tela_defeito.pega_dados_defeito()
    titulo = dados_defeito["titulo"]
    descricao = dados_defeito["descricao"]
    codigo = dados_defeito["codigo"]
    novo_defeito = Defeito(titulo, descricao, codigo)
    if isinstance(novo_defeito, Defeito):
#      self.defeitos.append(novo_defeito)
      self.__defeito_DAO.add(novo_defeito)

  def alterar_titulo(self):
    dados = self.__tela_defeito.pega_dados_titulo()
    defeito = self.pega_defeito_codigo(dados['codigo'])
    if isinstance(defeito, Defeito) and defeito in self.__defeito_DAO.get_all():
      defeito.titulo = dados['titulo']
    else:
      self.__tela_defeito.mostra_mensagem("Dados Inválidos!","Por favor repita a operação com dados válidos: Defeito cadastrado no sistema e título válido!")

  def alterar_descricao(self):
    dados = self.__tela_defeito.pega_dados_descricao()
    defeito = self.pega_defeito_codigo(dados['codigo'])
    if isinstance(defeito, Defeito) and defeito in self.__defeito_DAO.get_all():
      defeito.descricao = dados['descricao']
      self.__defeito_DAO.update(defeito)
    else:
      self.__tela_defeito.mostra_mensagem("Dados Inválidos!","Por favor repita a operação com dados válidos: Defeito cadastrado no sistema e descricao válida!")

  def excluir_defeito(self):
    codigo = self.__tela_defeito.seleciona_defeito()
    defeito = self.pega_defeito_codigo(codigo)
    if isinstance(defeito, Defeito) and defeito in self.__defeito_DAO.get_all():
#      self.__defeitos.remove(defeito)
      self.__defeito_DAO.remove(defeito.codigo)
    else:
      self.__tela_defeito.mostra_mensagem("Dados inválidos!","Por favor repita a operação com parâmetros válidos: Defeito cadastrado no sistema")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {0: self.retornar, 1: self.incluir_defeito, 2: self.listar_defeitos, 3: self.alterar_titulo, 4: self.alterar_descricao, 5: self.excluir_defeito}
    continua = True
    while continua:       
      lista_opcoes[self.__tela_defeito.tela_opcoes()]()
