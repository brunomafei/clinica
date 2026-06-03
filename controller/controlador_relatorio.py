from exceptions import ElementoNaoEncontradoException


class ControladorRelatorio:
    def __init__(self, controlador_clinica, controlador_procedimento, controlador_atendimento):
        # instacia controladores
        self.__controlador_clinica = controlador_clinica
        self.__controlador_procedimento = controlador_procedimento
        self.__controlador_atendimento = controlador_atendimento

# Clínicas com maior número de atendimentos-------------------------------------------------------------------------------------------

    def relatorio_clinicas_mais_atendimentos(self):
            todas_clinicas = self.__controlador_clinica.listar_clinicas()
            atendimentos = self.__controlador_atendimento.listar_atendimentos()

            # Verifica se a lista está vazia
            if not todas_clinicas:
                raise ElementoNaoEncontradoException("Nenhuma clínica encontrada para gerar o relatório.")

            # Percorre todos os atendimentos e conta quantas vezes cada clínica aparece
            contagem_de_clinicas = {}
            for clinica in todas_clinicas:
                contagem_de_clinicas[clinica.nome] = 0  # Inicializa a contagem para cada clínica

            for atendimento in atendimentos:
                clinica = atendimento.clinica.nome
                if clinica in contagem_de_clinicas:
                    contagem_de_clinicas[clinica] += 1

            ordena_clinicas = sorted(contagem_de_clinicas.items(), key=lambda x: x[1], reverse=True)
            return ordena_clinicas

# Clínicas com atendimentos mais caros e baratos-------------------------------------------------------------------------------------------  

    def relatorio_atendimentos_mais_caros_eh_baratos(self):
        atendimentos = self.__ctrl_atendimento.listar_atendimentos()
        
        if not atendimentos:
            raise ElementoNaoEncontradoException("Nenhum atendimento encontrado para gerar o relatório.")

        # Ordena a lista de objetos Atendimento baseando-se no atributo valor
        atendimentos_ordenados = sorted(atendimentos, key=lambda a: a.valor)

        mais_barato = atendimentos_ordenados[0]  # O primeiro da lista ordenada
        mais_caro = atendimentos_ordenados[-1]   # O último da lista ordenada (-1 no Python pega o último item)

        return mais_caro, mais_barato
    
# Procedimentos mais realizados-------------------------------------------------------------------------------------------

    def relatorio_procedimentos_mais_realizados(self):
        procedimentos = self.__controlador_procedimento.listar_procedimentos()

        # Verifica se a lista está vazia
        if not procedimentos:
            raise ElementoNaoEncontradoException("Nenhum procedimento encontrado para gerar o relatório.")
        
        # Percorre todos os procedimentos e conta quantas vezes cada procedimento aparece
        contagem_de_procedimentos = {}
        for procedimento in procedimentos:
            descricao = procedimento.descricao
            if descricao in contagem_de_procedimentos:
                contagem_de_procedimentos[descricao] += 1
            else:
                contagem_de_procedimentos[descricao] = 1

        ordena_procedimentos = sorted(contagem_de_procedimentos.items(), key=lambda x: x[1], reverse=True)
        return ordena_procedimentos
    
# Procedimentos mais caros e baratos------------------------------------------------------------------------------------------- 

    def relatorio_procedimentos_mais_caros_eh_baratos(self):
        procedimentos = self.__controlador_procedimento.listar_procedimentos()
        
        if not procedimentos:
            raise ElementoNaoEncontradoException("Nenhum procedimento encontrado para gerar o relatório.")

        # Ordena a lista de objetos Procedimento baseando-se no atributo valor
        procedimentos_ordenados = sorted(procedimentos, key=lambda p: p.valor)

        mais_barato = procedimentos_ordenados[0]  # O primeiro da lista ordenada
        mais_caro = procedimentos_ordenados[-1]   # O último da lista ordenada (-1 no Python pega o último item)

        return mais_caro, mais_barato
 
