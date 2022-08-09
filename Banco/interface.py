def ler_opcao():
    opcao =int(input("\nDigite sua opção:"))
    return opcao
def exibir_menu():
    print(155*"=")
    print(62*'-' + " \033[1;34;43m Escolha uma opção a seguir \033[m " + 62*'-')
    print(155*"=")
    print(15*" "+" \033[7;30;46m[1]\033[m\033[7;36;40m Cadastrar Clientes \033[m -=- \033[7;30;46m[2]\033[m\033[7;36;40m"
          " Consultar Clientes \033[m -=- \033[7;30;46m[3]\033[m\033[7;36;40m Acessar Conta \033[m -=- \033[7;30;46m"
          "[4]\033[m\033[7;36;40m Remover Cliente \033[m -=- \033[7;30;46m[5]\033[m\033[7;36;40m Sair \033[m ")
    print(155*"=")

def mensagem_entrada():
    print("Seja bem vindo.")
def sair():
    entrada = input("Tem certeza que quer sair(s/n)?")
    return entrada.lower() == 's'
def mensagem_saida():
    print("Sistema encerrado.")
