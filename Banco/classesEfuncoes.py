class Corrente:
    def __init__(self,numero):
        self.saldo=0.00
        self.numero=numero
        self.status=True
        self.extrato=[]
    def deposito(self,valor):
        if (self.status):
            self.saldo+=valor
            self.extrato.append(valor)
            return True
        else:
            return False
    def saque(self,valor):
        if (self.status):
            if(self.saldo >= valor*(1+1/100)):
                self.saldo-=valor*(1+1/100)
                self.extrato.append(-1*valor)
                return True
            else:
                return False
        else:
            return True

    def info_saldo(self):
        if(self.status):
            return self.saldo
        else:
            return False



class Poupanca:
    def __init__(self,numero):
        self.saldo=0.00
        self.numero=numero
        self.status=True
        self.extrato=[]
    def deposito(self,valor):
        if (self.status):
            self.saldo+=valor*(1+1/100)
            self.extrato.append(valor)
            return True
        else:
            return False
    def saque(self,valor):
        if (self.status):
            if(self.saldo >= valor*(1+1/100)):
                self.saldo-=valor*(1+1/100)
                self.extrato.append(-1*valor)
                return True
            else:
                return False
        else:
            return False

    def info_saldo(self):
        if(self.status):
            return self.saldo
        else:
            return False

class Cliente:
    def __init__(self,nome,cpf,senha,numero):
        self.nome=nome
        self.cpf=cpf
        self.senha=senha
        self.numero=numero
        self.conta_corrente=Corrente(self.numero)
        self.conta_poupanca=Poupanca(self.numero)

    def abrir_conta(self,tipo):
        if(self.conta_corrente.status==False):
            if(tipo=='c' or tipo=='C'):
                self.conta_corrente.status=True
                return True
            elif(tipo=='p' or tipo=='P'):
                self.conta_poupanca.status=True
                return True
            else:
                return False
        else:
            return False

    def remover_conta(self,tipo):
        if(tipo=='c' or tipo=='C'):
            self.conta_corrente.status=False
            self.conta_corrente.saldo=0.00
            return True
        elif(tipo=='p' or tipo=='P'):
            self.conta_poupanca.status=False
            self.conta_poupanca.saldo=0.00
            return True
        else:
            return False

    def mudar_senha(self,nova_senha):
        self.senha=nova_senha

