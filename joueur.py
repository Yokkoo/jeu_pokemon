from rich.console import Console
from rich.table import Table
from pokemon import Pokemon
from attaque import *

console = Console(width=200)

class Joueur:
    def __init__(self, nom, argent):
        self.nom = nom
        self.argent = argent
        self.pokemons = []

    def afficher(self):
        table = Table(title="Joueur")

        table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
        table.add_column("Argent", style="magenta", justify="center", no_wrap=True)

        table.add_row(self.nom, str(self.argent))

        console.print(table)

    def afficher_pokemons(self):
        table = Table(title="Vos Pokémons")

        table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
        table.add_column("Type 1", style="magenta", justify="center", no_wrap=True)
        table.add_column("Type 2", style="magenta", justify="center", no_wrap=True)
        table.add_column("Point de vie", style="red", justify="center", no_wrap=True)

        for pokemon in self.pokemons:
            table.add_row(pokemon.nom, pokemon.type1, pokemon.type2, str(pokemon.point_de_vie))

        console.print(table)

    def ajouter_pokemon(self, pokemon):
        pokemon.proprietaire = self.nom
        self.pokemons.append(pokemon)

    def acheter_pokemon(self, pokemons_disponibles):
        while len(self.pokemons) < 3:
            table = Table(title="Pokémons disponibles")

            table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
            table.add_column("Prix", style="green", justify="center", no_wrap=True)
            table.add_column("Type 1", style="magenta", justify="center", no_wrap=True)
            table.add_column("Type 2", style="magenta", justify="center", no_wrap=True)

            for pokemon in pokemons_disponibles:
                table.add_row(pokemon.nom, str(pokemon.prix), pokemon.type1, pokemon.type2)

            console.print(table)

            choix = input("Choisissez votre Pokemon : ")
            for pokemon in pokemons_disponibles:
                if pokemon.nom == choix and self.argent >= pokemon.prix:
                    self.ajouter_pokemon(pokemon)
                    self.argent -= pokemon.prix
                    print(f"Vous avez acheté {choix} pour {pokemon.prix}$. Il vous reste {self.argent}$.")
                    break
            else:
                console.print("Le Pokemon n'existe pas ou vous n'avez pas assez d'argent.", style="red")

    def recuperer_pokemon(self):
        if not self.pokemons:
            console.print("Vous n'avez aucun Pokémon.", style="red")
            return None

        self.afficher_pokemons()

        choix = input("Choisissez un Pokémon : ")

        for pokemon in self.pokemons:
            if pokemon.nom == choix:
                return pokemon

        console.print("Le Pokémon n'existe pas.", style="red")
        return None


