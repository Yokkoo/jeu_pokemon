from rich.console import Console
from rich.table import Table
from pokemon import Pokemon

console = Console(width=200)

class Joueur:
    nom = ""
    mancheGagnee = 0
    argent = 1500
    pokemons = []

    def __init__(self, nom, pokemons):
        self.nom = nom
        self.pokemons = pokemons

    def afficher(self):
        table = Table(title="Joueur")

        table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
        table.add_column("Manche gagnée", style="green", justify="center", no_wrap=True)
        table.add_column("Argent", style="magenta", justify="center", no_wrap=True)

        table.add_row(self.nom, str(self.mancheGagnee), str(self.argent))

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
        self.pokemons.append(pokemon)

    def choisir_pokemon(self):
        pokemons_disponibles = [
            Pokemon("Carapuce", 0, "Eau", "", 44, 5, 48, 50, 65, 64, 43, [charge, pistolet_a_o, morsure, ecume]),
            Pokemon("Bulbizarre", 0, "Plante", "Poison", 45, 5, 49, 65, 49, 65, 45, [charge, tranch_herbe, fouet_lianes, vampigraine]),
            Pokemon("Salameche", 0, "Feu", "", 39, 5, 52, 60, 43, 50, 65, [griffe, flammeche, groz_yeux, rugissement]),
            Pokemon("Mystherbe", 0, "Plante", "Poison", 30, 5, 35, 40, 30, 45, 55, [charge, tranch_herbe, fouet_lianes, vampigraine]),
            Pokemon("Abra", 0, "Psy", "", 25, 5, 20, 105, 15, 55, 90, [teleport, saisie, choc_mental, ecras_face]),
            Pokemon("Machoc", 0, "Combat", "", 70, 5, 80, 35, 50, 35, 35, [poing_karate, balayage, frappe_atlas, dynamopoing])
        ]

        table = Table(title="Pokemons disponibles")

        table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
        table.add_column("Prix", style="green", justify="center", no_wrap=True)
        table.add_column("Type 1", style="magenta", justify="center", no_wrap=True)
        table.add_column("Type 2", style="magenta", justify="center", no_wrap=True)

        for pokemon in pokemons_disponibles:
            table.add_row(pokemon.nom, str(pokemon.prix), pokemon.type1, pokemon.type2)

        console.print(table)

        for i in range(3):
            choix = input("Choisissez votre Pokemon (Carapuce, Bulbizarre, Salameche, Mystherbe, Abra, Machoc) : ")

            if choix in ["Carapuce", "Bulbizarre", "Salameche", "Mystherbe", "Abra", "Machoc"]:
                for pokemon in pokemons_disponibles:
                    if pokemon.nom == choix:
                        self.ajouter_pokemon(pokemon)
                        print("Vous avez choisi " + choix)
                    else:
                        console.print("Le Pokemon n'existe pas", style="red")
            else:
                console.print("Le Pokemon n'existe pas", style="red")

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


