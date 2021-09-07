
class Digrafo:
    """
    Digrafo com lista de adjacencia com o algoritmo para verificar se o grafo tem ciclo utilizando pilha.
    O consumo de tempo do algoritmo, na lista de adjacencia, é O(V + E),
    onde E é o conjunto de arestas e V o conjunto de vertices.
    """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.arestas = 0
        self.lista_adjacente = [set() for i in range(self.vertices)]
    
    def inserir(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)
            self.arestas += 1

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def tem_ciclo(self):
        """ Verifica se tem ciclo no grafo. """

        visitados = [False] * self.vertices
        esta_na_pilha = [False] * self.vertices

        for vertice in range(self.vertices):
            if not visitados[vertice]:
                if self.visita(vertice, visitados, esta_na_pilha):
                    return True

        return False
    
    def visita(self, u, visitados, esta_na_pilha):
        visitados[u] = True
        esta_na_pilha[u] = True

        for w in self.lista_adjacente[u]:
            if not visitados[w]:
                self.visita(w, visitados, esta_na_pilha)
            elif esta_na_pilha[w]:
                return True
        
        esta_na_pilha[u] = False
        return False


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0, 2), (0, 4), (0, 3), (2, 1), (3, 4), (4, 2), (4, 1), (4, 5), (5, 3), (1, 5)]

    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])

    digrafo.mostrar()
    print(f"Tem ciclos no grafo? {digrafo.tem_ciclo()}")
 