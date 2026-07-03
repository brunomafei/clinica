import FreeSimpleGUI as sg
from model.pessoa import Paciente, Profissional


class TelaPessoa:
    # Tela para cadastro, alteração e consulta de pessoas.

    def __init__(self):
        # Define o tema visual da interface.
        try:
            sg.theme("DarkBlue3")
        except Exception:
            pass

    def tela_opcoes(self):
        # Exibe as opções de gerenciamento de pessoas.
        # Esse menu direciona o fluxo para cadastro, alteração, listagem ou remoção.
        layout = [
            [sg.Text("Pessoas", font=("Helvetica", 18, "bold"))],
            [sg.Button("1 - Cadastrar paciente", key="1", size=(24, 1))],
            [sg.Button("2 - Cadastrar profissional", key="2", size=(24, 1))],
            [sg.Button("3 - Alterar pessoa", key="3", size=(24, 1))],
            [sg.Button("4 - Listar pessoas", key="4", size=(24, 1))],
            [sg.Button("5 - Remover pessoa", key="5", size=(24, 1))],
            [sg.Button("0 - Voltar", key="0", size=(24, 1))],
        ]

        # Cria a janela de opções e espera a ação escolhida pelo usuário.
        window = sg.Window("Gerenciar Pessoas", layout, modal=True, finalize=True)
        event, _ = window.read()
        window.close()

        # Retorna -1 caso a janela seja fechada sem escolha.
        if event in (None, ""):
            return -1
        return int(event)

    def pega_dados_paciente(self):
        # Coleta os dados de cadastro de um paciente.
        # Os valores são retornados em uma estrutura simples para o controlador.
        layout = [
            [sg.Text("Cadastro de Paciente", font=("Helvetica", 16, "bold"))],
            [sg.Text("Nome"), sg.Input(key="nome")],
            [sg.Text("Idade"), sg.Input(key="idade")],
            [sg.Text("Celular"), sg.Input(key="celular")],
            [sg.Text("CPF"), sg.Input(key="cpf")],
            [sg.Button("Salvar", key="salvar"), sg.Button("Cancelar", key="cancelar")],
        ]

        while True:
            window = sg.Window("Cadastro de Paciente", layout, modal=True, finalize=True)
            event, values = window.read()
            window.close()

            # Se o usuário cancelar, interrompe o cadastro.
            if event in (None, "cancelar"):
                return None

            # Se salvar, valida a idade e retorna os dados digitados.
            if event == "salvar":
                try:
                    idade = int(values["idade"])
                    return values["nome"], idade, values["celular"], values["cpf"]
                except ValueError:
                    self.mostra_mensagem("Digite uma idade válida.")

    def pega_dados_profissional(self):
        # Coleta os dados de cadastro de um profissional.
        # Os campos são reunidos em uma tupla para uso posterior.
        layout = [
            [sg.Text("Cadastro de Profissional", font=("Helvetica", 16, "bold"))],
            [sg.Text("Nome"), sg.Input(key="nome")],
            [sg.Text("Celular"), sg.Input(key="celular")],
            [sg.Text("CPF"), sg.Input(key="cpf")],
            [sg.Text("Especialidade"), sg.Input(key="especialidade")],
            [sg.Text("Registro"), sg.Input(key="registro")],
            [sg.Button("Salvar", key="salvar"), sg.Button("Cancelar", key="cancelar")],
        ]

        window = sg.Window("Cadastro de Profissional", layout, modal=True, finalize=True)
        event, values = window.read()
        window.close()

        # Se o usuário cancelar, retorna None para encerrar o fluxo.
        if event in (None, "cancelar"):
            return None

        # Retorna os dados coletados em ordem esperada pelo controlador.
        return values["nome"], values["celular"], values["cpf"], values["especialidade"], values["registro"]

    def seleciona_cpf(self):
        # Solicita o CPF de uma pessoa para alteração ou remoção.
        layout = [
            [sg.Text("CPF da pessoa")],
            [sg.Input(key="cpf")],
            [sg.Button("OK"), sg.Button("Cancelar")],
        ]

        window = sg.Window("Selecionar CPF", layout, modal=True, finalize=True)
        event, values = window.read()
        window.close()

        if event in (None, "Cancelar"):
            return None
        return values["cpf"]

    def mostra_pessoas(self, pessoas):
        # Exibe a lista de pessoas cadastradas em uma janela rolável.
        # Útil para mostrar todos os cadastros de forma organizada.
        if not pessoas:
            self.mostra_mensagem("Nenhuma pessoa cadastrada.")
            return

        texto = []
        for pessoa in pessoas:
            texto.append(self.mostra_pessoa(pessoa))
            texto.append("-" * 30)

        sg.popup_scrolled("\n".join(texto), title="Pessoas cadastradas", size=(80, 20))

    def mostra_pessoa(self, pessoa):
        # Formata os dados de uma pessoa para apresentação na tela.
        # Diferencia paciente e profissional conforme o tipo da instância.
        tipo = "Paciente" if isinstance(pessoa, Paciente) else "Profissional"
        linhas = [
            f"Tipo: {tipo}",
            f"Nome: {pessoa.nome}",
            f"Celular: {pessoa.celular}",
            f"CPF: {pessoa.cpf}",
        ]

        if isinstance(pessoa, Paciente):
            linhas.append(f"Idade: {pessoa.idade}")
        elif isinstance(pessoa, Profissional):
            linhas.append(f"Especialidade: {pessoa.especialidade}")
            linhas.append(f"Registro: {pessoa.registro}")

        return "\n".join(linhas)

    def mostra_mensagem(self, msg):
        # Exibe uma mensagem de aviso ou confirmação ao usuário.
        # Serve como feedback visual para operações realizadas.
        try:
            sg.popup(msg, title="Mensagem")
        except Exception:
            print(msg)
