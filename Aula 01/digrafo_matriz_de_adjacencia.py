
# 1. Construa uma classe Digrafo para representar o grafo orientado utilizando a matriz de adjacência.

class Digrafo:
    def __init__(self, vertices):
        self.vertices = vertices + 1
        self.arestas = 0
        self.matriz_adjacente = [[0] * self.vertices for i in range(self.vertices)]

    def insere(self, u, w):
        self.matriz_adjacente[u][w] = 1
        self.arestas += 1

    def remove(self, u, w):
        self.matriz_adjacente[u][w] = 0
        self.arestas -= 1

    def grau_entrada(self, vertice):
        grau = 0

        for linha in self.matriz_adjacente:
            if linha[vertice] == 1:
                grau += 1
        
        return grau

    def grau_saida(self, vertice):
        return self.matriz_adjacente[vertice].count(1)  # Grau

    def mostra(self):
        print("Vértices com suas respectivas arestas orientadas")

        for i in range(1, self.vertices):
            print(f"{i}: ", end='')

            for j in range(1, self.vertices):
                if self.matriz_adjacente[i][j] == 1:
                    print(f"{j} ", end='')

            print()
    

if __name__ == "__main__":
    grafo_orientado = Digrafo(4)
    arestas = [(1, 2), (1, 3), (3, 2), (2, 4), (4, 3), (2, 2)]

    for aresta in arestas:
        grafo_orientado.insere(aresta[0], aresta[1])

    #grafo_orientado.mostra()

    print(f"Grau de entrada do vértice 2: {grafo_orientado.grau_entrada(2)}")
    print(f"Grau de saida do vértice 2: {grafo_orientado.grau_saida(2)}")

    # graus_de_entrada = [grafo_orientado.grau_entrada(1), grafo_orientado.grau_entrada(2), 
    #                     grafo_orientado.grau_entrada(3), grafo_orientado.grau_entrada(4)]

    # graus_de_saida = [grafo_orientado.grau_saida(1), grafo_orientado.grau_saida(2), 
    #                   grafo_orientado.grau_saida(3),grafo_orientado.grau_saida(4)]
    
    # print(f"Graus de entradas: {graus_de_entrada}")
    # print(f"Graus de saidas: {graus_de_saida}")
    