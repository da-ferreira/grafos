
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    tempo = 0
    INFINITO = float("inf")

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
        
        Grafo.tempo = 0
        pre = [-1] * self.vertices
        low = [Grafo.INFINITO] * self.vertices
        pai = [-1] * self.vertices

        for vertice in range(self.vertices):
            if pre[vertice] == -1:
                pai[vertice] = vertice
                self.DFS(vertice, pre, low, pai)

    def DFS(self, v, pre, low, pai):
        Grafo.tempo += 1
        pre[v] = Grafo.tempo
        low[v] = Grafo.tempo

        for w in self.lista_adjacente[v]:
            if pre[w] == -1:
                pai[w] = v
                self.DFS(w, pre, low, pai)

                low[v] = min(low[v], low[w])

                if low[w] > pre[v]:  # ou low[w] == pre[w]
                    print(f"Há uma ponte em ({v}, {w})")

            elif w != pai[v]:
                low[v] = min(low[v], pre[w])


if __name__ == "__main__":
    grafo = Grafo(8)
    arestas = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (5, 7), (6, 7)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()

    print("\nPontes do grafo:")
    grafo.pontes()
      