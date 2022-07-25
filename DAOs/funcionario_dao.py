from DAOs.dao import DAO
from Entidade.funcionario import Funcionario


# cada entidade terá uma classe dessa, implementação bem simples.
class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.matricula,
                                                                                             int):
            super().add(funcionario.matricula, funcionario)

    def update(self, funcionario: Funcionario):
        if (funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.matricula,
                                                                                             int):
            super().update(funcionario.matricula, funcionario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
