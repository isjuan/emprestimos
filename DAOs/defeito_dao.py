from DAOs.dao import DAO
from Entidade.defeito import Defeito

#cada entidade terá uma classe dessa, implementação bem simples.
class DefeitoDAO(DAO):
    def __init__(self):
        super().__init__('defeitos.pkl')

    def add(self, defeito: Defeito):
        if (defeito is not None) and isinstance(defeito, Defeito) and isinstance(defeito.codigo, str):
            super().add(defeito.codigo, defeito)

    def update(self, defeito: Defeito):
        if (defeito is not None) and isinstance(defeito, Defeito) and isinstance(defeito.codigo, str):
            super().update(defeito.codigo, defeito)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)