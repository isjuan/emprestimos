from abc import ABC, abstractmethod

class TelaAbstrata(ABC):
  @abstractmethod
  def __init__(self):
    pass

  def mostra_opcoes(self):
    pass

  def mostra_mensagem(self, msg):
    print(msg)

  def excecao_num_int(self, mensagem: str, inteiros_validos: []):
    while True:
      valor_lido = input(mensagem)
      try:
        inteiro = int(valor_lido)
        if inteiros_validos and inteiro not in inteiros_validos:
          raise ValueError
        return inteiro
      except ValueError:
        print("Opção inválida, digite uma das seguintes opções:", inteiros_validos)

  def excecao_tipo_int(self, mensagem: str, tipo_var):
    while True:
      valor_lido = input(mensagem)
      try:
        resultado = tipo_var(valor_lido)
        if isinstance(resultado, tipo_var):
          return resultado
      except ValueError:
        print("Tipo de caractere errado, digite um do tipo:", tipo_var)  