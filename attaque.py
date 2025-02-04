class Attaque:
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
        print("Nom de l'attaque :", self.nom)
        print("Type :", self.type_attaque)
        print("Catégorie :", self.categorie)
        print("Précision :", f"{self.precision}%")
        print("Puissance :", self.puissance)
        print("PP :", self.pp)
