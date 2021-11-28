from abc import ABC, abstractmethod

class Item(ABC):
    def __init__ (self, initNome, initValor):
        self.__nome = initNome
        self.__valor = initValor
        
    @property
    def nome(self):
        return self.__nome
    @property
    def valor(self):
        return self.__valor

    def valor_desconto(self):
        return self.valor - (self.valor * self.desconto)

    @abstractmethod
    def desconto(self):
        pass
    @abstractmethod
    def tipo(self):
        pass

class Livro (Item):
    def __init__ (self, initNome, initValor):
        Item.__init__(self, initNome, initValor)
        self.__desconto = 0.03
        self.__tipo = "Livro"
    
    @property
    def desconto (self):
        return self.__desconto

    @desconto.setter
    def desconto (self):
        raise "Não é possível alterar o valor do desconto para esse item"

    @property
    def tipo (self):
        return self.__tipo
    
    @tipo.setter
    def tipo (self):
        self.__tipo = "Livro"
    
class Brinquedo (Item):
    def __init__ (self, initNome, initValor):
        Item.__init__(self, initNome, initValor)
        self.__desconto = 0.05
        self.__tipo = "Brinquedo"
    
    @property
    def desconto (self):
        return self.__desconto

    @desconto.setter
    def desconto (self):
        raise "Não é possível alterar o valor do desconto para esse item"

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo (self):
        self.__tipo = "Brinquedo"
        

class Eletronico (Item):
    def __init__ (self, initNome, initValor):
        Item.__init__(self, initNome, initValor)
        self.__desconto = 0.08
        self.__tipo = "Eletrônico"
    
    @property
    def desconto (self):
        return self.__desconto

    @desconto.setter
    def desconto (self):
        raise "Não é possível alterar o valor do desconto para esse item"

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo (self):
        self.__tipo = "Eletrônico"
        
    
class CestaCompras:
    def __init__ (self):
        self.itens = {}

    def adicionar_item (self, item, initQtde):
        self.__qtde = initQtde
        self.itens.update({item : self.__qtde})

        @property
        def qtde(self):
            return self.__qtde

        @qtde.setter
        def qtde(self):
            self.__qtde = initQtde
    
    def valor_total_item(self, item, qtde):
        return item.valor * qtde
            
    def relatorio_final(self):
        valor_total_compra_desconto = 0
        for item, qtde in self.itens.items():
            valor_total_compra_desconto += item.valor_desconto()*qtde
        print("%.2f" %(valor_total_compra_desconto))

        for item, qtde in self.itens.items():
            print("%s, %s, %i, %.2f, %.2f, %.2f" % (item.tipo, item.nome, qtde, 
            item.valor, self.valor_total_item(item, qtde), item.valor_desconto()*qtde))