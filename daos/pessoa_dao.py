
from daos.dao import DAO
from model.pessoa import Pessoa

class PessoaDAO(DAO):
    def __init__(self):
        # Cria apenas um arquivo para guardar todas as pessoas
        super().__init__('pessoas.pkl')

    def add(self, pessoa: Pessoa):
        # Aceita qualquer objeto que herde de Pessoa (Profissional ou Paciente)
        if isinstance(pessoa, Pessoa) and pessoa.cpf:
            super().add(pessoa.cpf, pessoa)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)