from classesEfuncoes import Corrente
from classesEfuncoes import Poupanca
from classesEfuncoes import Cliente
from armazenamento import salvar
from armazenamento import carregar
from interface import ler_opcao
from interface import exibir_menu
from interface import mensagem_entrada
from interface import mensagem_saida
from cadastramento import cadastro_nome
from cadastramento import cadastro_cpf
from cadastramento import cadastro_senha
from cadastramento import cadastro_numero
from operacoes import operar_P
from operacoes import operar_C

banco=[]
banco=carregar(banco)

def pesquisar(banco):              #pesquisar cliente pelo cpf
    cpf=cadastro_cpf()
    encontrado=False
    for i in range(len(banco)):
        if (banco[i].cpf==cpf):
            print('cliente:',banco[i].nome)
            print('Nº de conta:',banco[i].numero)
            encontrado=True
            break
    if encontrado == False :
        print('cliente não encontrado')


def posicao_cliente(banco,n_conta):             #deve ser usada junto com operador del[deletar_cliente(banco,n_conta)]
    for i in range(len(banco)):
        if (banco[i].numero==n_conta):
            return i
            break

def deletar_cliente():
    while True:
        try:
            n_conta=int(input("Digite numero de conta:"))
            x=posicao_cliente(banco,n_conta)
            if x != None:
                senha_teste=cadastro_senha()
                if senha_teste==banco[x].senha:
                    del banco[x]
                    print('cliente removido')
                    break
                else:
                    print('senha incorreta')
                    break
            else:
                print('cliente não encontrado')
                break
        except:
            print('operação não realizada')
            break

def login(banco):
    try:
        n_conta=int(input("Digite numero de conta:"))
        x=posicao_cliente(banco,n_conta)
        if x!= None :
            senha=cadastro_senha()
            if(senha==banco[x].senha):
                print('login efetuado')
                return True, x
            else:
                print('senha incorreta')
                return False, 1000000000000000
        else:
            print('cliente não encontrado!')
            return False , 1000000000000000
    except:
        print('conta inválida')


def teste(banco):      #função criada para testar se o programa está atualizando a lista de clientes apos as operações
    for i in range (len(banco)):
        print(banco[i].nome, banco[i].senha, banco[i].cpf, banco[i].numero, banco[i].conta_corrente.saldo, banco[i].conta_poupanca.saldo )





while True:

    try:   # exibir menu
        exibir_menu()
        # ler opcao

        opcao = ler_opcao()
    except:
        print('erro')

        break


    # chamar os serviços dos módulos
    if opcao == 1:
        nome=cadastro_nome()
        senha=cadastro_senha()
        cpf=cadastro_cpf()
        numero=cadastro_numero()
        cpf_novo=True                                       #problema do cpf
        for k in range(len(banco)):                         #problema do cpf
            if(cpf==banco[k].cpf):                          #problema do cpf
                cpf_novo=False                              #problema do cpf
                break                                       #problema do cpf
        if cpf_novo:                                        #problema do cpf
            banco.append(Cliente(nome,cpf,senha,numero))
            print('cadastro efetuado')
            print('|nome: ' ,nome,'|CPF: ',cpf,'|senha: ',senha,'|Nº de conta: ',numero)
        else:                                               #problema do cpf
            print('cpf existente')                          #problema do cpf
    elif opcao == 2:
        pesquisar(banco)
    elif opcao == 3:
        cond,posicao = login(banco)
        if cond :
            tipo=input('acessar conta corrente(digite c) | conta poupanca (digite p) | mudar senha(digite s): ')
            if(tipo=='c'):
                banco=operar_C(banco,posicao)

            elif(tipo=='p'):
                banco=operar_P(banco,posicao)
            elif(tipo=='s'):
                nova_senha=cadastro_senha()
                banco[posicao].senha=nova_senha
            else:
                print('opcao invalida')

    elif opcao == 4:
        deletar_cliente()
    else:
        break
    teste(banco)        #testa atualizações
    #try:                      #correcao problema extrato/arquivo
       # salvar(banco)         #correcao problema extrato/arquivo
   # except:                    #correcao problema extrato/arquivo
        #print('erro inesperado')     #correcao problema extrato/arquivo



# saída do programa
mensagem_saida()

try:                      #correcao problema extrato/arquivo
    salvar(banco)         #correcao problema extrato/arquivo
except:                    #correcao problema extrato/arquivo
    print('erro inesperado')     #correcao problema extrato/arquivo


