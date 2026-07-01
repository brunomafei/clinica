from daos.dao import DAO
from model.procedimento import Procedimento

class ProcedimentoDAO(DAO):
    def __init__(self):
        super().__init__('procedimentos.pkl')

    def add(self, procedimento: Procedimento):
        if isinstance(procedimento, Procedimento) and procedimento.id_procedimento:
            super().add(procedimento.id_procedimento, procedimento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)