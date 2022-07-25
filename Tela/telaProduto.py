from Tela.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaProduto(TelaAbstrata):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Opções para produtos:', font=('Helvetica', 20), justification='center')],
            [sg.Button('Cadastrar Produto', key='1', size=(15, 2), button_color='#008015'),
             sg.Button('Editar Produto', key='2', size=(15, 2)),
             sg.Button('Excluir Produto', key='3', size=(15, 2), button_color='#d5001d')
             ],
            [sg.Button('Produtos em Estoque', key='4', size=(24, 2)),
             sg.Button('Produtos Emprestados', key='5', size=(24, 2))
             ],
            [sg.Text('_'*60)],
            [sg.Text('Opções para características de produto:', font=('Helvetica', 15))],
            [sg.Button('Incluir Característica', key='6', size=(15, 2), button_color='#008015'),
             sg.Button('Alterar Característica', key='7', size=(15, 2)),
             sg.Button('Excluir Característica', key='8', size=(15, 2), button_color='#d5001d')
             ],
            [sg.Button('Listar Características', key='9', size=(50, 1))
             ],
            [sg.Text('_' * 60)],
            [sg.Text('Defeitos:', font=('Helvetica', 15))],
            [sg.Button('Marcar Defeito', key='10', size=(15, 2), button_color='#008015'),
             sg.Button('Listar Defeitos', key='11', size=(15, 2)),
             sg.Button('Consertar Produto', key='12', size=(15, 2), )
             ],
            [sg.Text('-' * 100)],
            [sg.Button('<< Retornar <<', key='0', size=(15, 1), button_color='#500000')]
        ]
        self.__window = sg.Window('TELA PRODUTO', element_justification='c').Layout(layout)

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

    def pega_dados_produto(self):
        layout = [[sg.Text('Nome do produto:', size=(15, 1)), sg.InputText('', key='nome_produto')],
                  [sg.Text('Marca:', size=(15, 1)), sg.InputText('', key='marca')],
                  [sg.Text('Modelo:', size=(15, 1)), sg.InputText('', key='modelo')],
                  [sg.Text('Número de série:', size=(15, 1)), sg.InputText('', key='numero_serie')],
                  [sg.Submit('Cadastrar', button_color='#008000')]
                  ]
        self.__window = sg.Window('CADASTRAR PRODUTO').Layout(layout)

        while True:
            botao, valor = self.open()
            nome_produto = valor['nome_produto']
            marca = valor['marca']
            modelo = valor['modelo']
            numero_serie = self.excecao_tipo_int(valor['numero_serie'], int)

            if (nome_produto != '') and (marca != '') and (modelo != '') and isinstance(numero_serie, int):
                self.close()
                return {"nome_produto": nome_produto, "marca": marca, "modelo": modelo, "numero_serie": numero_serie}

    def mostra_produto(self, dados_produto):
        listagem_produtos = ""
        contador = 1
        for dado in dados_produto:
            listagem_produtos = listagem_produtos + str(contador) + '\n'
            listagem_produtos = listagem_produtos + "Nome do Produto: " + str(dado["nome_produto"]) + '\n'
            listagem_produtos = listagem_produtos + "Marca do Produto: " + str(dado["marca"]) + '\n'
            listagem_produtos = listagem_produtos + "Modelo: " + str(dado["modelo"]) + '\n'
            listagem_produtos = listagem_produtos + "N° Série: " + str(dado["numero_serie"]) + '\n\n'
            contador += 1
        sg.Popup('LISTA DE PRODUTOS', listagem_produtos)

    def seleciona_caracteristica(self):
        # codigo = input("Código da caracteristica a ser selecionada: ")
        layout = [
            [sg.Text('Qual o código da caracteristica a ser selecionada?', font=("Helvica", 9))],
            [sg.Text('Código:', size=(8, 1)), sg.InputText('', key='codigo')],
            [sg.Submit('Selecionar', button_color='#008000')]
        ]
        self.__window = sg.Window('SELECIONE A CARACTERISTICA').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo


    def mostra_caracteristicas(self, produto):
        caracteristicas = 'Descrição - Valor - Código: \n\n'
        for caracteristica in produto.caracteristicas:
            caracteristicas += (str(caracteristica.descricao) + ' - ' +
                                str(caracteristica.valor) + ' - ' +
                                str(caracteristica.codigo) + '\n')

        sg.Popup('CARACTERISTICAS', caracteristicas)

    def pega_dados_nova_caracteristica(self):
        layout = [[sg.Text('Valor:', size=(15, 1)), sg.InputText('', key='valor')],
                  [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
                  [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
                  [sg.Submit('Cadastrar', button_color='#008000')]
                  ]
        self.__window = sg.Window('INCLUIR CARACTERÍSTICA').Layout(layout)

        while True:
            botao, value = self.open()
            valor = value['valor']
            descricao = value['descricao']
            codigo = value['codigo']

            if (valor != '') and (descricao != '') and (codigo != ''):
                self.close()
                return {"valor": valor, "descricao": descricao, "codigo": codigo}
            else:
                self.mostra_mensagem("ERRO","Entradas inválidas, por favor repita a operação!")
                return None

    def pega_dados_nova_caracteristica_old(self):
        print("-------- INSIRA OS DADOS DA CARACTERÍSTICA ----------")
        valor = str(input("Valor: "))
        descricao = input("Descrição: ")
        codigo = str(input("Codigo: "))
        if isinstance(valor, str) and isinstance(descricao, str) and isinstance(codigo, str):
            return {"valor": valor, "descricao": descricao, "codigo": codigo}
        else:
            self.mostra_mensagem("Entradas inválidas, por favor repita a operação!")
            return None

    def pega_caracteristica_no_produto(self):
        layout = [
            [sg.Text('Qual o código da característica?', font=("Helvica", 9))],
            [sg.Text('Código:', size=(8, 1)), sg.InputText('', key='codigo')],
            [sg.Submit('Selecionar', button_color='#008000')]
        ]
        self.__window = sg.Window('CODIGO DA CARACTERÍSTICA').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return {"codigo": codigo}
        # print("-------- INDIQUE A CARACTERÍSTICA DO PRODUTO ----------")
        # codigo = input("Código da Característica: ")


    def pega_codigo_defeito(self):
        # print("-------- INDIQUE O CÓDIGO DO DEFEITO ----------")
        # codigo = str(input("Código do defeito: "))
        layout = [
            [sg.Text('Qual o código do defeito?', font=("Helvica", 9))],
            [sg.Text('Código:', size=(8, 1)), sg.InputText('', key='codigo')],
            [sg.Submit('Selecionar', button_color='#008000')]
        ]
        self.__window = sg.Window('CODIGO DO DEFEITO').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()

        return codigo

    def mostra_defeitos(self, produto):
        defeitos = 'Descrição - Código: \n\n'
        for defeito in produto.defeitos:
            defeitos += (str(defeito.descricao) + ' - ' + str(defeito.codigo) + '\n')

        sg.Popup('DEFEITOS', defeitos)

    def seleciona_produto(self):
        layout = [
            [sg.Text('Qual o N°Série que deseja selecionar?', font=("Helvica", 9))],
            [sg.Text('N°Série:', size=(8, 1)), sg.InputText('', key='numero_serie')],
            [sg.Submit('Selecionar', button_color='#008000')]
        ]
        self.__window = sg.Window('SELECIONE O PRODUTO').Layout(layout)

        button, values = self.open()
        numero_serie = self.excecao_tipo_int(values['numero_serie'], int)
        self.close()
        return numero_serie
