from DAOs.dao import DAO
from Entidade.caracteristica import Caracteristica

#cada entidade terá uma classe dessa, implementação bem simples.
class CaracteristicaDAO(DAO):
    def __init__(self):
        super().__init__('caracteristicas.pkl')

    def add(self, caracteristica: Caracteristica):
        if (caracteristica is not None) and isinstance(caracteristica, Caracteristica) and isinstance(caracteristica.codigo, str):
            super().add(caracteristica.codigo, caracteristica)

    def update(self, caracteristica: Caracteristica):
        if (caracteristica is not None) and isinstance(caracteristica, Caracteristica) and isinstance(caracteristica.codigo, str):
            super().update(caracteristica.codigo, caracteristica)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)