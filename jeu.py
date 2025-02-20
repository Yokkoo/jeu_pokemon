import joueur
from rich.console import Console
from pokemon import Pokemon
from attaque import *

console = Console(width=200)

class Jeu:
    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def jouer(self):
        try:
            # Initialisation des joueurs
            console.print("Joueur 1, entrez votre nom :")
            nom_joueur1 = input()
            joueur1 = joueur.Joueur(nom_joueur1, 1800)
            self.ajouter_joueur(joueur1)

            console.print("Joueur 1, choisissez vos Pokémons :")
            joueur1.acheter_pokemon(self.pokemons_disponibles())

            console.print("Joueur 2, entrez votre nom :")
            nom_joueur2 = input()
            joueur2 = joueur.Joueur(nom_joueur2, 1800)
            self.ajouter_joueur(joueur2)

            console.print("Joueur 2, choisissez vos Pokémons :")
            joueur2.acheter_pokemon(self.pokemons_disponibles())

            # Boucle de jeu
            manches_gagnees = {joueur1.nom: 0, joueur2.nom: 0}
            for i in range(3):
                console.print(f"Round {i+1}")
                pokemon1 = joueur1.pokemons[i]
                pokemon2 = joueur2.pokemons[i]

                while not pokemon1.est_ko() and not pokemon2.est_ko():
                    if pokemon1.vitesse >= pokemon2.vitesse:
                        if not self.tour(pokemon1, pokemon2):
                            continue
                        if pokemon2.est_ko():
                            manches_gagnees[joueur1.nom] += 1
                            break
                        if not self.tour(pokemon2, pokemon1):
                            continue
                        if pokemon1.est_ko():
                            manches_gagnees[joueur2.nom] += 1
                            break
                    else:
                        if not self.tour(pokemon2, pokemon1):
                            continue
                        if pokemon1.est_ko():
                            manches_gagnees[joueur2.nom] += 1
                            break
                        if not self.tour(pokemon1, pokemon2):
                            continue
                        if pokemon2.est_ko():
                            manches_gagnees[joueur1.nom] += 1
                            break

            if manches_gagnees[joueur1.nom] > manches_gagnees[joueur2.nom]:
                console.print(f"{joueur1.nom} a gagné!")
            else:
                console.print(f"{joueur2.nom} a gagné!")
        except KeyboardInterrupt:
            console.print("\nLe jeu a été interrompu par l'utilisateur.", style="red")

    def tour(self, attaquant, defenseur):
        noms_attaques = [attaque.nom for attaque in attaquant.attaques]
        attaque_choisie = input(f"{attaquant.nom} ({attaquant.proprietaire}), choisissez une attaque parmi {noms_attaques}: ")
        attaque = next((a for a in attaquant.attaques if a.nom == attaque_choisie), None)
        if attaque:
            degats = attaquant.attaquer(attaque, defenseur)
            console.print(f"{attaquant.nom} ({attaquant.proprietaire}) utilise {attaque.nom} et inflige {degats} dégâts à {defenseur.nom} ({defenseur.proprietaire}).")
            console.print(f"{defenseur.nom} ({defenseur.proprietaire}) a maintenant {defenseur.point_de_vie} points de vie restants.")
            if defenseur.est_ko():
                console.print(f"{defenseur.nom} ({defenseur.proprietaire}) est KO!")
            return True
        else:
            console.print("Attaque non valide.", style="red")
            return False

    def pokemons_disponibles(self):
        return [
            Pokemon("Carapuce", 500, "Eau", "", 44, 5, 48, 50, 65, 64, 43, [charge, pistolet_a_o, morsure, ecume]),
            Pokemon("Bulbizarre", 600, "Plante", "Poison", 45, 5, 49, 65, 49, 65, 45, [charge, tranch_herbe, fouet_lianes, vampigraine]),
            Pokemon("Salameche", 700, "Feu", "", 39, 5, 52, 60, 43, 50, 65, [griffe, flammeche, groz_yeux, rugissement]),
            Pokemon("Mystherbe", 400, "Plante", "Poison", 30, 5, 35, 40, 30, 45, 55, [charge, tranch_herbe, fouet_lianes, vampigraine]),
            Pokemon("Abra", 800, "Psy", "", 25, 5, 20, 105, 15, 55, 90, [teleport, saisie, choc_mental, ecras_face]),
            Pokemon("Machoc", 550, "Combat", "", 70, 5, 80, 35, 50, 35, 35, [poing_karate, balayage, frappe_atlas, dynamopoing])
        ]



