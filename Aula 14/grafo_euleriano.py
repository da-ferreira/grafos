
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

    def eh_euleriano(self):
        """ Um grafo é euleriano se todos os vértices tem grau par. """
        return all(vertice % 2 == 0 for vertice in self.grau)

    def tem_trilha_euleriana(self):
        """ Um grafo tem uma trilha euleriana se tem no máximo 2 vértices de grau ímpar. """
        return len([vertice for vertice in self.grau if vertice % 2 == 1]) <= 2


if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 5), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()

    print(f"\nO grafo é euleriano? {grafo.eh_euleriano()}")
    print(f"O grafo tem uma trilha euleriana? {grafo.tem_trilha_euleriana()}") 
      