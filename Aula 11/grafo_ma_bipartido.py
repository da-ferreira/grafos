
INCOLOR = -1
VERMELHO = 0
AZUL = 1

class Grafo:
    """ Grafo utilizando matriz de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.matriz_adjacente = [[0] * self.vertices for _ in range(self.vertices)]

    def inserir(self, u, w):
        self.matriz_adjacente[u][w] = 1
        self.matriz_adjacente[w][u] = 1

    def mostrar(self):
        for i in range(len(self.matriz_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.matriz_adjacente[i])}")

    def eh_bipartido(self):
        """ 
        Verifica, utilizando bicoloração do conjunto de vértices, se o grafo é bipartido.
        Atribui-se cores a cada vértice de tal modo que dois vértices adjacentes não tenham
        a mesma cor. Se isso acontecer o grafo é bipartido.
        """
        
        cores = [INCOLOR] * self.vertices
        vertices_vermelhos = []
        vertices_azuis = []

        if self.DFS(0, VERMELHO, cores):  # Começa pelo vértice 0 pela cor vermelha
            [vertices_vermelhos.append(v) if cores[v] == VERMELHO else vertices_azuis.append(v) for v in range(self.vertices)]
            return (True, vertices_vermelhos, vertices_azuis)
        else:
            return (False, vertices_vermelhos, vertices_azuis)

    def adjacente(self, vertice):
        """ Retorna todos os vértices adjacentes ao vértice passado no parametro. """
        return [x for x in range(len(self.matriz_adjacente[vertice])) if self.matriz_adjacente[vertice][x] != 0]

    def DFS(self, vertice, cor, cores):
        """ Executa a busca em profundidade atribuindo cores aos vértices (vermelho ou azul). """
        cores[vertice] = cor

        for u in self.adjacente(vertice):
            if cores[u] == INCOLOR:
                if self.DFS(u, cor ^ 1, cores) == False:  # A cor varia em [0, 1], a operação ^ 1 alterna entre 0 e 1.
                    return False
            elif cores[vertice] == cores[u]:
                return False
        
        return True


if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])
    
    grafo.mostrar()
    print()
    print(f"O grafo é bipartido? {grafo.eh_bipartido()}")

