import FreeSimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['TemaClinica'] = {
    'BACKGROUND': '#F7F9F9',
    'TEXT': '#2C3E50',
    'INPUT': '#FFFFFF',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#E3EAEA',
    'BUTTON': ('#FFFFFF', '#009688'),
    'PROGRESS': ('#009688', '#FFFFFF'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

class Tela_Pagamento:
    def __init__(self):
        sg.theme('TemaClinica')
        self.font_padrao = ("Helvetica", 11)
        self.font_titulo = ("Helvetica", 14, "bold")

    def tela_opcoes(self):
        # Opções do Menu Pagamento: 1 - Registrar, 2 - Listar, 0 - Retornar[cite: 2]
        layout = [
            [sg.Text("--- MENU PAGAMENTO ---", font=self.font_titulo, justification='center', expand_x=True)],
            [sg.Button("1 - Registrar Pagamento", key=1, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("2 - Listar Pagamentos", key=2, border_width=0, font=self.font_padrao, expand_x=True)],
            [sg.Button("0 - Retornar", key=0, border_width=0, font=self.font_padrao, expand_x=True)]
        ]

        window = sg.Window("Sistema - Pagamentos", layout, size=(300, 200), element_justification='c')
        event, values = window.read()
        window.close()

        if event == sg.WIN_CLOSED:
            return -1 # Retorno de erro no caso de fechar a janela[cite: 2]
        
        return event

    def pega_dados_pagamento(self):
        # Janela principal para ID, Data, Valor e seleção de Tipo[cite: 2]
        tipos_disponiveis = ['PIX', 'CARTAO', 'CEDULA']
        
        layout = [
            [sg.Text("--- DADOS DO PAGAMENTO ---", font=self.font_titulo)],
            [sg.Text("ID ou Data do Atendimento:", size=(22, 1)), sg.InputText(key='id_atendimento')],
            [sg.Text("Data (DD/MM/AAAA):", size=(22, 1)), sg.InputText(key='data')],
            [sg.Text("Valor a ser pago: R$", size=(22, 1)), sg.InputText(key='valor')],
            [sg.Text("Modalidade:", size=(22, 1)), sg.Combo(tipos_disponiveis, key='tipo', readonly=True, size=(20, 1))],
            [sg.Button("Continuar", border_width=0, pad=(10, 20)), sg.Button("Cancelar", border_width=0, button_color=('white', '#E74C3C'))]
        ]

        window = sg.Window("Registrar Pagamento", layout, font=self.font_padrao)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, "Cancelar"):
            return None

        # Validação do valor numérico exigida pela regra original[cite: 2]
        try:
            valor_float = float(values['valor'])
        except ValueError:
            self.mostra_mensagem("Erro: Valor deve ser numérico!")
            return None

        dados = {
            "id_atendimento": values['id_atendimento'],
            "data": values['data'],
            "valor": valor_float,
            "tipo": values['tipo']
        }

        # Fluxos condicionais dependendo do tipo selecionado[cite: 2]
        if dados["tipo"] == "PIX":
            chave = sg.popup_get_text("Digite a chave PIX:", title="Dados PIX", font=self.font_padrao)
            if chave is None: return None
            dados["chave_pix"] = chave
            
        elif dados["tipo"] == "CARTAO":
            layout_cartao = [
                [sg.Text("Digite o número do cartão:"), sg.InputText(key='numero_cartao')],
                [sg.Text("Digite a bandeira (ex: Visa, Mastercard):"), sg.InputText(key='bandeira')],
                [sg.Button("Confirmar", border_width=0), sg.Button("Cancelar", border_width=0, button_color=('white', '#E74C3C'))]
            ]
            win_cartao = sg.Window("Dados do Cartão", layout_cartao, font=self.font_padrao)
            ev_cartao, val_cartao = win_cartao.read()
            win_cartao.close()
            
            if ev_cartao in (sg.WIN_CLOSED, "Cancelar"):
                return None
                
            dados["numero_cartao"] = val_cartao["numero_cartao"]
            dados["bandeira"] = val_cartao["bandeira"]

        return dados

    def mostra_pagamentos(self, pagamentos):
        texto = ""
        for p in pagamentos:
            # Exibe Data e Valor Pago[cite: 2]
            texto += f"Data: {p.data} | Valor Pago: R$ {p.valor_pago:.2f}\n"

            # Identifica os atributos específicos (hasattr) para detalhar a modalidade de pagamento[cite: 2]
            if hasattr(p, 'chave_pix'):
                texto += f"Modalidade: PIX | Chave: {p.chave_pix}\n"
            elif hasattr(p, 'numero_cartao'):
                texto += f"Modalidade: Cartão de Crédito | Bandeira: {p.bandeira}\n"
            else:
                texto += "Modalidade: Cédula (Dinheiro em espécie)\n"
            
            texto += "-" * 40 + "\n"

        sg.popup_scrolled(texto, title="--- HISTÓRICO DE PAGAMENTOS ---", size=(50, 15), font=self.font_padrao)

    def seleciona_pagamento(self):
        # Captura a Data ou ID do pagamento para seleção[cite: 2]
        codigo = sg.popup_get_text("Digite a Data (ou ID) do pagamento que deseja selecionar:", title="Selecionar Pagamento", font=self.font_padrao)
        return codigo

    def mostra_mensagem(self, msg):
        # Padrão de mensagens do sistema[cite: 2]
        sg.popup(msg, title="Aviso do Sistema", font=self.font_padrao)