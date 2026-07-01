from daos.dao import DAO
from model.pagamento import Pagamento 

class PagamentoDAO(DAO):
    def __init__(self):
        # Todos os tipos de pagamento ficarão salvos no mesmo arquivo
        super().__init__('pagamentos.pkl')

    def add(self, pagamento: Pagamento):
        # O pulo do gato: isinstance(pagamento, Pagamento) retorna True 
        # para PagamentoPix, PagamentoCedula e PagamentoCartao!
        if isinstance(pagamento, Pagamento) and pagamento.id:
            super().add(pagamento.id, pagamento)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)