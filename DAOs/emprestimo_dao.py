from DAOs.dao import DAO
from Entidade.emprestimo import Emprestimo


# cada entidade terá uma classe dessa, implementação bem simples.
class EmprestimoDAO(DAO):
    def __init__(self):
        super().__init__('emprestimos.pkl')

    def add(self, emprestimo: Emprestimo):
        if (emprestimo is not None) and isinstance(emprestimo, Emprestimo) and isinstance(emprestimo.codigo,
                                                                                          str):
            super().add(emprestimo.codigo, emprestimo)

    def update(self, emprestimo: Emprestimo):
        if (emprestimo is not None) and isinstance(emprestimo, Emprestimo) and isinstance(emprestimo.codigo,
                                                                                          str):
            super().update(emprestimo.codigo, emprestimo)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
