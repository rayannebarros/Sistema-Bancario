
def cadastro_nome():
    while True:
        nome=input("Digite seu nome:")
        l=['0','1','2','3','4','5','6','7','8','9']
        c=0
        for x in nome:
            if x in l:
                c+=1
        if c>0:
            print("Nome inválido.")
        else:
            return(nome)
            break

def cadastro_cpf():
    while True:
        cpf=input("Digite seu cpf:")
        l=['0','1','2','3','4','5','6','7','8','9']
        c=0
        for i in cpf:
            if i in l:
                c+=1
        if c < 11 or c > 11:
            print("Cpf inválido.")
        else:
            return(cpf)
            break
def cadastro_senha():
    while True:
        senha=input("Digite sua senha:")
        if len(senha)<4:
            print("Senha muito curta.")
        else:
            return(senha)
            break
def cadastro_numero():
    arquivo = open('ultimaconta.txt', 'r')
    conta=int(arquivo.readline())
    arquivo.close()
    gerar=conta
    conta+=1
    arquivo = open('ultimaconta.txt', 'w')
    arquivo.close()
    arquivo = open('ultimaconta.txt', 'w')
    arquivo.write(str(conta))
    arquivo.close()
    print("operação encerrada.")
    return(gerar)




