
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for _ in range(self.vertices)]
        self.grau = [0] * self.vertices  # Grau dos vertices
    
    def inserir(self, u, w):
        self.lista_adjacente[u].add(w)
        self.lista_adjacente[w].add(u)
        self.grau[u] += 1
        self.grau[w] += 1   

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def fleury(self):
        """
        O problema do carteiro chinês pode ser resolvido pelo Algoritmo de Fleury, já que ele encontra
        uma trilha de Euler no grafo euleriano. Este algoritmo constrói uma trilha sujeita à condição
        de que, em cada passo, a aresta escolhida para compor a trilha não seja de corte no grafo 
        restante, a menos que não haja alternativa.
        """
        pass


if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 5), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()

    print(f"\nTrilha euleriana encontrada pelo algoritmo de Fleury: {grafo.fleury()}")
