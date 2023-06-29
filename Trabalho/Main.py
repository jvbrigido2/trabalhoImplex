import HillClimbing as HC
import SimulatedAnnealing as SA

if __name__ == "__main__":
    paths = ["Data/att48.tsp.txt",
             "Data/berlin52.tsp.txt",
             "Data/bier127.tsp.txt",
             "Data/eil76.tsp.txt",
             "Data/kroA100.tsp.txt",
             "Data/kroE100.tsp.txt",
             "Data/pr76.tsp.txt",
             "Data/rat99.tsp.txt",
             "Data/st70.tsp.txt"]

    print('Por favor entre com os parametros para o algoritmo Simulated Annealing')
    Tmax = int(input('Temperatura inicial: '))
    Tmin = int(input('Temperatura final: '))
    k = float(input('Razão de resfriamento: '))
    iteracoes = int(input('Quantidade de iterações: '))

    for path in paths:
        print('----------------------------------------')
        print('File ' + path)
        solution, iteracoes = SA.run(path, Tmax, Tmin, k, iteracoes)
        print('SA Distance = ' + str(iteracoes))
        print('SA Solution = ' + str(solution))
        solution, iteracoes = HC.run(path)
        print('HC Distance = ' + str(iteracoes))
        print('HC Solution = ' + str(solution))
    print('----------------------------------------')
