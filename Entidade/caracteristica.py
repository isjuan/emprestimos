class Caracteristica:
  def __init__(self, valor: str, descricao: str, codigo: int):
    if isinstance(valor, str):
      self.__valor = valor
    if isinstance(descricao, str):
      self.__descricao = descricao
    if isinstance(codigo, str):
      self.__codigo = codigo

  @property
  def valor(self):
    return self.__valor

  @property
  def descricao(self):
    return self.__descricao

  @property
  def codigo(self):
    return self.__codigo

  @valor.setter
  def valor(self, valor: str):
    if isinstance(valor, str):
      self.__valor = valor

  @descricao.setter
  def descricao(self, descricao: str):
    if isinstance(descricao, str):
      self.__descricao = descricao

  @codigo.setter
  def codigo (self, codigo: str):
    if isinstance(codigo, str):
      self.__codigo = codigo
