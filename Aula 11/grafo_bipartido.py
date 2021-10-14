
INCOLOR = -1
VERMELHO = 0
AZUL = 1

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

    def eh_bipartido(self):
        """ Verifica, utilizando bicoloração do conjunto de vértices, de o grafo é bipartido. """
        
        cores = [INCOLOR] * self.vertices
        

    def DFS(self):
        """ Executa a busca em profundidade atribuindo cores aos vértices (vermelho ou azul). """
        pass


if __name__ == "__main__":
    grafo = Grafo(8)
    arestas = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7)]
    
    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()
    print()
    grafo.eh_bipartido()
