from Entidade.emprestimo import Emprestimo
from Tela.telaEmprestimo import TelaEmprestimo
from DAOs.emprestimo_dao import EmprestimoDAO

class ControladorEmprestimo:

  def __init__(self, controlador_sistema):
    self.__tela_emprestimo = TelaEmprestimo(self)
    self.__controlador_sistema = controlador_sistema
    # self.__emprestimos = []
    self.__emprestimos_DAO = EmprestimoDAO()

  @property
  def emprestimos(self):
    return self.__emprestimos_DAO.get_all()

  def pega_emprestimo_codigo(self, codigo: int):
    for emprestimo in self.__emprestimos_DAO.get_all():
      if(emprestimo.codigo == codigo):
        return emprestimo
    return None
 
  def lista_emprestimo(self):
    if len(self.emprestimos) > 0:
      self.__tela_emprestimo.mostra_emprestimo(self)
    else:
      self.__tela_emprestimo.mostra_mensagem("Erro!","NÃO HÁ EMPRÉSTIMOS REALIZADOS!!!")

  def incluir_emprestimo(self):
    dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
    numero_serie = dados_emprestimo['numero_serie']#self.__tela_emprestimo.seleciona_produto()
    produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
    try:
      if produto is not None:
        matricula = dados_emprestimo['matricula']#self.__tela_emprestimo.seleciona_funcionario()
        funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_por_matricula(matricula)
        try:
          if funcionario is not None:
            codigo = dados_emprestimo['codigo']#self.__tela_emprestimo.pega_codigo_emprestimo()
            emprestimo = Emprestimo(produto, funcionario, codigo)
            self.__emprestimos_DAO.add(emprestimo)
            self.__controlador_sistema.controlador_produto.add_emprestado(produto)
            self.__controlador_sistema.controlador_produto.remove_estocado(produto)
        except:
            self.__tela_emprestimo.mostra_mensagem("Erro!","!!! FUNCIONÁRIO NÃO EXISTENTE! INSIRA UMA MATRÍCULA VÁLIDA !!!")
    except:
      self.__tela_emprestimo.mostra_mensagem("Erro!","!!! PRODUTO NÃO EXISTENTE! INSIRA UM NÚMERO DE SÉRIE VÁLIDO !!!")

  def remover_emprestimo(self):
    codigo = self.__tela_emprestimo.seleciona_emprestimo()
    emprestimo = self.pega_emprestimo_codigo(codigo)
    try:
      if emprestimo in self.__emprestimos_DAO.get_all():
        produto = emprestimo.produto
        self.__emprestimos_DAO.remove(emprestimo.codigo)
        self.__controlador_sistema.controlador_produto.add_estocado(produto)
        self.__controlador_sistema.controlador_produto.remove_emprestado(produto)
    except:
      self.__tela_emprestimo.mostra_mensagem("Erro!","EMPRÉSTIMO NÃO EXISTENTE! INSIRA UM CÓDIGO VÁLIDO!")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_emprestimo, 2: self.remover_emprestimo, 3: self.lista_emprestimo, 0: self.retornar}

    while True:
      opcao_escolhida = self.__tela_emprestimo.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()
