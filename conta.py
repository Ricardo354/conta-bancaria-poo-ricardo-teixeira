
class ContaBancaria:

    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.saldo = saldo
        pass

    def exibir_saldo(self):
        print(f"Titular - {self.titular}")
        print(f"Saldo - {self.saldo}R$")


c1 = ContaBancaria("Ricardo")

c1.exibir_saldo()