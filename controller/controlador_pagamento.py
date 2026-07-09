from datetime import datetime
from model.pagamento import PagamentoPix, PagamentoCartao, PagamentoCedula
from view.tela_pagamento import Tela_Pagamento
from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from daos.pagamento_dao import PagamentoDAO


class ControladorPagamento:
    def __init__(self, controlador_atendimento):
        self.__pagamentos_dao = PagamentoDAO()
        self.__tela_pagamento = Tela_Pagamento()
        self.__controlador_atendimento = controlador_atendimento

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pagamento,
            2: self.listar_pagamentos
        }

        while True:
            opcao = self.__tela_pagamento.tela_opcoes()
            if opcao in (0, -1):
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

                # REQUISITO 3: Validação da data de pagamento
                try:
                    data_pagamento = datetime.strptime(dados["data"], "%d/%m/%Y")
                    data_atendimento = datetime.strptime(atendimento.data, "%d/%m/%Y")
                    
                    if data_pagamento > data_atendimento:
                        raise ValueError("O pagamento deve ser realizado até a data do atendimento.")
                except ValueError as ve:
                    raise ValueError(f"Erro de data: {ve}. Certifique-se de usar o formato DD/MM/AAAA.")

                # REQUISITO: Não deixar pagar mais do que o saldo devedor
                if dados["valor"] > atendimento.valor_restante:
                    raise ValueError(f"O valor do pagamento (R$ {dados['valor']:.2f}) não pode ser maior que o saldo devedor (R$ {atendimento.valor_restante:.2f}).")

                novo_pagamento = None
                tipo = dados["tipo"]

                if tipo == "PIX":
                    novo_pagamento = PagamentoPix(
                        dados["data"], dados["valor"], dados["chave_pix"], atendimento)
                elif tipo == "CARTAO":
                    novo_pagamento = PagamentoCartao(
                        dados["data"], dados["valor"], dados["numero_cartao"], dados["bandeira"], atendimento)
                elif tipo == "CEDULA":
                    novo_pagamento = PagamentoCedula(
                        dados["data"], dados["valor"], atendimento)
                else:
                    raise ValueError("Tipo inválido.")

                self.__pagamentos_dao.add(novo_pagamento)
                
                # A MÁGICA ACONTECE AQUI: Somamos no valor_pago em vez de subtrair do valor_total
                atendimento.valor_pago += dados["valor"]
                
                self.__controlador_atendimento._ControladorAtendimento__atendimentos_dao.add(atendimento)
                
                self.__tela_pagamento.mostra_mensagem(
                    f"Pago! Saldo devedor restante: R$ {atendimento.valor_restante:.2f}")

            except Exception as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")

    def listar_pagamentos(self):
        pagamentos = list(self.__pagamentos_dao.get_all())
        if len(pagamentos) == 0:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento.")
        else:
            self.__tela_pagamento.mostra_pagamentos(pagamentos)