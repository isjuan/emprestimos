from Entidade.emprestimo import Emprestimo
#from Controlador.controladorProduto import ControladorProduto
#from Controlador.controladorFunionario import ControladorFuncionario
from Tela.telaEmprestimo import TelaEmprestimo
#import datetime

class ControladorEmprestimo:

  def __init__(self, controlador_sistema):
    self.__tela_emprestimo = TelaEmprestimo(self)
    self.__controlador_sistema = controlador_sistema
    self.__emprestimos = []
    self.__data_emprestimos = {}

  @property
  def emprestimos(self):
    return self.__emprestimos

  def pega_emprestimo_codigo(self, codigo: int):
    for emprestimo in self.__emprestimos:
      if(emprestimo.codigo == codigo):
        return emprestimo
    return None
 
  def lista_emprestimo(self):
    
    if len(self.emprestimos) > 0:
      for emprestimo in self.emprestimos:
        self.__tela_emprestimo.mostra_emprestimo(emprestimo)
    else:
      self.__tela_emprestimo.mostra_mensagem("NÃO HÁ EMPRÉSTIMOS REALIZADOS!!!")

  def incluir_emprestimo(self):
    dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
    codigo = dados_emprestimo["codigo"]
    funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_por_matricula(dados_emprestimo["matricula"])
    produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(dados_emprestimo["numero_serie"])
    emprestimo = Emprestimo(funcionario, produto, codigo)
    self.__emprestimos.append(emprestimo)
    self.__controlador_sistema.controlador_produto.produtos_estocados.remove(produto)
    self.__controlador_sistema.controlador_produto.produtos_emprestados.append(produto)
    

  def remover_emprestimo(self):
    codigo = self.__tela_emprestimo.seleciona_emprestimo()
    emprestimo = self.pega_emprestimo_codigo(codigo)
    produto = emprestimo.produto
    if emprestimo in self.__emprestimos:
      self.__emprestimos.remove(emprestimo)
      self.__controlador_sistema.controlador_produto.produtos.append(produto)
      self.__controlador_sistema.controlador_produto.produtos_emprestados.remove(produto)
#      if emprestimo in self.__data_emprestimos:
#        self.__data_emprestimos.pop(emprestimo)
#
#  def data_emprestimo(self, emprestimo: Emprestimo, data: datetime.date):
#    if isinstance(emprestimo, Emprestimo) and isinstance (data, datetime.date):
#      self.__data_emprestimos[emprestimo] = data

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_emprestimo, 2: self.remover_emprestimo, 3: self.lista_emprestimo, 0: self.retornar}

    flag = True
    while flag:
      lista_opcoes[self.__tela_emprestimo.tela_opcoes()]()

