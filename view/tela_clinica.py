import FreeSimpleGUI as sg

# Definindo o tema visual claro e limpo (estilo site de clínica)
sg.LOOK_AND_FEEL_TABLE['TemaClinica'] = {
    'BACKGROUND': '#F7F9F9',
    'TEXT': '#2C3E50',
    'INPUT': '#FFFFFF',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#E3EAEA',
    'BUTTON': ('#FFFFFF', '#009688'), # Branco com fundo Verde-Água
    'PROGRESS': ('#009688', '#FFFFFF'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

class Tela_Clinica:
    def __init__(self):
        sg.theme('TemaClinica')
        self.font_padrao = ("Helvetica", 11)
        self.font_titulo = ("Helvetica", 14, "bold")

    def tela_opcoes(self):
        # Opções do Menu Clínica: 1 - Incluir, 2 - Alterar, 3 - Listar, 4 - Excluir, 0 - Retornar[cite: 1]
        layout = [
            [sg.Text("--- MENU CLÍNICA ---", font=self.font_titulo, justification='center', expand_x=True)],
            [sg.Button("1 - Incluir Clínica", key=1, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("2 - Alterar Clínica", key=2, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("3 - Listar Clínicas", key=3, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("4 - Excluir Clínica", key=4, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("0 - Retornar", key=0, border_width=0, font=self.font_padrao, expand_x=True)]
        ]

        window = sg.Window("Sistema - Clínica", layout, size=(300, 250), element_justification='c')
        event, values = window.read()
        window.close()

        if event == sg.WIN_CLOSED:
            return -1 # Retorno de erro no caso de fechar a janela[cite: 1]
        
        return event

    def pega_dados_clinica(self):
        # Campos capturados: Nome, Cidade, Descrição, Horário de Abertura e Fechamento[cite: 1]
        layout = [
            [sg.Text("--- DADOS DA CLÍNICA ---", font=self.font_titulo)],
            [sg.Text("Nome:", size=(20, 1)), sg.InputText(key='nome')],
            [sg.Text("Cidade:", size=(20, 1)), sg.InputText(key='cidade')],
            [sg.Text("Descrição:", size=(20, 1)), sg.InputText(key='descricao')],
            [sg.Text("Horário de Abertura (ex: 08:00):", size=(20, 1)), sg.InputText(key='horario_abertura')],
            [sg.Text("Horário de Fechamento (ex: 18:00):", size=(20, 1)), sg.InputText(key='horario_fechamento')],
            [sg.Button("Confirmar", border_width=0, pad=(10, 20)), sg.Button("Cancelar", border_width=0, button_color=('white', '#E74C3C'))]
        ]

        window = sg.Window("Cadastro de Clínica", layout, font=self.font_padrao)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, "Cancelar"):
            return None
        
        return values

    def mostra_clinica(self, clinicas):
        texto = ""
        for clinica in clinicas:
            # Exibição de Nome, Cidade, Horários e Descrição formatados[cite: 1]
            texto += f"Nome: {clinica.nome} | Cidade: {clinica.cidade}\n"
            texto += f"Horário: {clinica.horario_abertura} às {clinica.horario_fechamento}\n"
            texto += f"Descrição: {clinica.descricao}\n"
            texto += "-" * 40 + "\n"

        sg.popup_scrolled(texto, title="--- LISTA DE CLÍNICAS ---", size=(50, 15), font=self.font_padrao)

    def seleciona_clinica(self):
        # Captura o NOME da clínica para seleção[cite: 1]
        nome = sg.popup_get_text("Digite o NOME da clínica que deseja selecionar:", title="Selecionar Clínica", font=self.font_padrao)
        return nome

    def mostra_mensagem(self, msg):
        # Padrão de mensagens do sistema[cite: 1]
        sg.popup(msg, title="Aviso do Sistema", font=self.font_padrao)