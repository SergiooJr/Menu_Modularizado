from time import sleep

def l(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(l())
    print(txt.center(42))
    print(l())

def leiaInt(v):
    while True:
        n = input(v)
        if n.isalpha():
            print("Digite um número inteiro válido!")
            continue
        else:
            return int(n)

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c} - \033[34m{item}\033[m")
        c += 1
    print(l())
    opc = leiaInt("\033[32mSua opção: \033[m")
    print("\033[90mUm momento...\033[m")
    sleep(1)
    return opc