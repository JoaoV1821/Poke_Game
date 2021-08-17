from random import choice # Importa a função choice da biblioteca random

class Poke_game:
    def __init__(self):
        self.__lista_pokemons = self.__extrai_do_arquivo() # Lista com os pokemóns 
        self.__pokemon_escolhido = self.__escolhe_pokemon(self.__lista_pokemons[0]) # pokemón escolhido
    

    def __escolhe_pokemon(self, lista_de_pokemons): # Método que sorteia o pokemón na lista de pokemóns
        pokemon_escolhido = choice(lista_de_pokemons) # Sorteia um nome na lisa
        return pokemon_escolhido
    

    def __extrai_do_arquivo(self): # Método que extrai do arquivo "pokemon_names.txt" os nomes dos pokemóns até o 100º
        lista_pokemons = []

        for i in range(1, 101): 
            with open('pokemon_names.txt', mode='r', encoding='UTF-8') as arquivo:
                lista_pokemons.append(arquivo.readlines()) # Adiciona o nome na lista por linha 
        return lista_pokemons
    

    def imprime_lista_de_pokemons(self): # Método que imprime todos os nomes da lista
         for i in range(1, 101):
            print(f'{i}- {self.__lista_pokemons[0][i]}')
    

    @property # Getter do pokemón sorteado
    def pokemon_escolhido(self):
        return self.__pokemon_escolhido.replace('\n', '') # Retira a quebra de linha do nome
