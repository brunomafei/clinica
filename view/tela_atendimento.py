import FreeSimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['TemaClinica'] = {
    'BACKGROUND': '#F7F9F9', 'TEXT': '#2C3E50', 'INPUT': '#FFFFFF', 'TEXT_INPUT': '#000000',
    'SCROLL': '#E3EAEA', 'BUTTON': ('#FFFFFF', '#009688'), 'PROGRESS': ('#009688', '#FFFFFF'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0
}

class Tela_Atendimento:
    def __init__(self):
        sg.theme('TemaClinica')
        self.font_padrao = ("Helvetica", 11)
        self.font_titulo = ("Helvetica", 14, "bold")

    def tela_opcoes(self):
        layout = [
            [sg.Text("--- MENU ATENDIMENTO ---", font=self.font_titulo, justification='center', expand_x=True)],
            [sg.Button("1 - Agendar Atendimento", key=1, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("2 - Alterar Atendimento", key=2, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("3 - Listar Atendimentos", key=3, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("4 - Cancelar/Excluir Atendimento", key=4, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("5 - Registrar Procedimento no Atendimento", key=5, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("0 - Retornar", key=0, border_width=0, font=self.font_padrao, expand_x=True)]
        ]
        window = sg.Window("Sistema - Atendimentos", layout, size=(300, 280), element_justification='c')
        event, _ = window.read()
        window.close()
        
        if event == sg.WIN_CLOSED: return -1
        return event

    def pega_dados_atendimento(self):
        layout = [
            [sg.Text("--- DADOS DO AGENDAMENTO ---", font=self.font_titulo)],
            [sg.Text("CPF do Paciente:", size=(20, 1)), sg.InputText(key='cpf_paciente')],
            [sg.Text("Nome da Clínica:", size=(20, 1)), sg.InputText(key='nome_clinica')],
            [sg.Text("Registro do Profissional:", size=(20, 1)), sg.InputText(key='registro_profissional')],
            [sg.Text("Data (DD/MM/AAAA):", size=(20, 1)), sg.InputText(key='data')],
            [sg.Text("Hora de Início:", size=(20, 1)), sg.InputText(key='hora_inicio')],
            [sg.Text("Hora de Fim:", size=(20, 1)), sg.InputText(key='hora_fim')],
            [sg.Text("Tipo (Consulta, Exame...):", size=(20, 1)), sg.InputText(key='tipo')],
            [sg.Text("Valor Base: R$", size=(20, 1)), sg.InputText(key='valor_total')],
            [sg.Button("Confirmar", border_width=0, pad=(10, 20)), sg.Button("Cancelar", border_width=0, button_color=('white', '#E74C3C'))]
        ]
        window = sg.Window("Agendar Atendimento", layout, font=self.font_padrao)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, "Cancelar"): return None

        try:
            valor = float(values['valor_total'])
        except ValueError:
            self.mostra_mensagem("Erro: Valor deve ser numérico! Tente novamente.")
            return None

        return {
            "cpf_paciente": values['cpf_paciente'],
            "nome_clinica": values['nome_clinica'],
            "registro_profissional": values['registro_profissional'],
            "data": values['data'],
            "hora_inicio": values['hora_inicio'],
            "hora_fim": values['hora_fim'],
            "tipo": values['tipo'],
            "valor_total": valor
        }

    def mostra_atendimento(self, atendimentos):
        texto = ""
        for a in atendimentos:
            texto += f"ID: {a.id} | Data: {a.data} | Horário: {a.horario_inicio} às {a.horario_fim}\n"
            
            # Aqui eu mudo para mostrar as informações financeiras de forma transparente para o usuário
            texto += f"Tipo: {a.tipo} | Custo Total: R$ {a.custo_total:.2f} | Falta Pagar: R$ {a.valor_restante:.2f}\n"
            
            if a.procedimentos:
                texto += "Procedimentos Realizados:\n"
                for proc in a.procedimentos:
                    texto += f"  -> {proc.descricao} (Custo Adicional: R$ {proc.custo:.2f})\n"
            else:
                texto += "Procedimentos Realizados: Nenhum\n"
            
            texto += "-" * 50 + "\n"
            
        sg.popup_scrolled(texto, title="--- Lista de Atendimentos ---", size=(60, 15), font=self.font_padrao)

    def seleciona_atendimento(self):
        return sg.popup_get_text("Digite o ID do atendimento que deseja selecionar:", title="Selecionar", font=self.font_padrao)

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Aviso", font=self.font_padrao)