

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
    mostrar_tabela(tabela)

    print(f"Você está jogando como {x_ou_o}")

    posicao = int(input("Qual posição jogar ?"))

    if tabela[posicao] == " " :
        tabela[posicao]= x_ou_o
    else:
        print("\nAcho que você jogou errado\n")
        jogada(x_ou_o)





def main():

    numero = input("Se quer rodar o código aperte 0, se não, aperte 1 ")

    while int(numero) < 1:
        opcao_de_jogo = input("\nQual você quer ser ?[X ou O]").upper()

        jogador1 = Player(opcao_de_jogo)

        if jogador1.opcao_de_jogo == "X":
            jogador2 = Player("O")

        else:
            jogador2 = Player("X")

        players = [jogador1, jogador2]


        current_player_index = 0

        controle = 0

        controle_jogada = 0

        while controle < 1:
            current_player = players[current_player_index]

            jogada(current_player.opcao_de_jogo)

            controle_jogada += 1

            if tabela[0] == "X" and tabela[1] == "X" and tabela[2] == "X" or tabela[0]== "O" and tabela[1]== "O" and tabela[2] == "O":
                controle += 1

            elif tabela[3] == "X"  and tabela[4] == "X"  and tabela[5] == "X" or tabela[3] == "O" and tabela[4] == "O" and tabela[5] == "O":
                controle += 1

            elif tabela[6] == "X"  and tabela[7] == "X"  and tabela[8] == "X" or tabela[6] == "O" and tabela[7] == "O" and tabela[8] == "O":
                controle += 1

            elif tabela[0] == "X" and tabela[3] == "X" and tabela[6] == "X" or tabela[0] == "O" and tabela[3] == "O" and tabela[6] == "O":
                controle += 1

            elif tabela[1] == "X" and tabela[4] == "X" and tabela[7] == "X" or tabela[1] == "O" and tabela[4] == "O" and tabela[7] == "O":
                controle += 1

            elif tabela[2] == "X" and tabela[5] == "X" and tabela[8] == "X" or tabela[2] == "O" and tabela[5] == "O" and tabela[8] == "O":
                controle += 1

            elif tabela[0] == "X" and tabela[4] == "X" and tabela[8] == "X" or tabela[0] == "O" and tabela[4] == "O" and tabela[8] == "O":
                controle += 1

            elif tabela[2] == "X" and tabela[4] == "X" and tabela[6] == "X" or tabela[2] == "O" and tabela[4] == "O" and tabela[6] == "O":
                controle += 1

            elif controle_jogada == 9 :
                controle += 1
                print("\n")
                mostrar_tabela(tabela)
                print("Empate\n")

            else:
                print("")

            # Advance to the next player
            current_player_index = (current_player_index + 1) % len(players)

        numero = int(input("\nQuer continuar ?[0 sim/1 não]"))

        if numero == 0:
            numero == 0
            zerar_tabela()

        else:
            numero += 1


main()



