class Conta:
    def __init__(self, numero) :
        self.__numero = numero
        self.__saldo = 0.0
    
    @property
    def numero (self) :
        return self.__numero
    @numero.setter
    def numero(self, value_numero) :
        self.__numero = value_numero

    @property
    def saldo (self) :
        return self.__saldo  
    @saldo.setter
    def saldo(self, value_salario) :
        raise "Operação proibida! O saldo não pode ser implementado diretamente"
    
    def depositar (self, valor) :
        self.__saldo = self.__saldo + valor

    def sacar (self, valor) :
        self.__saldo = self.__saldo - valor
        
class ContaCorrente(Conta):
    def __init__(self, numero, taxa):
        Conta.__init__(self, numero)
        self.__taxa = taxa
        
    @property
    def taxa(self):
        return self.__taxa
    @taxa.setter
    def taxa(self, value_taxa) :
        raise "Operação proibida! O valor da taxa não pode ser alterado"

    def cobrar_taxa(self) :
        self.sacar(self.taxa)
        
class ContaPoupanca(Conta):
    def __init__(self, numero, juros):
        Conta.__init__(self, numero)
        self.__juros = juros
        
    @property
    def juros(self):
        return self.__juros
    @juros.setter
    def juros(self, value_juros) :
        raise "Operação proibida! O valor dos juros mensais não pode ser alterado"
   
    def aplicar_juros(self) :
       self.depositar(self.saldo * self.juros)