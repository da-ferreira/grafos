
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[w].append(u)   

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def pontes(self):
        """ Explicação do algoritmo O(V + E) para detectar pontes em 'Detector de pontes - algoritmo O(V + E).md' """
        pass

    def DFS(self):
        pass


if __name__ == "__main__":
    grafo = Grafo(8)
    arestas = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (5, 7), (6, 7)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()

    print(f"\nPontes do grafo: {grafo.pontes()}")