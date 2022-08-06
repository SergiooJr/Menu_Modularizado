from tkinter.tix import InputOnly
from lib.interface import *
from lib.arquivo import *

c = ["\033[m",       # sem cor
     "\033[31m",]    # vermelho       

arq = "pessoasCadastradas.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        lerArquivo(arq)
        sleep(4)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("Até a próxima!")
        break
    else:
        print(f"{c[1]}ERRO: Digite uma opção válida!{c[0]}")
        sleep(1)
