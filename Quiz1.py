import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

def generar_puntos_3d(num_puntos, limite_superior):
    puntos = np.random.rand(num_puntos, 3) * limite_superior
    return puntos

def graficar_puntos_3d(puntos):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(puntos[:,0], puntos[:,1], puntos[:,2], marker='o')
    ax.set_xlabel('Coordenada X')
    ax.set_ylabel('Coordenada Y')
    ax.set_zlabel('Coordenada Z')
    ax.set_title('Conjunto de puntos aleatorios en 3D')
    plt.show()

def graficar_convex_hull_3d(puntos, convex_hull):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(puntos[:,0], puntos[:,1], puntos[:,2], marker='o')
    for simplex in convex_hull.simplices:
        simplex = np.append(simplex, simplex[0])  # Completa el ciclo
        ax.plot(puntos[simplex, 0], puntos[simplex, 1], puntos[simplex, 2], 'k-')
    ax.set_xlabel('Coordenada X')
    ax.set_ylabel('Coordenada Y')
    ax.set_zlabel('Coordenada Z')
    ax.set_title('Envoltura convexa del conjunto de puntos en 3D')
    plt.show()
