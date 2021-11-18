
class Digrafo:
    """ Digrafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.qtd_vertices = vertices
        self.lista_adjacente = [set() for _ in range(self.qtd_vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].add(w)

    def mostrar(self):
        for i in range(self.qtd_vertices):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def BSF(self, s):
        """
        Executa a busca em largura (BFS) e retorna o percurso os vértices visitados. Complexidade: O(V + E).
        :param s: vértice que começa a busca em largura.
        """

        visitados = [False] * self.qtd_vertices
        visitados[s] = True
        fila = [s]
        
        percurso = []

        while len(fila) != 0:
            vertice = fila.pop(0)
            percurso.append(vertice)

            for w in self.lista_adjacente[vertice]:
                if not visitados[w]:
                    visitados[w] = True
                    fila.append(w)

        return percurso


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5), (5, 1)]

    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])

    digrafo.mostrar()

    print(f"\nPercurso da busca em largura: {digrafo.BSF(0)}")
