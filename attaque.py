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
        """
        Initialise une attaque avec :
          - nom : nom de l'attaque (str)
          - type_attaque : type de l'attaque (ex : "feu", "eau", etc.) (str)
          - categorie : "physique" ou "speciale" (str)
          - precision : pourcentage de précision (ex : 100 pour 100%) (int)
          - puissance : puissance de base de l'attaque (int)
          - pp : nombre de fois que l'attaque peut être utilisée (int)
        """
        self.nom = nom
        self.type_attaque = type_attaque
        self.categorie = categorie  # "physique" ou "speciale"
        self.precision = precision  # en pourcentage
        self.puissance = puissance
        self.pp = pp

    def calculer_degats(self, attaquant, defenseur):
        """
        Calcule les dégâts occasionnés par l'attaque.

        Paramètres :
          - attaquant : le Pokémon qui attaque.
                       On suppose qu'il possède au moins les attributs :
                         - niveau (int)
                         - attaque (int) et attaque_special (int)
                         - types (liste de str) qui contient ses types (ex : ["feu"] ou ["eau", "vol"])
          - defenseur : le Pokémon qui est attaqué.
                        On suppose qu'il possède au moins les attributs :
                          - defense (int) et defense_special (int)
        
        La formule utilisée est la suivante :
          (((niveau * 0.4 + 2) * stat_attaquant * puissance) / (stat_defenseur * 50) + 2)
              * coef_stab * (precision / 100)

        Où :
          - stat_attaquant et stat_defenseur dépendent de la catégorie de l'attaque
          - coef_stab est égal à 1.5 si le type de l'attaque est présent dans attaquant.types, sinon 1
          - precision est utilisée comme un coefficient (ex : 100% donne 1)
        
        Retourne :
          - Les dégâts calculés (int).
        """
        # Choisir les stats selon la catégorie de l'attaque
        if self.categorie.lower() == "physique":
            stat_attaquant = attaquant.attaque
            stat_defenseur = defenseur.defense
        elif self.categorie.lower() == "speciale":
            stat_attaquant = attaquant.attaque_special
            stat_defenseur = defenseur.defense_special
        else:
            # Par défaut, on prend l'attaque physique
            stat_attaquant = attaquant.attaque
            stat_defenseur = defenseur.defense

        # Calcul du STAB : si le type de l'attaque correspond à l'un des types du Pokémon attaquant,
        # alors on applique un bonus de 1.5, sinon 1.
        if self.type_attaque in attaquant.types:
            coef_stab = 1.5
        else:
            coef_stab = 1

        # Coefficient de précision (par exemple, 100% = 1)
        coef_precision = self.precision / 100

        # Calcul de base des dégâts
        degats = (((attaquant.niveau * 0.4 + 2) * stat_attaquant * self.puissance) /
                  (stat_defenseur * 50) + 2)

        # Application des coefficients STAB et précision
        degats *= coef_stab * coef_precision

        # On peut arrondir ou convertir en entier
        return int(degats)

    def afficher(self):
        """
        Affiche les informations de l'attaque.
        """
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
