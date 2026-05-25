from controlador_pagamento import Pagamento_pix, Pagamento_cartao, Pagamento_cedula


class ControladorPagamento:
    def __init__(self):
        # Aqui guardamos todos os recibos (pagamentos) do sistema inteiro
        self.__pagamentos = []

    def incluir_pagamento(self, atendimento, tipo, data, valor, **kwargs):
        try:
            novo_pagamento = None

            # Decide qual "filho" de Pagamento criar com base no tipo escolhido na tela
            if tipo.upper() == "PIX":
                chave = kwargs.get("chave_pix")
                novo_pagamento = Pagamento_pix(data, valor, chave, atendimento)

            elif tipo.upper() == "CARTAO":
                numero = kwargs.get("numero_cartao")
                bandeira = kwargs.get("bandeira")
                novo_pagamento = Pagamento_cartao(
                    data, valor, numero, bandeira, atendimento)

            elif tipo.upper() == "CEDULA":
                novo_pagamento = Pagamento_cedula(data, valor, atendimento)

            else:
                # Se digitar um tipo maluco que não existe...
                raise ValueError(
                    "Tipo de pagamento inválido! Escolha PIX, Cartão ou Cédula.")

            self.__pagamentos.append(novo_pagamento)
            return novo_pagamento

        except ValueError as e:
            # Pega erros como "data do pagamento maior que a consulta" que fizemos no Model
            print(f"Erro ao processar pagamento: {e}")
            return None

    def listar_pagamentos(self):
        return self.__pagamentos

    def alterar_pagamento(self, pagamento, nova_data, novo_valor):
        try:
            # Na vida real a gente não costuma alterar recibo, mas como o CRUD
            # exige alteração para os Registros, a gente implementa!
            pagamento.data = nova_data
            pagamento.valor_pago = novo_valor
            return True
        except ValueError as e:
            print(f"Erro ao alterar o pagamento: {e}")
            return False

    def excluir_pagamento(self, pagamento):
        if pagamento in self.__pagamentos:
            self.__pagamentos.remove(pagamento)
            return True
        return False
