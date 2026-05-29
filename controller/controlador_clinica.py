from model.clinica import Clinica


class ControladorClinica:
    def __init__(self):
        # Essa é a nossa "gaveta" principal. Toda clínica cadastrada vai parar nessa lista.
        self.__clinicas = []

    def incluir_clinica(self, nome, cidade, descricao, horario_abertura, horario_fechamento):
        try:
            # Tenta criar a clínica. Se algum dado for inválido (como nome vazio),
            # o Model vai gritar um ValueError e cair no except lá embaixo.
            nova_clinica = Clinica(
                nome, cidade, descricao, horario_abertura, horario_fechamento)
            self.__clinicas.append(nova_clinica)
            return nova_clinica
        except ValueError as e:
            # Tratamento de exceção! Avisamos o que deu errado.
            print(f"Ops, erro ao cadastrar a clínica: {e}")
            return None

    def listar_clinicas(self):
        # Só devolve a lista para a Tela poder iterar e mostrar pro usuário.
        return self.__clinicas

    def alterar_clinica(self, clinica, novo_nome, nova_cidade, nova_descricao, novo_abertura, novo_fechamento):
        try:
            # Usamos os setters que você criou. Eles vão garantir que a regra
            # do "nome inválido" continue funcionando mesmo na alteração.
            clinica.nome = novo_nome
            clinica.cidade = nova_cidade
            clinica.descricao = nova_descricao
            clinica.horario_abertura = novo_abertura
            clinica.horario_fechamento = novo_fechamento
            return True
        except ValueError as e:
            print(f"Não foi possível alterar a clínica: {e}")
            return False

    def excluir_clinica(self, clinica):
        # Checa se ela existe na lista antes de tentar remover
        if clinica in self.__clinicas:
            self.__clinicas.remove(clinica)
            return True
        return False
