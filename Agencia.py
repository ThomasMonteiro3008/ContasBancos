from random import randint

class Agencia:


    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R${:,.2f}'.format(self.caixa))
        else:
            print('Caixa atual com valor dentro dos padrões, valor: R${:,.2f}'.format(self.caixa))

    def emprestar(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))

        else:
            print('Dinheiro não disponível em caixa')

    def adicionar_clientes(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

#Agencia Virtual
class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


#Agencia Comum
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


#Agencia Premium
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_clientes(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_clientes(nome, cpf, patrimonio)
        else:
            print('Cliente não tem o patrimônio mínimo necessário para entrar na agência Premium')




