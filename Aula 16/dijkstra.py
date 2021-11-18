
class MinHeap:
    pass

class Digrafo:
    """ Digrafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.qtd_vertices = vertices
        self.lista_adjacente = [set() for _ in range(self.qtd_vertices)]
    
    def inserir(self, arco):
        u, w, peso = arco
        self.lista_adjacente[u].add((w, peso))

    def mostrar(self):
        for i in range(self.qtd_vertices):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def Dijkstra(self):
        pass


if __name__ == "__main__":
    #digrafo = Digrafo()
    #arcos = [(, , ), ]

    #for arco in arcos:
    #    digrafo.inserir(arco)
    pass