class Player:
    def __init__(self, opcao_de_jogo):
        self.opcao_de_jogo = opcao_de_jogo


# 🧩 Tabela do jogo da velha (1D)
tabela = [" " for _ in range(10)]


# 🔁 Função para reiniciar o jogo
def zerar_tabela():
    global tabela
    tabela = [" " for _ in range(10)]


# 🎯 Exibição da tabela
def mostrar_tabela(tab):
    print(f" {tab[7]} | {tab[8]} | {tab[9]} ")
    print("——— ——— ———")
    print(f" {tab[4]} | {tab[5]} | {tab[6]} ")
    print("——— ——— ———")
    print(f" {tab[1]} | {tab[2]} | {tab[3]} ")


# ✅ Verifica se alguém venceu
def verificar_vencedor():
    combinacoes = [
        [7, 8, 9], [4, 5, 6], [1, 2, 3],  # Linhas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Colunas
        [1, 5, 9], [3, 5, 7]              # Diagonais
    ]
    for a, b, c in combinacoes:
        if tabela[a] != " " and tabela[a] == tabela[b] == tabela[c]:
            return True
    return False


# 🎮 Jogada com validação
def jogada(simbolo):
    mostrar_tabela(tabela)
    print(f"Você está jogando como {simbolo}")

    while True:
        try:
            posicao = int(input("Qual posição jogar (1–9)? "))
            if 1 <= posicao <= 9 and tabela[posicao] == " ":
                tabela[posicao] = simbolo
                break
            else:
                print("Posição inválida ou já ocupada.")
        except ValueError:
            print("Digite um número válido entre 1 e 9.")


# 🧠 Loop principal do jogo
def main():
    while True:
        opcao_de_jogo = input("\nQual você quer ser? [X ou O] ").upper()
        if opcao_de_jogo not in ["X", "O"]:
            print("Escolha válida: X ou O.")
            continue

        jogador1 = Player(opcao_de_jogo)
        jogador2 = Player("O" if jogador1.opcao_de_jogo == "X" else "X")
        players = [jogador1, jogador2]

        zerar_tabela()
        current_player_index = 0
        jogadas = 0

        while True:
            current_player = players[current_player_index]
            jogada(current_player.opcao_de_jogo)
            jogadas += 1

            if verificar_vencedor():
                mostrar_tabela(tabela)
                print(f"{current_player.opcao_de_jogo} venceu! 🎉\n")
                break

            if jogadas == 9:
                mostrar_tabela(tabela)
                print("Empate! 🤝\n")
                break

            current_player_index = (current_player_index + 1) % 2

        continuar = input("Quer jogar novamente? [s/n] ").lower()
        if continuar != "s":
            print("Obrigado por jogar! 👋")
            break




main()


