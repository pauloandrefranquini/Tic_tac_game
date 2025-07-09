

class Player:
    def __init__(self, opcao_de_jogo):
        self.opcao_de_jogo = opcao_de_jogo


tabela = [ " " for i in range(9)]



def zerar_tabela():
    for i in range(9):
        tabela[i]= " "


def mostrar_tabela(tab):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("——— ——— ———")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("——— ——— ———")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")


def jogada(x_ou_o):
    posicao = int(input("Qual posição jogar ?"))

    tabela[posicao]= x_ou_o

    mostrar_tabela(tabela)


def victory_or_draw(jogador):
    controle = 0

    while controle < 1:
        jogada(jogador.opcao_de_jogo)  # fazer um while loop dentro de um while loop para gerar alternância de turnos

        if tabela[0] and tabela[1] and tabela[2] == "X" or tabela[0] and tabela[1] and tabela[2] == "O":
            controle += 1

        elif tabela[3] and tabela[4] and tabela[5] == "X" or tabela[3] and tabela[4] and tabela[5] == "O":
            controle += 1

        elif tabela[6] and tabela[7] and tabela[8] == "X" or tabela[6] and tabela[7] and tabela[8] == "O":
            controle += 1

        elif tabela[0] and tabela[3] and tabela[6] == "X" or tabela[0] and tabela[3] and tabela[6] == "O":
            controle += 1

        elif tabela[1] and tabela[4] and tabela[7] == "X" or tabela[1] and tabela[4] and tabela[7] == "O":
            controle += 1

        elif tabela[2] and tabela[5] and tabela[8] == "X" or tabela[2] and tabela[5] and tabela[8] == "O":
            controle += 1

        elif tabela[0] and tabela[4] and tabela[8] == "X" or tabela[0] and tabela[4] and tabela[8] == "O":
            controle += 1

        elif tabela[2] and tabela[4] and tabela[6] == "X" or tabela[2] and tabela[4] and tabela[6] == "O":
            controle += 1

        else:
            controle = 0  # adicionar forma do jogo finalizar empatado neste else

def criacao_dos_players():

    x_ou_o = input("Qual você quer ser ?[X ou O]").upper()
    x_ou_o1 = " "

    if x_ou_o == "X" or x_ou_o == "O":
        jogador1 = Player(x_ou_o)
        if x_ou_o == "X":
            x_ou_o1 == "O"
            jogador2 = Player(x_ou_o1)
        else:
            x_ou_o1 == "X"
            jogador2 = Player(x_ou_o1)
    else:
        print("""__________________________________________
           \nEscolha apenas entre X ou O !!!\n__________________________________________""")

        ligacao()

    victory_or_draw(jogador1)





def jogada(x_ou_o):
    posicao = int(input("Qual posição jogar ?"))

    tabela[posicao]= x_ou_o

    mostrar_tabela(tabela)



def ligacao():

    mostrar_tabela(tabela)

    criacao_dos_players()




def main():

    numero = input("Se quer rodar o código aperte 0, se não, aperte 1 ")

    while int(numero) < 1:
        ligacao()

        numero = int(input("Quer continuar ?[0 sim/1 não]"))

        if numero == 0:
            numero == 0
            zerar_tabela()

        else:
            numero += 1


main()



