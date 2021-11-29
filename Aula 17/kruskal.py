
class DisjointSets:
    def __init__(self, vertices):
        """ Cria um novo conjunto {x}. x não deve estar em nenhum outro conjunto. """

        self.id = [-1] * vertices
        self.sz = [0] * vertices  # Tamanho dos conjuntos (quantidade de elementos)

    def make_set(self, x):
        self.id[x] = x

    def find(self, x):
        """ find(x) == find(y) se e somente se x e y estão no mesmo conjunto. """

        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])
        
        return self.id[x]

    def union(self, x, y):
        """ Combina o conjunto que contém x com o conjunto que contém y. """
        
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.sz[x] > self.sz[y]:
            x, y = y, x
        
        self.id[x] = y
        self.sz[y] += self.sz[x]


def kruskal(arestas, vertices):
    """ Gera uma árvore geradora mínima em um grafo com pesos. Complexidade total: O(E log E). """

    disjoint_sets = DisjointSets(vertices)
    arestas.sort(key=lambda item: item[2])  # Ordenando peso peso das arestas

    A = []

    for vertice in range(vertices):
        disjoint_sets.make_set(vertice)

    for (u, v, weight) in arestas:
        if disjoint_sets.find(u) != disjoint_sets.find(v):
            disjoint_sets.union(u, v)
            A.append((u, v))

    return A

if __name__ == "__main__":
    arestas = [(0, 1, 7), (0, 2, 10), (0, 3, 15), (1, 4, 9), (1, 5, 12), (1, 6, 5), (2, 6, 8), (2, 7, 3), (5, 6, 6), (6, 7, 14)]
    print(f"Ligações no grafo para a árvore geradora mínima: {kruskal(arestas, 8)}")
  