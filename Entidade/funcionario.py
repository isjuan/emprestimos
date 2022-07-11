class Funcionario:
  def __init__(self, nome: str, matricula: int): 
    #if isinstance(nome, str):
    self.__nome = nome
    # if isinstance(matricula, int):
    self.__matricula = matricula

  @property
  def nome(self):
    return self.__nome

  @property
  def matricula(self):
    return self.__matricula

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @matricula.setter
  def matricula(self, matricula):
    self.__matricula = matricula
