
class Grafo:
    """ Grafo não orientado utilizando lista de adjacencia. """
    
    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for i in range(self.vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].add(w)
        self.lista_adjacente[w].add(u)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def eh_subgrafo(self, grafo_g1):
        """ Recebe um grafo e devolve True caso o grafo seja um subgrafo do grafo atual. """
        
        if grafo_g1.vertices <= self.vertices:
            for vertice in range(grafo_g1.vertices):
                for w in grafo_g1.lista_adjacente[vertice]:
                    if w not in self.lista_adjacente[vertice]:
                        return False
            
            return True
        
        return False

    def eh_subgrafo_gerador(self, grafo_g1):
        """ Recebe um grafo e devolve True caso o grafo seja um subgrafo gerador do grafo atual. """
        
        if grafo_g1.vertices == self.vertices:
            for vertice in range(grafo_g1.vertices):
                for w in grafo_g1.lista_adjacente[vertice]:
                    if w not in self.lista_adjacente[vertice]:
                        return False
            
            return True
        
        return False


if __name__ == "__main__":
    grafo_g = Grafo(7)
    arestas_g = [(0, 1), (0, 5), (0, 6), (1, 2), (1, 6), (2, 3), (2, 6), (3, 4), (3, 6), (4, 5), (4, 6), (5, 6)]
            
    for aresta in arestas_g:
        grafo_g.inserir(aresta[0], aresta[1])

    grafo_g1 = Grafo(6)
    arestas_g1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]

    for aresta in arestas_g1:
        grafo_g1.inserir(aresta[0], aresta[1])

    grafo_g2 = Grafo(6)
    arestas_g2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (1, 4)]

    for aresta in arestas_g2:
        grafo_g2.inserir(aresta[0], aresta[1])

    print("Grafo G")
    grafo_g.mostrar()
    
    print('-' * 20)
    
    print("Grafo G'1")
    grafo_g1.mostrar()

    print('-' * 20)

    print("Grafo G'2")
    grafo_g2.mostrar()

    print('-' * 20)

    print(f"G'1 é subgrafo de G? {grafo_g.eh_subgrafo(grafo_g1)}")
    print(f"G'2 é subgrafo de G? {grafo_g.eh_subgrafo(grafo_g2)}")

    print(f"\nG'1 é subgrafo gerador de G? {grafo_g.eh_subgrafo_gerador(grafo_g1)}")
    print(f"G'2 é subgrafo gerador de G? {grafo_g.eh_subgrafo_gerador(grafo_g2)}")
    print(f"G'1 é subgrafo gerador de G'2? {grafo_g2.eh_subgrafo_gerador(grafo_g1)}")
 