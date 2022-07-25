from Tela.telaFuncionario import TelaFuncionario
from Entidade.funcionario import Funcionario
from DAOs.funcionario_dao import FuncionarioDAO

class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        # self.__funcionarios = []
        self.__funcionario_DAO = FuncionarioDAO()
        self.__tela_funcionario = TelaFuncionario(self)
        self.__controlador_sistema = controlador_sistema

    @property  # função usada pelo sistema
    def funcionarios(self):
        return self.__funcionario_DAO.get_all()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_funcionario, 2: self.lista_funcionarios, 3: self.alterar_funcionario,
                        4: self.excluir_funcionario, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_funcionario.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def pega_funcionario_por_matricula(self, matricula: int):
        for funcionario in self.__funcionario_DAO.get_all():
            if funcionario.matricula == matricula:
                return funcionario
        return None

    def cadastrar_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()

        try:
            for funcionario in self.funcionarios:
                if funcionario.matricula == dados_funcionario["matricula"]:
                    raise EOFError
            novo_funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["matricula"])
            self.__funcionario_DAO.add(novo_funcionario)
        except EOFError:

            self.__tela_funcionario.mostra_mensagem("Erro!", "!!! Matrícula já existe!!!")
            novo_funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["matricula"])
            self.__funcionario_DAO.add(novo_funcionario)

            self.__tela_funcionario.mostra_mensagem("!!! Matrícula já existe!!!")

    def lista_funcionarios(self):
        dados_funcionario = []
        for funcionario in self.__funcionario_DAO.get_all():
            dados_funcionario.append({"nome": funcionario.nome, "matricula": funcionario.matricula})
            # self.__tela_funcionario.mostra_funcionario({"nome": funcionario.nome, "matricula": funcionario.matricula}

        if len(dados_funcionario) < 1:
            self.__tela_funcionario.mostra_mensagem("lista vazia", "!!! Nenhum funcionário cadastrado!!!")
        else:
            self.__tela_funcionario.mostra_funcionario(dados_funcionario)

    def alterar_funcionario(self):

        self.lista_funcionarios()
        matricula_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_matricula(matricula_funcionario)

        if (funcionario is not None):
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            if novos_dados_funcionario["matricula"] == matricula_funcionario:
                funcionario.nome = novos_dados_funcionario["nome"]
                self.__funcionario_DAO.update(funcionario)
                self.__tela_funcionario.mostra_mensagem("Nome alterado!", "Nome do funcionario alterado com sucesso!")
            else:
                try:
                    for funcionario in self.__funcionario_DAO.get_all():
                        if funcionario.matricula == novos_dados_funcionario["matricula"]:
                            raise EOFError
                    self.__tela_funcionario.mostra_mensagem("Erro!","Não é possível alterar a matricula")
                except EOFError:
                    self.__tela_funcionario.mostra_mensagem("Erro!",
                                                            "!!! Matrícula já utilizada por outro funcionário!!!")
            self.lista_funcionarios()
        else:
            self.__tela_funcionario.mostra_mensagem("Erro!", "!!! FUNCIONARIO NÃO EXISTENTE !!!")

    def excluir_funcionario(self):
        self.lista_funcionarios()
        matricula_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_matricula(matricula_funcionario)

        if funcionario is not None:
            self.__funcionario_DAO.remove(funcionario.matricula)
            self.__tela_funcionario.mostra_mensagem("funcionário removido",
                                                    "Funcionário removido. Lista de funcionários atualizada.")
            self.lista_funcionarios()
        else:
            self.__tela_funcionario.mostra_mensagem("Erro!", "!!!!! FUNCIONARIO NÃO EXISTENTE !!!")

