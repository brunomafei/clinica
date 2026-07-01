from daos.dao import DAO
from model.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento):
        # Geralmente atendimentos usam um 'id', 'numero' ou 'codigo' autogerado
        if isinstance(atendimento, Atendimento) and atendimento.id:
            super().add(atendimento.id, atendimento)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)