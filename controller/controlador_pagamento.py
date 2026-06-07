from model.pagamento import Pagamento_pix, Pagamento_cartao, Pagamento_cedula
from view.tela_pagamento import Tela_Pagamento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException


class ControladorPagamento:
    def __init__(self, controlador_atendimento):
        self.__pagamentos = []
        self.__tela_pagamento = Tela_Pagamento()
        self.__controlador_atendimento = controlador_atendimento

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pagamento,
            2: self.listar_pagamentos
        }

        while True:
            opcao = self.__tela_pagamento.tela_opcoes()
            if opcao == 0:
                break

            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__tela_pagamento.mostra_mensagem("Opção inválida!")

    def incluir_pagamento(self):
        dados = self.__tela_pagamento.pega_dados_pagamento()

        if dados is not None:
            try:
                atendimento = self.__controlador_atendimento.buscar_atendimento_por_id(
                    dados["id_atendimento"])

                if atendimento is None:
                    raise ElementoNaoExisteException(
                        "Atendimento não encontrado.")

                novo_pagamento = None
                tipo = dados["tipo"]

                if tipo == "PIX":
                    novo_pagamento = Pagamento_pix(
                        dados["data"], dados["valor"], dados["chave_pix"], atendimento)
                elif tipo == "CARTAO":
                    novo_pagamento = Pagamento_cartao(
                        dados["data"], dados["valor"], dados["numero_cartao"], dados["bandeira"], atendimento)
                elif tipo == "CEDULA":
                    novo_pagamento = Pagamento_cedula(
                        dados["data"], dados["valor"], atendimento)
                else:
                    raise ValueError("Tipo inválido.")

                self.__pagamentos.append(novo_pagamento)
                atendimento.valor_total -= dados["valor"]
                self.__tela_pagamento.mostra_mensagem(
                    f"Pago! Valor restante: R${atendimento.valor_total:.2f}")

            except Exception as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")

    def listar_pagamentos(self):
        if len(self.__pagamentos) == 0:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento.")
        else:
            self.__tela_pagamento.mostra_pagamentos(self.__pagamentos)
