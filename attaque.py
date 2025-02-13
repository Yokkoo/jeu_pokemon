from rich.console import Console
from rich.table import Table

console = Console(width=200)

class Attaque:
    nom = ""
    type_attaque = ""
    categorie = ""
    precision = 0
    puissance = 0
    pp = 0

    def __init__(self, nom, type_attaque, categorie, precision, puissance, pp):
        self.nom = nom
        self.type_attaque = type_attaque
        self.categorie = categorie
        self.precision = precision
        self.puissance = puissance
        self.pp = pp

    def calculer_degats(self, attaquant, defenseur):
        if self.categorie.lower() == "physique":
            stat_attaquant = attaquant.attaque
            stat_defenseur = defenseur.defense
        elif self.categorie.lower() == "speciale":
            stat_attaquant = attaquant.attaque_speciale
            stat_defenseur = defenseur.defense_speciale
        else:
            stat_attaquant = attaquant.attaque
            stat_defenseur = defenseur.defense

        if self.type_attaque in [attaquant.type1, attaquant.type2]:
            coef_stab = 1.5
        else:
            coef_stab = 1

        coef_precision = self.precision / 100

        degats = (((attaquant.niveau * 0.4 + 2) * stat_attaquant * self.puissance) /
                  (stat_defenseur * 50) + 2)

        degats *= coef_stab * coef_precision

        return int(degats)

    def afficher(self):
        table = Table(title="Attaque")

        table.add_column("Nom", style="cyan", justify="center", no_wrap=True)
        table.add_column("Type", style="green", justify="center", no_wrap=True)
        table.add_column("Catégorie", style="magenta", justify="center", no_wrap=True)
        table.add_column("Précision", style="red", justify="center", no_wrap=True)
        table.add_column("Puissance", style="yellow", justify="center", no_wrap=True)
        table.add_column("PP", style="blue", justify="center", no_wrap=True)

        table.add_row(self.nom, self.type_attaque, self.categorie, str(self.precision), str(self.puissance), str(self.pp))

        console.print(table)

# Définir toutes les attaques mentionnées
eclair = Attaque("Éclair", "électrique", "speciale", 100, 40, 30)
vive_attaque = Attaque("Vive-attaque", "normal", "physique", 100, 40, 30)
tonnerre = Attaque("Tonnerre", "électrique", "speciale", 100, 90, 15)
fatal_foudre = Attaque("Fatal-foudre", "électrique", "speciale", 70, 110, 10)
charge = Attaque("Charge", "normal", "physique", 100, 40, 35)
pistolet_a_o = Attaque("Pistolet à O", "eau", "speciale", 100, 40, 25)
morsure = Attaque("Morsure", "tenebres", "physique", 100, 60, 25)
ecume = Attaque("Ecume", "eau", "speciale", 100, 20, 30)
tranch_herbe = Attaque("Tranch'Herbe", "plante", "physique", 95, 55, 25)
fouet_lianes = Attaque("Fouet Lianes", "plante", "physique", 100, 45, 25)
vampigraine = Attaque("Vampigraine", "plante", "status", 90, 0, 10)
griffe = Attaque("Griffe", "normal", "physique", 100, 40, 35)
flammeche = Attaque("Flammeche", "feu", "speciale", 100, 40, 25)
groz_yeux = Attaque("Groz'Yeux", "normal", "status", 100, 0, 30)
rugissement = Attaque("Rugissement", "normal", "status", 100, 0, 40)
teleport = Attaque("Teleport", "psy", "status", 100, 0, 20)
saisie = Attaque("Saisie", "normal", "physique", 100, 40, 30)
choc_mental = Attaque("Choc Mental", "psy", "speciale", 100, 50, 25)
ecras_face = Attaque("Ecras'Face", "normal", "physique", 100, 50, 35)
poing_karate = Attaque("Poing-Karaté", "combat", "physique", 100, 50, 25)
balayage = Attaque("Balayage", "combat", "physique", 100, 50, 20)
frappe_atlas = Attaque("Frappe Atlas", "combat", "physique", 100, 50, 20)
dynamopoing = Attaque("Dynamopoing", "combat", "physique", 50, 100, 5)
lance_flamme = Attaque("Lance-flamme", "feu", "speciale", 100, 90, 15)
tranche = Attaque("Tranche", "normal", "physique", 100, 70, 20)
