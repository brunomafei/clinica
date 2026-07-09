import FreeSimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['TemaClinica'] = {
    'BACKGROUND': '#F7F9F9', 'TEXT': '#2C3E50', 'INPUT': '#FFFFFF', 'TEXT_INPUT': '#000000',
    'SCROLL': '#E3EAEA', 'BUTTON': ('#FFFFFF', '#009688'), 'PROGRESS': ('#009688', '#FFFFFF'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0
}

class Tela_Clinica:
    def __init__(self):
        sg.theme('TemaClinica')
        self.font_padrao = ("Helvetica", 11)
        self.font_titulo = ("Helvetica", 14, "bold")

    def tela_opcoes(self):
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
            return -1 
        
        return event

    def pega_dados_clinica(self):
        layout = [
            [sg.Text("--- DADOS DA CLÍNICA ---", font=self.font_titulo)],
            [sg.Text("Nome:", size=(20, 1)), sg.InputText(key='nome')],
            [sg.Text("CNPJ:", size=(20, 1)), sg.InputText(key='cnpj')],
            [sg.Text("Cidade:", size=(20, 1)), sg.InputText(key='cidade')],
            [sg.Text("Descrição:", size=(20, 1)), sg.InputText(key='descricao')],
            [sg.Text("Abertura (ex: 08:00):", size=(20, 1)), sg.InputText(key='horario_abertura')],
            [sg.Text("Fechamento (ex: 18:00):", size=(20, 1)), sg.InputText(key='horario_fechamento')],
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
            texto += f"Nome: {clinica.nome} | CNPJ: {clinica.cnpj}\n"
            texto += f"Cidade: {clinica.cidade}\n"
            texto += f"Horário: {clinica.horario_abertura} às {clinica.horario_fechamento}\n"
            texto += f"Descrição: {clinica.descricao}\n"
            texto += "-" * 40 + "\n"

        sg.popup_scrolled(texto, title="--- LISTA DE CLÍNICAS ---", size=(50, 15), font=self.font_padrao)

    def seleciona_clinica(self):
        # Agora solicitamos o CNPJ para ser mais exato na seleção
        cnpj = sg.popup_get_text("Digite o CNPJ da clínica que deseja selecionar:", title="Selecionar Clínica", font=self.font_padrao)
        return cnpj

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Aviso do Sistema", font=self.font_padrao)