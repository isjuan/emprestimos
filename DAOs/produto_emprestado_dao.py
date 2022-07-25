from DAOs.dao import DAO
from Entidade.produto import Produto

class ProdutoEmprestadoDAO(DAO):
    def __init__(self):
        super().__init__('produtos_emprestrados.pkl')

    def add(self, produto: Produto):
        if (produto is not None) and isinstance(produto, Produto) and isinstance(produto.numero_serie, int):
            super().add(produto.numero_serie, produto)

    def update(self, produto: Produto):
        if (produto is not None) and isinstance(produto, Produto) and isinstance(produto.numero_serie, int):
            super().update(produto.numero_serie, produto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)