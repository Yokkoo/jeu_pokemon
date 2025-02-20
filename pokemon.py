from rich.console import Console
from rich.table import Table
from attaque import *

console = Console(width=200)

class Pokemon:
    nom = ""
    prix = 0
    type1 = ""
    type2 = ""
    point_de_vie = 0
    niveau = 0
    attaque = 0
    attaque_speciale = 0
    defense = 0
    defense_speciale = 0
    vitesse = 0
    attaques = []
    proprietaire = None

    def __init__(self, nom, prix, type1, type2, point_de_vie, niveau, attaque, attaque_speciale, defense, defense_speciale, vitesse, attaques, proprietaire=None):
        self.nom = nom
        self.prix = prix
        self.type1 = type1
        self.type2 = type2
        self.point_de_vie = point_de_vie
        self.niveau = niveau
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale
        self.defense = defense
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.attaques = attaques
        self.proprietaire = proprietaire

    def afficher(self):
        table = Table(title="Pokemon")

        table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
        table.add_column("Prix", style="green", justify="center", no_wrap=True)
        table.add_column("Type 1", style="magenta", justify="center", no_wrap=True)
        table.add_column("Type 2", style="magenta", justify="center", no_wrap=True)
        table.add_column("Point de vie", style="red", justify="center", no_wrap=True)
        table.add_column("Niveau", style="blue", justify="center", no_wrap=True)
        table.add_column("Propriétaire", style="yellow", justify="center", no_wrap=True)

        table.add_row(self.nom, str(self.prix), self.type1, self.type2, str(self.point_de_vie), str(self.niveau), self.proprietaire)

        console.print(table)

    def afficher_attaques(self):
        table = Table(title="Attaques")

        table.add_column("Attaque", style="cyan", justify="center", no_wrap=True)
        table.add_column("Attaque Spéciale", style="green", justify="center", no_wrap=True)
        table.add_column("Defense", style="magenta", justify="center", no_wrap=True)
        table.add_column("Defense Spéciale", style="red", justify="center", no_wrap=True)
        table.add_column("Vitesse", style="blue", justify="center", no_wrap=True)

        table.add_row(str(self.attaque), str(self.attaque_speciale), str(self.defense), str(self.defense_speciale), str(self.vitesse))

        console.print(table)

    def est_ko(self):
        return self.point_de_vie <= 0

    def ajouter_attaque(self, attaque):
        self.attaques.append(attaque)

    def attaquer(self, attaque, adversaire):
        degats = attaque.calculer_degats(self, adversaire)
        adversaire.point_de_vie -= degats
        return degats