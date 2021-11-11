
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.qtd_vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.qtd_vertices)]
        self.grau = [0] * self.qtd_vertices  # Grau dos vertices
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[w].append(u)
        self.grau[u] += 1
        self.grau[w] += 1

    def mostrar(self):
        for i in range(self.qtd_vertices):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def hierholzer(self):
        """ 
        O problema do carteiro chinês pode ser resolvido pelo Algoritmo de Hierholzer,
        já que ele encontra uma trilha euleriana fechada em um grafo conexo euleriano.
        Algoritmo detalhado em 'Aula 15 > Algoritmo de Hierholzer.md'.
        Complexidade: O(E).
        """

        impares = [vertice for vertice in self.grau if vertice % 2 == 1]  # Todos os vértices de grau ímpar

        if len(impares) != 0:
            return False  # Grafo não é euleriano, não tem todos os vértice com grau par




if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 3), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()
      