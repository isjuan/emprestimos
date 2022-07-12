from Controlador.controladorEmprestimo import ControladorEmprestimo
from Controlador.controladorCaracteristica import ControladorCaracteristica
from Controlador.controladorProduto import ControladorProduto
from Controlador.controladorDefeito import ControladorDefeito
from Controlador.controladorFunionario import ControladorFuncionario

from Tela.telaSistema import TelaSistema

class ControladorSistema:
  def __init__(self):
    self.__tela_sistema = TelaSistema()
    self.__controlador_caracteristica = ControladorCaracteristica(self)
    self.__controlador_produto = ControladorProduto(self)
    self.__controlador_emprestimo = ControladorEmprestimo(self)
    self.__controlador_defeito = ControladorDefeito(self)
    self.__controlador_funcionario = ControladorFuncionario(self)

  @property
  def controlador_funcionario(self):
    return self.__controlador_funcionario

  @property
  def controlador_produto(self):
    return self.__controlador_produto
  
  @property
  def controlador_defeito(self):
    return self.__controlador_defeito

  @property
  def controlador_caracteristica(self):
    return self.__controlador_caracteristica

  @property
  def controlador_emprestimo(self):
    return self.__controlador_emprestimo

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_funcionario, 2: self.cadastrar_produto, 3: self.cadastrar_emprestimo, 4: self.cadastrar_defeito, 0: self.finalizar}

    while True:
      opcao_escolhida = self.__tela_sistema.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()
    
  def inicializa_sistema(self):
    self.abre_tela()

  def cadastrar_funcionario(self):
    self.__controlador_funcionario.abre_tela()
    
  def cadastrar_produto(self):
    self.__controlador_produto.abre_tela()

  def cadastrar_emprestimo(self):
    if len(self.__controlador_funcionario.funcionarios) > 0 and len(self.__controlador_produto.produtos) > 0:
      self.__controlador_emprestimo.abre_tela()
    else:
      self.__tela_sistema.mostra_mensagem("Nenhum funcionário e/ou produto cadastrado(s)!!!")

  def cadastrar_defeito(self):
    self.__controlador_defeito.abre_tela()

  def finalizar(self):
    exit(0)

    

    