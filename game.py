

class Player:
    def __init__(self, opcao_de_jogo):
        self.opcao_de_jogo = opcao_de_jogo


tabela = [ " " for i in range(9)]

def mostrar_tabela(tab):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("——— ——— ———")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("——— ——— ———")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")


def jogada(vez):
    posicao = int(input("Qual posição jogar ?"))

    tabela[posicao]= vez

    mostrar_tabela(tabela)


def vitoria_empate():

    mostrar_tabela(tabela)

    qual_jogar = input("Qual você quer ser ?[X ou O]").upper()

    if qual_jogar == ("X" or "O"):
        jogador1 = Player(qual_jogar)
    else:
        print("""__________________________________________
        \nEscolha apenas entre X ou O !!!\n__________________________________________""")
        vitoria_empate()

    #Aqui colocarei um while loop para
    # o jogo só interromper dadas algumas condições

    jogada(jogador1.opcao_de_jogo)


def vai_parar():
    numero = 0

    numero = input("Se quer rodar o código aperte 0, se não, aperte 1 ")

    while int(numero) < 1:
        vitoria_empate()

        numero = int(input("Quer continuar ?[0 sim/1 não]"))

        if numero == 0:
            numero == 0
        else:
            numero += 1


vai_parar()



