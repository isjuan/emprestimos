from Entidade.emprestimo import Emprestimo
from Tela.telaEmprestimo import TelaEmprestimo

class ControladorEmprestimo:

  def __init__(self, controlador_sistema):
    self.__tela_emprestimo = TelaEmprestimo(self)
    self.__controlador_sistema = controlador_sistema
    self.__emprestimos = []

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
    numero_serie = self.__tela_emprestimo.seleciona_produto()
    produto = self.__controlador_sistema.controlador_produto.pega_produto_numero_serie(numero_serie)
    try:
      if produto is not None:
        matricula = self.__tela_emprestimo.seleciona_funcionario()
        funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_por_matricula(matricula)
        try:
          if funcionario is not None:
            codigo = self.__tela_emprestimo.pega_codigo_emprestimo()
            emprestimo = Emprestimo(produto, funcionario, codigo)
            self.__emprestimos.append(emprestimo)
            self.__controlador_sistema.controlador_produto.produtos_emprestados.append(produto)
            self.__controlador_sistema.controlador_produto.produtos_estocados.remove(produto)
        except:
            self.__tela_emprestimo.mostra_mensagem("!!! FUNCIONÁRIO NÃO EXISTENTE! INSIRA UMA MATRÍCULA VÁLIDA !!!")
    except:
      self.__tela_emprestimo.mostra_mensagem("!!! PRODUTO NÃO EXISTENTE! INSIRA UM NÚMERO DE SÉRIE VÁLIDO !!!")

  def remover_emprestimo(self):
    codigo = self.__tela_emprestimo.seleciona_emprestimo()
    emprestimo = self.pega_emprestimo_codigo(codigo)
    try:
      if emprestimo in self.__emprestimos:
        produto = emprestimo.produto
        self.__emprestimos.remove(emprestimo)
        self.__controlador_sistema.controlador_produto.produtos.append(produto)
        self.__controlador_sistema.controlador_produto.produtos_emprestados.remove(produto)
    except:
      self.__tela_emprestimo.mostra_mensagem("!!! EMPRÉSTIMO NÃO EXISTENTE! INSIRA UM CÓDIGO VÁLIDO !!!")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_emprestimo, 2: self.remover_emprestimo, 3: self.lista_emprestimo, 0: self.retornar}

    flag = True
    while flag:
      lista_opcoes[self.__tela_emprestimo.tela_opcoes()]()
