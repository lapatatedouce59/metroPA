import time
import math

def simuler_acceleration(puissance_acceleration, puissance_moteurs, pente):
    masse_train = 1000  # Masse du train en kilogrammes
    coefficient_frottement = 0.1  # Coefficient de frottement du train
    vitesse_initiale = 0  # Vitesse initiale du train en m/s
    distance_parcourue = 0  # Distance parcourue par le train en mètres
    temps_ecoule = 0  # Temps écoulé en secondes

    while vitesse_initiale < 100:  # Simulation jusqu'à une vitesse maximale de 100 m/s
        if vitesse_initiale != 0:
            force_acceleration = puissance_acceleration / vitesse_initiale  # Calcul de la force d'accélération
            force_frottement = coefficient_frottement * vitesse_initiale**2  # Calcul de la force de frottement (proportionnelle au carré de la vitesse)
            force_totale = puissance_moteurs / vitesse_initiale - force_frottement  # Calcul de la force totale (puissance des moteurs - force de frottement)
        else:
            force_acceleration = puissance_acceleration
            force_frottement = 0
            force_totale = puissance_moteurs - force_frottement

        acceleration = force_totale / masse_train - math.sin(math.atan(pente)) * 9.8  # Calcul de l'accélération avec prise en compte de la pente
        vitesse_initiale += acceleration * 1  # Mise à jour de la vitesse avec un intervalle de temps de 1 seconde
        distance_parcourue += vitesse_initiale * 1  # Calcul de la distance parcourue avec un intervalle de temps de 1 seconde
        temps_ecoule += 1  # Incrémentation du temps écoulé de 1 seconde

        print("Vitesse :", vitesse_initiale, "m/s")
        print("Accélération :", acceleration, "m/s^2")
        print("Distance parcourue :", distance_parcourue, "m")
        print("Temps écoulé :", temps_ecoule, "s")
        print("----------------------")

        time.sleep(1)  # Pause de 1 seconde pour simuler l'écoulement du temps

    print("Simulation terminée.")

# Exemple d'utilisation de la fonction
puissance_acceleration = 500000  # Puissance d'accélération du train en watts
puissance_moteurs = 50000  # Puissance continue des moteurs du train en watts
pente = 0.05  # Pente du terrain (5%)
simuler_acceleration(puissance_acceleration, puissance_moteurs, pente)