
class Grafo:
    """ Grafo não orientado utilizando lista de adjacencia. """
    
    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for i in range(self.vertices)]
    
    def inserir(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)
            self.lista_adjacente[w].add(u)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def induzido(self, vertices_induzidos):
        """ 
        Recebe um conjunto de vértices V' que pertence aos
        vértices V do grafo atual e devolve um grafo induzido.
        """

        for vertice in vertices_induzidos:
            if vertice >= self.vertices:
                raise Exception("Não é possível geral o subgrafo induzido")
        
        grafo_induzido = Grafo(self.vertices)

        #for i in range(len(vertices_induzidos)):
        
    
        
        return grafo_induzido


if __name__ == "__main__":
    grafo = Grafo(7)
    arestas = [(0, 1), (0, 5), (0, 6), (1, 2), (1, 6), (2, 3), (2, 6), (3, 4), (3, 6), (4, 5), (4, 6), (5, 6)]
            
    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])        
    