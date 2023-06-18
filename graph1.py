import numpy as np
import matplotlib.pyplot as plt

def courbe_acceleration(t, t0, t1, a_max):
    """
    Fonction de courbe d'accélération réaliste d'un train.

    Arguments :
    - t : Temps (array ou valeur) où l'accélération est calculée.
    - t0 : Temps de début de l'accélération (temps de transition).
    - t1 : Temps de fin de l'accélération (temps de stabilisation).
    - a_max : Accélération maximale atteinte par le train.

    Retourne :
    - Accélération du train au temps t.
    """

    # Calcul des paramètres de la courbe sigmoidale
    k = 10 / (t1 - t0)
    c = -k * t0

    # Calcul de l'accélération en utilisant la fonction sigmoidale
    acceleration = a_max / (1 + np.exp(-k * t + c))

    return acceleration

# Exemple d'utilisation de la fonction pour tracer la courbe d'accélération
t = np.linspace(0, 30, 100)  # Temps de 0 à 30 secondes
t0 = 5  # Temps de début de l'accélération (temps de transition)
t1 = 15  # Temps de fin de l'accélération (temps de stabilisation)
a_max = 5  # Accélération maximale atteinte par le train

acceleration = courbe_acceleration(t, t0, t1, a_max)

plt.plot(t, acceleration)
plt.xlabel('Temps (s)')
plt.ylabel('Accélération (m/s^2)')
plt.title('Courbe d\'accélération réaliste d\'un train')
plt.grid(True)
plt.show()