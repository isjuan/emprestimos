import PySimpleGUI as sg
from Tela.telaAbstrata import TelaAbstrata

class TelaDefeito(TelaAbstrata):
  def __init__(self, controlador):
    super().__init__()
    self.__controlador = controlador
    #self.__tela_abstrata = TelaAbstrata()

  def tela_opcoes(self):
    print("-------- DEFEITO ----------")
    print("Escolha a opcao")
    print("1 - Novo defeito")
    print("2 - Listar defeitos")
    print("3 - Alterar titulo")
    print("4 - Alterar descrição")
    print("5 - Excluir defeito")
    print("0 - Retornar")

    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,5,0])
    return opcao

  def pega_dados_defeito(self):
    print("-------- NOVO DEFEITO ----------")
    titulo = input("Titulo: ")
    descricao = input("Descricao: ")
    codigo = input("Codigo: ")
    return {"titulo": titulo, "descricao": descricao, "codigo": codigo}

  def pega_dados_titulo(self):
    print("-------- NOVO TÍTULO ----------")
    titulo = input("Titulo: ")
    return titulo

  def pega_dados_descricao(self):
    print("-------- NOVA DESCRIÇÃO ----------")
    descricao = input("Descricao: ")
    return descricao

  def pega_dados_codigo(self):
    print("-------- NOVO CÓDIGO ----------")
    codigo = input("Novo Código: ")
    return codigo

  def seleciona_defeito(self):
    codigo = input("Código do Defeito: ")
    return codigo

  def mostra_defeito(self, dados_defeito):
    print("\n")
    print("-------DEFEITOS CADASTRADOS-----")
    print("TITULO: ", dados_defeito["titulo"])
    print("DESCRIÇÃO: ", dados_defeito["descricao"])
    print("CÓDIGO: ", dados_defeito["codigo"])
    print("\n")
