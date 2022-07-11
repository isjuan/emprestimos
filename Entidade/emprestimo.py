from Entidade.produto import Produto
from Entidade.funcionario import Funcionario

class Emprestimo:
  def __init__(self, produto: Produto, funcionario: Funcionario, codigo: str):
 #   if isinstance(produto, Produto):
    self.__produto = produto
 #   if isinstance(funcionario, Funcionario):
    self.__funcionario = funcionario
  #  if isinstance(codigo, str):
    self.__codigo = codigo

  @property
  def produto(self):
    return self.__produto

  @property
  def funcionario(self):
    return self.__funcionario

  @property
  def codigo(self):
    return self.__codigo

  @produto.setter
  def produto(self, produto):
    if isinstance(produto, Produto):
      self.__produto = produto

  @funcionario.setter
  def funcionario(self, funcionario):
    if isinstance(funcionario, Funcionario):
      self.__funcionario = funcionario

  @codigo.setter
  def codigo (self, codigo: str):
    if isinstance(codigo, str):
      self.__codigo = codigo
