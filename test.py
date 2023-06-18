import time

def simuler_acceleration(puissance_acceleration):
    masse_train = 1000  # Masse du train en kilogrammes
    coefficient_frottement = 0.1  # Coefficient de frottement du train
    vitesse_initiale = 0  # Vitesse initiale du train en m/s
    distance_parcourue = 0  # Distance parcourue par le train en mètres
    temps_ecoule = 0  # Temps écoulé en secondes

    while vitesse_initiale < 100:  # Simulation jusqu'à une vitesse maximale de 100 m/s
        if vitesse_initiale != 0:
            force_acceleration = puissance_acceleration / vitesse_initiale  # Calcul de la force d'accélération
        else:
            force_acceleration = puissance_acceleration
        
        force_frottement = coefficient_frottement * vitesse_initiale  # Calcul de la force de frottement
        force_totale = force_acceleration - force_frottement  # Calcul de la force totale

        acceleration = force_totale / masse_train  # Calcul de l'accélération
        vitesse_initiale += acceleration * 1  # Mise à jour de la vitesse avec une intervalle de temps de 1 seconde
        distance_parcourue += vitesse_initiale * 1  # Calcul de la distance parcourue avec une intervalle de temps de 1 seconde
        temps_ecoule += 1  # Incrémentation du temps écoulé de 1 seconde

        print("Vitesse :", vitesse_initiale, "m/s")
        print("Distance parcourue :", distance_parcourue, "m")
        print("Temps écoulé :", temps_ecoule, "s")
        print("----------------------")

        time.sleep(1)  # Pause de 1 seconde pour simuler l'écoulement du temps

    print("Simulation terminée.")

# Exemple d'utilisation de la fonction
puissance_acceleration = 5000  # Puissance d'accélération du train en watts
simuler_acceleration(puissance_acceleration)