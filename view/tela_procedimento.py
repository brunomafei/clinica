import FreeSimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['TemaClinica'] = {
    'BACKGROUND': '#F7F9F9', 'TEXT': '#2C3E50', 'INPUT': '#FFFFFF', 'TEXT_INPUT': '#000000',
    'SCROLL': '#E3EAEA', 'BUTTON': ('#FFFFFF', '#009688'), 'PROGRESS': ('#009688', '#FFFFFF'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0
}

class TelaProcedimento:
    def __init__(self):
        sg.theme('TemaClinica')
        self.font_padrao = ("Helvetica", 11)
        self.font_titulo = ("Helvetica", 14, "bold")

    def tela_opcoes(self):
        # Opções do menu: 1. Incluir, 2. Listar, 3. Alterar, 4. Excluir, 0. Voltar[cite: 8]
        layout = [
            [sg.Text("--- PROCEDIMENTOS ---", font=self.font_titulo, justification='center', expand_x=True)],
            [sg.Button("1. Incluir Procedimento", key=1, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("2. Listar Procedimentos", key=2, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("3. Alterar Procedimento", key=3, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("4. Excluir Procedimento", key=4, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("0. Voltar", key=0, border_width=0, font=self.font_padrao, expand_x=True)]
        ]
        window = sg.Window("Sistema - Procedimentos", layout, size=(300, 250), element_justification='c')
        event, _ = window.read()
        window.close()
        
        # Retorna -1 se o usuário fechar a janela, simulando erro de valor inválido[cite: 8]
        if event == sg.WIN_CLOSED: return -1 
        return event

    def pega_dados_procedimento(self):
        layout = [
            [sg.Text("--- Cadastro de Procedimento ---", font=self.font_titulo)],
            [sg.Text("Descrição:", size=(20, 1)), sg.InputText(key='descricao')],
            [sg.Text("Custo:", size=(20, 1)), sg.InputText(key='custo')],
            [sg.Text("Profissional responsável:", size=(20, 1)), sg.InputText(key='profissional_responsavel')],
            [sg.Text("ID do procedimento:", size=(20, 1)), sg.InputText(key='id_procedimento')],
            [sg.Button("Confirmar", border_width=0, pad=(10, 20)), sg.Button("Cancelar", border_width=0, button_color=('white', '#E74C3C'))]
        ]
        window = sg.Window("Cadastro de Procedimento", layout, font=self.font_padrao)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, "Cancelar"):
            return None

        # Validação de conversão de dados conforme a regra original[cite: 8]
        try:
            custo = float(values['custo'])
        except ValueError:
            self.mostra_mensagem("Erro: Custo deve ser numérico!")
            return None

        # Tenta converter o ID para int, se falhar, mantém como string[cite: 8]
        try:
            id_proc = int(values['id_procedimento'])
        except ValueError:
            id_proc = values['id_procedimento']

        return {
            "descricao": values['descricao'],
            "custo": custo,
            "profissional_responsavel": values['profissional_responsavel'],
            "id_procedimento": id_proc
        }

    def mostra_procedimentos(self, procedimentos):
        texto = ""
        for p in procedimentos:
            prof = p.profissional_responsavel
            nome_prof = getattr(prof, 'nome', prof)
            # Mostra ID, Descrição, Custo e Profissional[cite: 8]
            texto += f"ID: {p.id_procedimento} | Descrição: {p.descricao} | Custo: {p.custo} | Profissional Responsável: {nome_prof}\n"
            texto += "-" * 40 + "\n"
        sg.popup_scrolled(texto, title="--- Lista de Procedimentos ---", size=(60, 15), font=self.font_padrao)

    def seleciona_procedimento(self):
        id_str = sg.popup_get_text("Digite o ID do procedimento:", title="Selecionar", font=self.font_padrao)
        if not id_str: return None
        # Tenta converter para int, mantendo string caso falhe[cite: 8]
        try:
            return int(id_str)
        except ValueError:
            return id_str

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem, title="Aviso", font=self.font_padrao)