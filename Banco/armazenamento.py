
from classesEfuncoes import Corrente
from classesEfuncoes import Poupanca
from classesEfuncoes import Cliente

def limpar_info():                  #limpa o arquivo com as informações
    arquivo = open('clientes.txt', 'w')
    arquivo.close()

def salvar(lista_clientes):              #salva a lista de clientes de um arquivo
    limpar_info()
    for i in range (len(lista_clientes)):
        arquivo = open('clientes.txt', 'a')
        arquivo.write(lista_clientes[i].nome)
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].senha))
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].cpf))
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].numero))
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].conta_corrente.status))
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].conta_corrente.saldo))
        arquivo.write('\n')
        for j in range(len(lista_clientes[i].conta_corrente.extrato)):
            arquivo.write(str(lista_clientes[i].conta_corrente.extrato[j]))
            arquivo.write(' ')
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].conta_poupanca.status))
        arquivo.write('\n')
        arquivo.write(str(lista_clientes[i].conta_poupanca.saldo))
        arquivo.write('\n')
        for j in range(len(lista_clientes[i].conta_poupanca.extrato)):
            arquivo.write(str(lista_clientes[i].conta_poupanca.extrato[j]))
            arquivo.write(' ')
        arquivo.write('\n')
        arquivo.close()
    return lista_clientes

def carregar(lista_clientes):          #gera a lista de clientes de um arquivo
    arquivo = open('clientes.txt', 'r')
    texto=arquivo.readlines()
    arquivo.close()
    n=int(len(texto)/10)
    arquivo = open('clientes.txt', 'r')
    for i in range(n):
        nome=arquivo.readline()                                       #linha1
        nome = nome.replace('\n','')
        senha = arquivo.readline()                                    #linha3
        senha = senha.replace('\n', '')
        cpf=arquivo.readline()                                        #linha2
        cpf = cpf.replace('\n', '')
        numero=arquivo.readline()                                     #linha4
        numero = int(numero.replace('\n', ''))

        lista_clientes.append(Cliente(nome,cpf,senha,numero))

        sc=arquivo.readline()                                               #linha5
        sc=sc.replace('\n','')
        if(sc=='True'):
            lista_clientes[i].conta_corrente.status=True
        else:
            lista_clientes[i].conta_corrente.status = False
        lista_clientes[i].conta_corrente.saldo=float(arquivo.readline())     #linha6
        ext1=arquivo.readline()                                              #linha7
        ext1=ext1.replace('\n','')
        t1=ext1.split()
        lista_clientes[i].conta_corrente.extrato=t1

        sp=arquivo.readline()                                                #linha8

        sp = sp.replace('\n', '')
        if(sp=='True'):
            lista_clientes[i].conta_corrente.status=True
        else:
            lista_clientes[i].conta_corrente.status = False
        lista_clientes[i].conta_poupanca.saldo=float(arquivo.readline())        #linha9
        ext2=arquivo.readline()                                                 #linha10
        ext2=ext2.replace('\n','')
        t2=ext2.split()
        lista_clientes[i].conta_poupanca.extrato=t2

    arquivo.close()
    return lista_clientes
