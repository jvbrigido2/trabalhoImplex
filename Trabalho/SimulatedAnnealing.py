import numpy
import random
import Grafo

def distanciaSolucao(grafo, solucao):
    distancia = 0
    for i in range(len(solucao) - 1):
        distancia += grafo.distanciaEntreVertices(solucao[i], solucao[i + 1])
    return distancia


def solucaoRandom (grafo):
    cidades = grafo.getTodosIndices().tolist()
    solucao = []

    for i in range(len(grafo.getTodosIndices())):
        cidadeRandom = cidades[random.randint(0, len(cidades) - 1)]
        solucao.append(cidadeRandom)
        cidades.remove(cidadeRandom)

    return solucao


def run(path, TemperaturaMAX, TemperaturaMIN, k, iteracoes):
    grafo = Grafo.criarGrafo(path)

    Temperatura = TemperaturaMAX

    # ponto corrente de forma randomica
    solucao = solucaoRandom(grafo)

    # Simulated Annaeling
    custo_0 = distanciaSolucao(grafo, solucao)

    while Temperatura < TemperaturaMIN:
        Temperatura = 0
        while Temperatura != iteracoes:
            # Troca as coordenadas e pega a solução vizinha
            r1, r2 = numpy.random.randint(0, len(solucao), size=2)

            auxiliar = solucao[r1]
            solucao[r1] = solucao[r2]
            solucao[r2] = auxiliar

            # Pega novo custo
            custo_1 = distanciaSolucao(grafo, solucao)

            if custo_1 < custo_0:
                custo_0 = custo_1
            else:
                x = numpy.random.uniform()
                if x < numpy.exp((custo_0 - custo_1) / Temperatura):
                    custo_0 = custo_1
                else:
                    auxiliar = solucao[r1]
                    solucao[r1] = solucao[r2]
                    solucao[r2] = auxiliar
            Temperatura = Temperatura+1
        Temperatura = k * Temperatura

    return solucao, custo_0