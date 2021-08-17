from Poke_game import * # Importa o módulo com a classe "Poke_game"
from os import system # Importa a função system da biblioteca os


def main(): # Define a função principal
    
    print('-'*20)
    print('PokeGame'.center(20))
    print('-'*20)

    print('>>> Escolha um pokemón na lista abaixo e eu irei adivinhar qual você escolheu!\n') # Imprime as instruções do jogo

    while True: #Looping infinito
        jogo = Poke_game() # Objeto do tipo "Poke_game"

        jogo.imprime_lista_de_pokemons() # Imprime a lista com os nomes

        resposta = input('Já escolheu? [S/N]: ').upper().strip() # Pergunta se o usuário já escolheu o nome

        if resposta == 'S': # Verifca a resposta dada pelo usuário

            system('cls') # Limpa o terminal

            resposta = input(f'Você escolheu o {jogo.pokemon_escolhido}?[S/N]: ').strip().upper() # Pergunta ao se esse ero nome escolhido

            if resposta == 'S': # Se a resposta for afirmativa retorna uma mensagem de felicitação
                print('Que bom eu acertei! (:')
            else:
                print('Que pena eu errei ):') # Se não retorna uma mensagem de tristeza

        flag = input('Quer continuar? [S/N]: ').upper().strip() # Pergunta ao usuário se ele quer continuar com o jogo

        if flag == 'S': # Se sim limpa a tela e continua o jogo
            system('cls')
            continue
        else: # Se não encerra o looping e retorna uma mensagem de agradecimento
            break

    print('Obrigado por jogar!')

if __name__ == '__main__': # Verifica se o contexto de execução é o principal
    main()