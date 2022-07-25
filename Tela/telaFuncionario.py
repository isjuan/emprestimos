from Tela.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaFuncionario(TelaAbstrata):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [  # [sg.Listbox(values=('funcionario 2', 'funcionario3'), size=(30, 3))],
            [sg.Button('Cadastrar funcionário', key='1', size=(15, 2), button_color='#008015'),
             sg.Button('Excluir funcinário', key='4', size=(15, 2), button_color='#d5001d')],
            [sg.Button('Editar funcionário', key='3', size=(32, 2))],
            [sg.Button('Listar funcionários', key='2', size=(32, 2))],
            [sg.Button('<< Retornar <<', key='0', size=(15, 1), button_color='#500000')]
        ]
        self.__window = sg.Window('Funcionarios', element_justification='c').Layout(layout)

    def tela_opcoes(self):
        self.init_components()
        botao, valores = self.__window.Read()
        if botao is None:
            botao = 0
        self.close()
        return int(botao)

    def open(self):
        botao, valor = self.__window.Read()
        return botao, valor

    def close(self):
        self.__window.close()

    def pega_dados_funcionario(self):
        layout = [[sg.Text('Nome:', size=(8, 1)), sg.InputText('', key='nome')],
                  [sg.Text('Matrícula:', size=(8, 1)), sg.InputText('', key='matricula')],
                  [sg.Submit('Cadastrar', button_color='#008000')]
                  ]
        self.__window = sg.Window('Cadastrar funcionario').Layout(layout)

        while True:
            botao, valor = self.open()
            nome = valor['nome']
            matricula = self.excecao_tipo_int(valor['matricula'], int)

            if nome != '' and isinstance(matricula, int):
                self.close()
                return {"nome": nome, "matricula": matricula}

    def seleciona_funcionario(self):

        layout = [
            [sg.Text('Qual matrícula deseja selecionar?', font=("Helvica", 9))],
            [sg.Text('Matrícula:', size=(8, 1)), sg.InputText('', key='matricula')],
            [sg.Submit('Selecionar', button_color='#008000')]
        ]
        self.__window = sg.Window('Seleciona funcionario').Layout(layout)

        button, values = self.open()
        matricula = self.excecao_tipo_int(values['matricula'], int)
        self.close()

        return matricula

    def mostra_funcionario(self, dados_funcionario):
        listagem_funcionarios = ""
        contador = 1
        for dado in dados_funcionario:
            listagem_funcionarios = listagem_funcionarios + str(contador) + '\n'
            listagem_funcionarios = listagem_funcionarios + "FUNCIONÁRIO: " + dado["nome"] + '\n'
            listagem_funcionarios = listagem_funcionarios + "MATRICULA: " + str(dado["matricula"]) + '\n\n'
            contador += 1
        sg.Popup('LISTA DE FUNCIONÁRIOS', listagem_funcionarios)
