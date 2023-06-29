import Grafo
import random

def solucaoRandom(grafo):
    cities = grafo.getTodosIndices().tolist()
    solucao = []

    for i in range(len(grafo.getTodosIndices())):
        randomCity = random.choice(cities)
        solucao.append(randomCity)
        cities.remove(randomCity)

    return solucao


def distanciaSolucao(grafo, solucao):
    distancia = 0
    for i in range(len(solucao) - 1):
        distancia += grafo.distanciaEntreVertices(solucao[i], solucao[i+1])
    return distancia


def getVizinhos(solucao):
    vizinhos = []
    for i in range(len(solucao)):
        for j in range(i+1, len(solucao)):
            vizinho = solucao.copy()
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos


def getMelhorVizinho(grafo, vizinhos):
    melhorRota = distanciaSolucao(grafo, vizinhos[0])
    melhorVizinho = vizinhos[0]
    for vizinho in vizinhos:
        rotaAtual = distanciaSolucao(grafo, vizinho)
        if rotaAtual < melhorRota:
            melhorRota = rotaAtual
            melhorVizinho = vizinho
    return melhorVizinho, melhorRota


def run(path):
    grafo = Grafo.criarGrafo(path)

    solucao = solucaoRandom(grafo)
    distancia = distanciaSolucao(grafo, solucao)
    vizinhos = getVizinhos(solucao)
    melhorVizinho, melhorDistanciaVizinho = getMelhorVizinho(grafo, vizinhos)

    while melhorDistanciaVizinho < distancia:
        solucao = melhorVizinho
        distancia = melhorDistanciaVizinho
        vizinhos = getVizinhos(solucao)
        melhorVizinho, melhorDistanciaVizinho = getMelhorVizinho(grafo, vizinhos)

    return solucao, distancia
  
