import FreeSimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['TemaClinica'] = {
    'BACKGROUND': '#F7F9F9', 'TEXT': '#2C3E50', 'INPUT': '#FFFFFF', 'TEXT_INPUT': '#000000',
    'SCROLL': '#E3EAEA', 'BUTTON': ('#FFFFFF', '#009688'), 'PROGRESS': ('#009688', '#FFFFFF'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0
}

class TelaRelatorio:
    def __init__(self):
        sg.theme('TemaClinica')
        self.font_padrao = ("Helvetica", 11)
        self.font_titulo = ("Helvetica", 14, "bold")

    def tela_opcoes(self):
        layout = [
            [sg.Text("--- RELATÓRIOS ---", font=self.font_titulo, justification='center', expand_x=True)],
            [sg.Button("1. Clínicas com mais atendimentos", key=1, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("2. Atendimentos mais caros e baratos", key=2, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("3. Procedimentos mais realizados", key=3, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("4. Procedimentos mais caros e baratos", key=4, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("0. Voltar", key=0, border_width=0, font=self.font_padrao, expand_x=True)]
        ]
        window = sg.Window("Sistema - Relatórios", layout, size=(350, 250), element_justification='c')
        event, _ = window.read()
        window.close()
        
        if event == sg.WIN_CLOSED: return -1
        return event

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem, title="Aviso", font=self.font_padrao)

    def mostra_relatorio_clinicas_mais_atendimentos(self, relatorio):
        if not relatorio:
            self.mostra_mensagem("Nenhum dado encontrado para este relatório.")
            return
        
        texto = ""
        for nome, quantidade in relatorio:
            texto += f"Clínica: {nome} | Atendimentos: {quantidade}\n"
        sg.popup_scrolled(texto, title="Clínicas com mais atendimentos", size=(40, 10), font=self.font_padrao)

    def mostra_relatorio_atendimentos_mais_caros_eh_baratos(self, mais_caro, mais_barato):
        # ATUALIZAÇÃO: Puxando o "custo_total" para o relatório refletir a realidade
        texto = f"Mais caro: Clínica {mais_caro.clinica.nome} | Custo Total: R$ {mais_caro.custo_total:.2f}\n\n"
        texto += f"Mais barato: Clínica {mais_barato.clinica.nome} | Custo Total: R$ {mais_barato.custo_total:.2f}"
        sg.popup(texto, title="Atendimentos mais caros e mais baratos", font=self.font_padrao)

    def mostra_relatorio_procedimentos_mais_realizados(self, relatorio):
        if not relatorio:
            self.mostra_mensagem("Nenhum dado encontrado para este relatório.")
            return
        
        texto = ""
        for descricao, quantidade in relatorio:
            texto += f"Procedimento: {descricao} | Quantidade: {quantidade}\n"
        sg.popup_scrolled(texto, title="Procedimentos mais realizados", size=(40, 10), font=self.font_padrao)

    def mostra_relatorio_procedimentos_mais_caros_eh_baratos(self, mais_caro, mais_barato):
        texto = f"Mais caro: {mais_caro.descricao} | Custo: R$ {mais_caro.custo:.2f}\n\n"
        texto += f"Mais barato: {mais_barato.descricao} | Custo: R$ {mais_barato.custo:.2f}"
        sg.popup(texto, title="Procedimentos mais caros e mais baratos", font=self.font_padrao)