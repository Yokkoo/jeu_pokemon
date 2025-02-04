from rich.console import Console
from rich.table import Table

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
        table.add_column("Pokemons", style="red", justify="center", no_wrap=True)

        table.add_row(self.nom, str(self.mancheGagnee), str(self.argent), str(self.pokemons))

        console.print(table)

aurelien = Joueur("Aurélien", ["Carapuce", "Bulbizarre", "Salameche"])

aurelien.afficher()