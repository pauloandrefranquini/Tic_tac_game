

tabela = [ " " for i in range(9)]

def mostrar_tabela(tab):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("——— ———— ———")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("——— ———— ———")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")


def jogada():
    posicao = int(input("Qual posição jogar ?"))

    tabela[posicao]= "X"

    mostrar_tabela(tabela)



mostrar_tabela(tabela)

qual_jogar = input("Qual você quer ser ?[X ou O]").upper()

if qual_jogar == "X":
    jogada()



