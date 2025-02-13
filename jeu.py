import joueur
from rich.console import Console

console = Console(width=200)

class Jeu:
    joueurs = []

    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def jouer(self):
        # Initialisation des joueurs
        joueur1 = joueur.Joueur("Joueur 1", [])
        joueur2 = joueur.Joueur("Joueur 2", [])

        self.ajouter_joueur(joueur1)
        self.ajouter_joueur(joueur2)

        # Choix des Pokémons pour chaque joueur
        console.print("Joueur 1, choisissez vos Pokémons :")
        joueur1.choisir_pokemon()
        console.print("Joueur 2, choisissez vos Pokémons :")
        joueur2.choisir_pokemon()

        # Boucle de jeu
        while True:
            for joueur_actuel in self.joueurs:
                console.print(f"{joueur_actuel.nom}, c'est votre tour.")
                pokemon_attaquant = None
                while not pokemon_attaquant:
                    pokemon_attaquant = joueur_actuel.recuperer_pokemon()
                
                adversaire = self.joueurs[1] if joueur_actuel == self.joueurs[0] else self.joueurs[0]
                pokemon_defenseur = None
                while not pokemon_defenseur:
                    pokemon_defenseur = adversaire.recuperer_pokemon()

                if pokemon_attaquant and pokemon_defenseur:
                    while True:
                        noms_attaques = [attaque.nom for attaque in pokemon_attaquant.attaques]
                        attaque_choisie = input(f"Choisissez une attaque parmi {noms_attaques}: ")
                        attaque = next((a for a in pokemon_attaquant.attaques if a.nom == attaque_choisie), None)
                        if attaque:
                            degats = pokemon_attaquant.attaquer(attaque, pokemon_defenseur)
                            console.print(f"{pokemon_attaquant.nom} utilise {attaque.nom} et inflige {degats} dégâts à {pokemon_defenseur.nom}.")
                            if pokemon_defenseur.est_ko():
                                console.print(f"{pokemon_defenseur.nom} est KO!")
                                adversaire.pokemons.remove(pokemon_defenseur)
                                if not adversaire.pokemons:
                                    console.print(f"{joueur_actuel.nom} a gagné!")
                                    return
                            break
                        else:
                            console.print("Attaque non valide.", style="red")
                else:
                    console.print("Pokémon non valide.", style="red")



