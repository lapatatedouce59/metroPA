import math

def simulation_acceleration(degre_traction, puissance_moteurs, poids_rame, pourcentage_pente, duree):
    masse_train = poids_rame / 9.8  # Conversion du poids de la rame en masse du train
    coefficient_frottement = 0.1  # Coefficient de frottement du train

    angle_pente_rad = math.atan(pourcentage_pente / 100)  # Conversion du pourcentage de pente en angle en radians

    force_frottement = coefficient_frottement * masse_train * 9.8 * math.cos(angle_pente_rad)  # Calcul de la force de frottement
    force_traction = degre_traction * puissance_moteurs / 100  # Calcul de la force de traction

    acceleration = (force_traction - force_frottement) / masse_train

    vitesse_initiale = 0  # Vitesse initiale du train
    distance_parcourue = 0  # Distance parcourue par le train

    temps = 0
    temps_echantillonnage = 1  # Intervalle de temps pour l'échantillonnage (en secondes)
    acceleration_echantillonnage = []  # Liste pour stocker les valeurs d'accélération
    vitesse_echantillonnage = []  # Liste pour stocker les valeurs de vitesse
    distance_echantillonnage = []  # Liste pour stocker les valeurs de distance

    while temps <= duree:
        acceleration_echantillonnage.append(acceleration)
        vitesse = vitesse_initiale + (acceleration * temps_echantillonnage)
        vitesse_echantillonnage.append(vitesse)
        distance = distance_parcourue + (vitesse * temps_echantillonnage)
        distance_echantillonnage.append(distance)

        print(f"Temps: {temps}s, Accélération: {acceleration} m/s², Vitesse: {vitesse} m/s, Distance: {distance} m")

        temps += temps_echantillonnage

    return acceleration_echantillonnage, vitesse_echantillonnage, distance_echantillonnage

simulation_acceleration(3,2000000,1411200,0,50)