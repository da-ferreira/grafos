
class MinHeap:
    """ Implementa uma fila de prioridades MinHeap. """
    pass

    def __init__(self):
        pass

    def constroi_heap(self):  # O(n)
        pass

    def subir(self):  # O(log n)
        pass

    def inserir(self):  # O(log n)
        pass

    def descer(self):  # O(log n)
        pass

    def remover(self):  # O(log n)
        pass

    def extrair_minimo(self):  # O(log n)
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

    def Dijkstra(self, s):
        """
        Resolve o problema do caminho mínimo de fonte única em um grafo não-direcionado com pesos nas arestas.
        :param s: vértice inicial.
        :return: Um vetor de distancia (mínima) do vértice inicial s para todos os vértices e o vetor de pai.
        """
        pass


if __name__ == "__main__":
    #digrafo = Digrafo()
    #arcos = [(, , ), ]

    #for arco in arcos:
    #    digrafo.inserir(arco)
    pass