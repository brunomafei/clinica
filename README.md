# 🏥 Sistema de Gerenciamento de Clínica Médica

Este projeto é um sistema de gerenciamento de clínicas desenvolvido em **Python 3**, utilizando o padrão de arquitetura **MVC (Model-View-Controller)** e os princípios da **Orientação a Objetos**. 

O sistema foi desenvolvido como requisito de avaliação da disciplina de **INE5605 - Desenvolvimento de Sistemas Orientados a Objetos I** do curso de Sistemas de Informação da Universidade Federal de Santa Catarina (UFSC).

## 🚀 Funcionalidades Principais
O sistema permite o gerenciamento completo do fluxo de uma clínica, operando inteiramente em memória (sem persistência em banco de dados nesta etapa).
* **Gerenciamento de Pessoas:** Cadastro, alteração, listagem e exclusão de Pacientes e Profissionais de Saúde.
* **Gerenciamento de Clínicas:** Controle de unidades, incluindo horários de funcionamento.
* **Agendamentos:** Controle de consultas e exames, com validação de idade mínima (18 anos) e verificação de cadastros existentes.
* **Procedimentos:** Registro de procedimentos e custos vinculados aos profissionais.
* **Pagamentos:** Sistema de pagamentos com suporte a transações parciais (abatimento do valor total) utilizando polimorfismo para diferentes modalidades (PIX, Cartão de Crédito e Cédula).
* **Relatórios:** Emissão de dados estatísticos do sistema, incluindo clínicas com mais atendimentos, procedimentos mais populares, e os atendimentos/procedimentos mais caros e mais baratos.

## 🛠️ Tecnologias e Arquitetura
* **Linguagem:** Python 3.12+
* **Arquitetura:** MVC (Model, View, Controller)
* **Tratamento de Erros:** Implementação de Exceções Personalizadas (`ElementoNaoExisteException`, `ElementoRepetidoException`).

---

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado na sua máquina.
2. Clone o repositório ou extraia o arquivo ZIP do projeto.
3. Navegue pelo terminal até a pasta raiz do projeto.
4. Execute o arquivo principal:
   ```bash
   python main.py
   # ou dependendo do seu sistema:
   python3 main.py