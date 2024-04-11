from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #isso significa que a classe Pratro vai herdar metodos e atributos da classe ItemCardapio para dentro da classe Prato
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #aqui a classe Prato pega os atributos da classe pai ItemCardapio
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05) #pega o preço original e subtrai 5% dele