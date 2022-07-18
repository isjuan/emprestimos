class Defeito:
  def __init__(self, titulo: str, descricao: str, codigo: str):
    if isinstance(titulo, str):
      self.__titulo = titulo
    if isinstance(descricao, str):
      self.__descricao = descricao
    if isinstance(codigo, str):
      self.__codigo = codigo

  @property
  def titulo(self):
    return self.__titulo

  @property
  def descricao(self):
    return self.__descricao

  @property
  def codigo(self):
    return self.__codigo

  @titulo.setter
  def titulo(self, titulo):
    self.__titulo = titulo

  @descricao.setter
  def descricao(self, descricao):
    self.__descricao = descricao

  @codigo.setter
  def codigo (self, codigo: str):
    if isinstance(codigo, str):
      self.__codigo = codigo
