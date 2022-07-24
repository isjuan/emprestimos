from abc import ABC, abstractmethod
from typing import List
import PySimpleGUI as sg

class TelaAbstrata(ABC):
  @abstractmethod
  def __init__(self):
    pass

  def mostra_opcoes(self):
    pass

  def mostra_mensagem(self, titulo: str, msg: str):
    sg.popup(titulo, msg)

  def excecao_num_int(self, mensagem: str, inteiros_validos: List):
    while True:
      valor_lido = input(mensagem)
      try:
        inteiro = int(valor_lido)
        if inteiros_validos and inteiro not in inteiros_validos:
          raise ValueError
        return inteiro
      except ValueError:
        self.mostra_mensagem("Aviso!",("Opção inválida, digite uma das seguintes opções:", inteiros_validos))

  def excecao_tipo_int(self, mensagem: str, tipo_var):
    try:
      resultado = int(mensagem)
      return resultado
    except Exception:
      self.mostra_mensagem("Aviso!",("Tipo de caractere errado, digite um do tipo:", tipo_var))