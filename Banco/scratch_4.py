reset=0;
while(reset == 0):
    voto = int(input("digite seu voto: "))
    print("\n")
    if (voto == 13) :
        haddad+=1
    else:
        if (voto == 17) :
            bolsonaro+=1
    else:
        nulo+=1
    reset = input("digite número diferente de 0 para sair: ")
    print("\n")
    if reset != 0:
        break
print("haddad: ", haddad, "\n", "bolsonaro", bolsonaro, "\n")
