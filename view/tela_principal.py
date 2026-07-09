import FreeSimpleGUI as sg

class TelaPrincipal:
    # Tela principal da aplicação com interface gráfica simples.

    def __init__(self):
        # Define o tema visual da interface.
        try:
            sg.theme("DarkBlue3")
        except Exception:
            pass

    def tela_opcoes(self):
        # Exibe as opções principais do sistema para o usuário.
        # Passamos números inteiros no parâmetro 'key' para facilitar o retorno.
        layout = [
            [sg.Text("Clínica", font=("Helvetica", 20, "bold"))],
            [sg.Text("Escolha uma opção:", font=("Helvetica", 12))],
            [sg.Button("1. Atendimentos", key=1, size=(20, 1))],
            [sg.Button("2. Clínicas", key=2, size=(20, 1))],
            [sg.Button("3. Pagamentos", key=3, size=(20, 1))],
            [sg.Button("4. Pessoas", key=4, size=(20, 1))],
            [sg.Button("5. Procedimentos", key=5, size=(20, 1))],
            [sg.Button("6. Relatórios", key=6, size=(20, 1))],
            [sg.Button("0. Sair", key=0, size=(20, 1))],
        ]

        # Cria a janela e aguarda a escolha do usuário.
        window = sg.Window("Menu Principal", layout, modal=True, finalize=True)
        event, _ = window.read()
        window.close()

        # Se o usuário fechar a janela no 'X' (None ou WIN_CLOSED), 
        # devolvemos 0 para o controlador encerrar o sistema de forma limpa.
        if event in (None, sg.WIN_CLOSED):
            return 0

        # Como as 'keys' já são inteiros, podemos retornar o evento direto
        return event

    def mostra_mensagem(self, mensagem):
        # Mostra uma mensagem ao usuário em uma janela popup.
        try:
            sg.popup(mensagem, title="Mensagem")
        except Exception:
            print(mensagem)