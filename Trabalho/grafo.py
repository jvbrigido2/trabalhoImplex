import numpy as np
import math

def gerarVector(path):
    with open(path) as v_input:
        text = [" ".join(l.split()) for l in v_input]
        
    vector = np.loadtxt(text, dtype=float, delimiter="").astype(int)
    
    return vector

def criarGrafo(path):
    vector = gerarVector(path)
    
    grafo = Grafo(vector)
    
    return grafo

class Grafo:
    def __init__(self , vector):
        self.vector = vector
        
    
    def distanciaEntreVertices(self, v1, v2):
        coordV1 = [self.vector [v1 - 1] [1], self.vector[v1 - 1] [2]]
        coordV2 = [self.vector [v2 - 1] [1], self.vector[v2 - 1] [2]]
        distancia_euclidiana = math.sqrt(
            ((coordV1[0] - coordV2[0]) ** 2) + ((coordV1[1] - coordV2[1]) ** 2)
        )
        return distancia_euclidiana
    
    def getVerticeCoord(self, vertice):
        resultado = []
        for x_coord in range(vertice):
            for y_coord in range(vertice):
                resultado.append(x_coord , y_coord)
        
        return resultado
    
    def getTodosIndices(self):
        return self.vector[:, 0]

