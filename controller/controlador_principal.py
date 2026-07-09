from controller.controlador_atendimento import ControladorAtendimento
from controller.controlador_clinica import ControladorClinica
from controller.controlador_pagamento import ControladorPagamento
from controller.controlador_pessoa import ControladorPessoa
from controller.controlador_procedimento import ControladorProcedimento
from controller.controlador_relatorio import ControladorRelatorio
from view.tela_principal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa()
        self.__controlador_clinica = ControladorClinica()
        self.__controlador_procedimento = ControladorProcedimento()
        
        # Injeção ajustada: agora passamos o controlador de procedimento também!
        self.__controlador_atendimento = ControladorAtendimento(
            self.__controlador_pessoa, 
            self.__controlador_clinica,
            self.__controlador_procedimento
        )
        
        self.__controlador_pagamento = ControladorPagamento(
            self.__controlador_atendimento)
            
        self.__controlador_relatorio = ControladorRelatorio(
            self.__controlador_clinica,
            self.__controlador_procedimento,
            self.__controlador_atendimento
        )
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    @property
    def controlador_procedimento(self):
        return self.__controlador_procedimento

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_principal.tela_opcoes()

            if opcao in (0, -1):
                break
            elif opcao == 1:
                self.__controlador_atendimento.abre_tela()
            elif opcao == 2:
                self.__controlador_clinica.abre_tela()
            elif opcao == 3:
                self.__controlador_pagamento.abre_tela()
            elif opcao == 4:
                self.__controlador_pessoa.abre_tela()
            elif opcao == 5:
                self.__controlador_procedimento.abre_tela()
            elif opcao == 6:
                self.__controlador_relatorio.abre_tela()
            else:
                self.__tela_principal.mostra_mensagem(
                    "Opção inválida. Tente novamente.")