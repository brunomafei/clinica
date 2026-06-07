from exceptions.elemento_nao_existe_exception import ElementoNaoExisteException
from view.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_clinica, controlador_procedimento, controlador_atendimento):
        self.__controlador_clinica = controlador_clinica
        self.__controlador_procedimento = controlador_procedimento
        self.__controlador_atendimento = controlador_atendimento
        self.__tela_relatorio = TelaRelatorio()

    def relatorio_clinicas_mais_atendimentos(self):
        todas_clinicas = self.__controlador_clinica.listar_clinicas()
        atendimentos = self.__controlador_atendimento.listar_atendimentos()

        if not todas_clinicas:
            raise ElementoNaoExisteException("Nenhuma clínica encontrada para gerar o relatório.")

        contagem_de_clinicas = {clinica.nome: 0 for clinica in todas_clinicas}

        for atendimento in atendimentos:
            nome_clinica = atendimento.clinica.nome
            if nome_clinica in contagem_de_clinicas:
                contagem_de_clinicas[nome_clinica] += 1

        ordena_clinicas = sorted(contagem_de_clinicas.items(), key=lambda x: x[1], reverse=True)
        return ordena_clinicas

    def relatorio_atendimentos_mais_caros_eh_baratos(self):
        atendimentos = self.__controlador_atendimento.listar_atendimentos()

        if not atendimentos:
            raise ElementoNaoExisteException("Nenhum atendimento encontrado para gerar o relatório.")

        atendimentos_ordenados = sorted(atendimentos, key=lambda a: a.valor_total)

        mais_barato = atendimentos_ordenados[0]
        mais_caro = atendimentos_ordenados[-1]

        return mais_caro, mais_barato

    def relatorio_procedimentos_mais_realizados(self):
        procedimentos = self.__controlador_procedimento.listar_procedimentos()

        if not procedimentos:
            raise ElementoNaoExisteException("Nenhum procedimento encontrado para gerar o relatório.")

        contagem_de_procedimentos = {}
        for procedimento in procedimentos:
            descricao = procedimento.descricao
            contagem_de_procedimentos[descricao] = contagem_de_procedimentos.get(descricao, 0) + 1

        ordena_procedimentos = sorted(contagem_de_procedimentos.items(), key=lambda x: x[1], reverse=True)
        return ordena_procedimentos

    def relatorio_procedimentos_mais_caros_eh_baratos(self):
        procedimentos = self.__controlador_procedimento.listar_procedimentos()

        if not procedimentos:
            raise ElementoNaoExisteException("Nenhum procedimento encontrado para gerar o relatório.")

        procedimentos_ordenados = sorted(procedimentos, key=lambda p: p.custo)

        mais_barato = procedimentos_ordenados[0]
        mais_caro = procedimentos_ordenados[-1]

        return mais_caro, mais_barato

    def retornar(self):
        return

    def abre_tela(self):
        opcoes_relatorio = {
            1: self.mostra_relatorio_clinicas_mais_atendimentos,
            2: self.mostra_relatorio_atendimentos_mais_caros_eh_baratos,
            3: self.mostra_relatorio_procedimentos_mais_realizados,
            4: self.mostra_relatorio_procedimentos_mais_caros_eh_baratos,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_relatorio.tela_opcoes()
            funcao_escolhida = opcoes_relatorio.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_relatorio.mostra_mensagem(" Opção inválida!")

            if opcao == 0:
                continua = False

    def mostra_relatorio_clinicas_mais_atendimentos(self):
        try:
            resultado = self.relatorio_clinicas_mais_atendimentos()
            self.__tela_relatorio.mostra_relatorio_clinicas_mais_atendimentos(resultado)
        except ElementoNaoExisteException as e:
            self.__tela_relatorio.mostra_mensagem(str(e))

    def mostra_relatorio_atendimentos_mais_caros_eh_baratos(self):
        try:
            mais_caro, mais_barato = self.relatorio_atendimentos_mais_caros_eh_baratos()
            self.__tela_relatorio.mostra_relatorio_atendimentos_mais_caros_eh_baratos(mais_caro, mais_barato)
        except ElementoNaoExisteException as e:
            self.__tela_relatorio.mostra_mensagem(str(e))

    def mostra_relatorio_procedimentos_mais_realizados(self):
        try:
            resultado = self.relatorio_procedimentos_mais_realizados()
            self.__tela_relatorio.mostra_relatorio_procedimentos_mais_realizados(resultado)
        except ElementoNaoExisteException as e:
            self.__tela_relatorio.mostra_mensagem(str(e))

    def mostra_relatorio_procedimentos_mais_caros_eh_baratos(self):
        try:
            mais_caro, mais_barato = self.relatorio_procedimentos_mais_caros_eh_baratos()
            self.__tela_relatorio.mostra_relatorio_procedimentos_mais_caros_eh_baratos(mais_caro, mais_barato)
        except ElementoNaoExisteException as e:
            self.__tela_relatorio.mostra_mensagem(str(e))

