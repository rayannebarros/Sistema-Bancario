from classesEfuncoes import Corrente
from classesEfuncoes import Poupanca
from classesEfuncoes import Cliente
#saldo=banco[posicao].conta_poupanca.saldo
#operacoes=banco[posicao].conta_poupanca.extrato

def operar_P(banco,posicao):
    try:
        print('Nome:',banco[posicao].nome)
        print('Nº de conta:',banco[posicao].numero)
        def entrada_de_dados(pergunta):
            # FAZ UMA PARGUNTA AO USUARIO E RETORNA A RESPOSTA
            resultado = float(input(pergunta))
            return resultado

        def saque(banco):


          # Pergunta ao usuario quanto ele deseja sacar
          valor = entrada_de_dados("Valor de Saque: R$")

          # Verifica se o valor inserido pelo usuario é maior que o saldo atual
          if valor > banco[posicao].conta_poupanca.saldo:
              print("Saldo insuficiente.\n\n")
          else:
              if valor == 0 or valor < 0:
                print("Valor invalido. Tente novamente.\n")
                return saque(banco)
              # Caso o valor seja valido, subtrai ao saldo atual com 1% de juro
              banco[posicao].conta_poupanca.saldo -= valor
              print("Saque de R$%.2f efetuado com sucesso.\n\n"%valor)
              banco[posicao].conta_poupanca.extrato.append(-1*valor)

        def deposito(banco):

          # Faz pergunta ao usuario de quanto ele deseja depositar
          valor = entrada_de_dados("Valor de Deposito: R$")
          if valor == 0 or valor < 0:
                print("Valor invalido. Tente novamente.\n")
                return deposito()
          # Soma ao saldo atual
          banco[posicao].conta_poupanca.saldo += valor * 1.01
          print("Deposito de R$%.2f efetuado com sucesso.\n\n"%valor)
          banco[posicao].conta_poupanca.extrato.append(valor)

        def operacao(tipo):
          # Associa um numero a uma funcao, simulando assim um menu
            if tipo == 1: saque(banco)
            elif tipo == 2: deposito(banco)
            elif tipo == 3: extrato(banco)

        def extrato(banco):
            print("Foram registradas %i ações na sua conta:\n"%len(banco[posicao].conta_poupanca.extrato))
            for i in range(len( banco[posicao].conta_poupanca.extrato)):
                if banco[posicao].conta_poupanca.extrato[i]>=0:
                    print("-> deposito R$",  banco[posicao].conta_poupanca.extrato[i])
                elif banco[posicao].conta_poupanca.extrato[i]<0:
                    print("-> saque R$",  -1*banco[posicao].conta_poupanca.extrato[i])
            print('-> A cada deposito é adicionado 1% do mesmo no seu saldo atual!.')
            print("O saldo atual é de R$%.2f"%banco[posicao].conta_poupanca.saldo)
            print("\n")

        while True:
          print("Insira a opção desejada:")
          print("[1] - Saque\n[2] - Deposito\n[3] - Extrato\n[4] - Sair\n")
          opcao = int(input("Opção: "))
          if opcao == 4:
            print("Obrigado. Volte sempre")
            break
          operacao(opcao)
        return banco
    except:
        print('ocorreu um erro no sistema')




#saldo=banco[posicao].conta_corrente.saldo
#operacoes=banco[posicao].conta_corrente.extrato

def operar_C(banco,posicao):
    try:
        print('Nome:',banco[posicao].nome)
        print('Nº de conta:',banco[posicao].numero)
        def entrada_de_dados(pergunta):
            # FAZ UMA PARGUNTA AO USUARIO E RETORNA A RESPOSTA
            resultado = float(input(pergunta))
            return resultado

        def saque(banco):


          # Pergunta ao usuario quanto ele deseja sacar
          valor = entrada_de_dados("Valor de Saque: R$")

          # Verifica se o valor inserido pelo usuario é maior que o saldo atual
          if valor*1.01 > banco[posicao].conta_corrente.saldo:
              print("Saldo insuficiente.\n\n")
          else:
              if valor == 0 or valor < 0:
                print("Valor invalido. Tente novamente.\n")
                return saque(banco)
              # Caso o valor seja valido, subtrai ao saldo atual com 1% de juro
              banco[posicao].conta_corrente.saldo -= valor
              print("Saque de R$%.2f efetuado com sucesso.\n\n"%valor)
              banco[posicao].conta_corrente.extrato.append(-1*valor)

        def deposito(banco):

          # Faz pergunta ao usuario de quanto ele deseja depositar
          valor = entrada_de_dados("Valor de Deposito: R$")
          if valor == 0 or valor < 0:
                print("Valor invalido. Tente novamente.\n")
                return deposito()
          # Soma ao saldo atual
          banco[posicao].conta_corrente.saldo += valor
          print("Deposito de R$%.2f efetuado com sucesso.\n\n"%valor)
          banco[posicao].conta_corrente.extrato.append(valor)

        def operacao(tipo):
          # Associa um numero a uma funcao, simulando assim um menu
            if tipo == 1: saque(banco)
            elif tipo == 2: deposito(banco)
            elif tipo == 3: extrato(banco)

        def extrato(banco):
            banco[posicao].conta_corrente.saldo -= 2
            print("Foram registradas %i ações na sua conta:\n"%len(banco[posicao].conta_corrente.extrato))
            for i in range(len( banco[posicao].conta_corrente.extrato)):
                if banco[posicao].conta_corrente.extrato[i]>=0:
                    print("-> deposito R$",  banco[posicao].conta_corrente.extrato[i])
                elif banco[posicao].conta_corrente.extrato[i]<0:
                    print("-> saque R$",  -1*banco[posicao].conta_corrente.extrato[i])
            print("-> Taxa do extrato de R$2.00")
            print('-> A cada saque é descontado um juro de 1% sobre seu valor.')
            print("O saldo atual é de R$%.2f"%banco[posicao].conta_corrente.saldo)
            print("\n")

        while True:
          print("Insira a opção desejada:")
          print("[1] - Saque\n[2] - Deposito\n[3] - Extrato\n[4] - Sair\n")
          opcao = int(input("Opção: "))
          if opcao == 4:
            print("Obrigado. Volte sempre")
            break
          operacao(opcao)
        return banco
    except:
        print('ocorreu um erro no sistema')
