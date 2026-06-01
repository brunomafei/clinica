from controlador_atendimento import ControladorAtendimento
from controlador_clinica import ControladorClinica
from controlador_pagamento import ControladorPagamento
from controlador_pessoa import ControladorPessoa
from controlador_procedimento import ControladorProcedimento
from controlador_relatorio import ControladorRelatorio

class ControladorPrincipal:
    def __init__(self):
        self.controlador_pessoa = ControladorPessoa()
        self.controlador_clinica = ControladorClinica()
        self.controlador_atendimento = ControladorAtendimento(self.controlador_pessoa, self.controlador_clinica)
        self.controlador_pagamento = ControladorPagamento()
        self.controlador_procedimento = ControladorProcedimento()
        self.controlador_relatorio = ControladorRelatorio(self.controlador_atendimento, self.controlador_pagamento)

    @property
    def controlador_pessoa(self):
        return self.controlador_pessoa

    @property
    def controlador_clinica(self):
        return self.controlador_clinica

    @property
    def controlador_atendimento(self):
        return self.controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.controlador_pagamento

    @property
    def controlador_procedimento(self):
        return self.controlador_procedimento

    @property
    def controlador_relatorio(self):
        return self.controlador_relatorio
    
    def inicializar_sistema(self):
        while true:
            opcao = self.__tela_principal.tela_opcoes()

            if opcao == '0':
                break
            
            elif opcao == '1':
                self.__controlador_atendimento.abre_tela()

            elif opcao == '2':
                self.__controlador_clinica.abre_tela()

            elif opcao == '3':
                self.__controlador_pagamento.abre_tela()

            elif opcao == '4':
                self.__controlador_pessoa.abre_tela()

            elif opcao == '5':
                self.__controlador_procedimento.abre_tela()
            
            elif opcao == '6':
                self.__controlador_relatorio.abre_tela()

            else:
                self.__tela_principal.mostrar_mensagem("Opção inválida. Tente novamente.")
