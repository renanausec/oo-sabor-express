from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title() #este .title() faz a primeira letra de cada nome ficar maiuscula
        self._categoria = categoria.upper() # .upper() deixa tudo maiusculo
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') #o ativo nao alteramos para _ativo aqui pois queremos a @property
    
    @property #decorador do python (precisa colocar _ativo no metodo original)
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self): #inverte de False para True ou vice-versa
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property #precisamos ser capazes de ler essas informações para cada um dos restaurantes por isso é uma @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao: #se aquele restaurante não tiver nenhuma avaliação mostra o seguinte 0
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #pega cada avaliacao e soma essas notas
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1) #usamos o round(x,1) para deixar apenas 1 casa decimal apos a virgula
        return media
    
    # def adicionar_bebidas_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item): #esse método resume as duas anteriormente comentadas para fazer apenas um método
        if isinstance(item, ItemCardapio): #verifica se a bebida ou prato é uma instancia do cardapio ou uma classe derivada de cardapio
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self): #faz sentido ser uma @property pois só queremos ler o que vai apresentar
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1): #i aqui significa o índice e o start=1 pra começar do 1 e nao do zero
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)