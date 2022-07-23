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

        """
    print("-------- PRODUTOS ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar produto")
    print("2 - Alterar produto")
    print("3 - Excluir produto")
    print("4 - Produtos em estoque")
    print("5 - Produtos emprestados")
    print("6 - Incluir característica")
    print("7 - Alterar característica")
    print("8 - Excluir caracteristica")
    print("9 - Listar caracteristicas")
    print("10 - Marcar defeito")
    print("11 - Listar defeitos")
    print("12 - Consertar produto")
    print("0 - Retornar")
    
    opcao = self.excecao_num_int("Escolha a opção:", [1,2,3,4,5,6,7,8,9,10,11,12,0])
    return opcao
    """

    def close(self):
        self.__window.close()

    # nome_produto: str, marca: str, modelo: str, numero_serie: int
    def pega_dados_produto(self):
        print("-------- INSIRA OS DADOS DO PRODUTO ----------")
        nome_produto = input("Nome: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        numero_serie = int(input("Número de série:"))
        return {"nome_produto": nome_produto, "marca": marca, "modelo": modelo, "numero_serie": numero_serie}

    def mostra_produto(self, dados_produto):
        print("Nome do produto: ", dados_produto["nome_produto"])
        print("Marca do Produto: ", dados_produto["marca"])
        print("Modelo: ", dados_produto["modelo"])
        print("Número de série: ", dados_produto["numero_serie"])
        print("----------------------")

    def seleciona_caracteristica(self):
        codigo = input("Código da caracteristica a ser selecionada: ")
        return codigo

    def mostra_caracteristicas(self, caracteristica):
        print("Descrição: ", caracteristica.descricao)
        print("Valor: ", caracteristica.valor)
        print("Código: ", caracteristica.codigo)
        print("----------------------")

    def pega_dados_nova_caracteristica(self):
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
        print("-------- INDIQUE A CARACTERÍSTICA DO PRODUTO ----------")
        codigo = input("Código da Característica: ")

        return {"codigo": codigo}

    def pega_codigo_defeito(self):
        print("-------- INDIQUE O CÓDIGO DO DEFEITO ----------")
        codigo = str(input("Código do defeito: "))

        return codigo

    def mostra_defeitos(self, defeito):
        print("Título: ", defeito.titulo)
        print("Descrição: ", defeito.descricao)
        print("Código: ", defeito.codigo)
        print("----------------------")

    def seleciona_produto(self):
        numero_serie = input("Número de série que deseja selecionar: ")
        return int(numero_serie)
