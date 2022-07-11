from Entidade.caracteristica import Caracteristica
from Entidade.defeito import Defeito

class Produto:
  def __init__(self,nome_produto: str, marca: str, modelo: str, numero_serie: int):
    self.__numero_serie = numero_serie
    self.__modelo = modelo
    self.__marca = marca
    self.__nome_produto = nome_produto
    self.__defeitos = []
    self.__caracteristicas = []

    if isinstance(nome_produto, str):
      self.__nome_produto = nome_produto
    if isinstance(marca, str):
      self.__marca = marca
    if isinstance(modelo, str):
      self.__modelo = modelo
    if isinstance(numero_serie, int):
      self.__numero_serie = numero_serie

  @property
  def nome_produto(self):
    return self.__nome_produto

  @property
  def marca(self):
    return self.__marca

  @property
  def modelo(self):
    return self.__modelo

  @property
  def numero_serie(self):
    return self.__numero_serie

  @property
  def defeitos(self):
    return self.__defeitos

  @property
  def caracteristicas(self):
    return self.__caracteristicas

  @nome_produto.setter
  def nome_produto(self, nome_produto: str):
    if isinstance(nome_produto, str):
      self.__nome_produto = nome_produto

  @marca.setter
  def marca(self, marca: str):
    if isinstance(marca, str):
      self.__marca = marca

  @modelo.setter
  def modelo(self, modelo: str):
    if isinstance(modelo, str):
      self.__modelo = modelo

  @numero_serie.setter
  def numero_serie(self, numero_serie: int):
    if isinstance(numero_serie, int):
      self.__numero_serie = numero_serie

  @defeitos.setter
  def defeito(self, defeito: Defeito):
    if isinstance(defeito, Defeito):
      self.__defeitos.append(defeito)

  @caracteristicas.setter
  def caracteristicas(self, valor: str, descricao: str):
    if isinstance(valor, str) and isinstance(descricao, str):
      self.__caracteristicas.append(Caracteristica(valor, descricao))
