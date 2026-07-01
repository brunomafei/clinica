from daos.dao import DAO
from model.clinica import Clinica

class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica: Clinica):
        if isinstance(clinica, Clinica) and clinica.nome:
            super().add(clinica.nome, clinica) # Usando o nome como chave

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)