
"""
Digrafo com lista de adjacência, com implementação do algoritmo DFS (Depth-First Search), Busca em Profundidade
Consumo de tempo para a lista de adjacência do DFS é O(V + A)
"""

class Digrafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.lista_adjacente = [[] for i in range(self.vertices)]
    
    def insere(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].append(w)
            self.arestas += 1

    def mostra(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    """ Retorna todos os vértices adjancentes de u """
    def adjacente(self, u):
        return self.lista_adjacente[u]

    """ Aplica o algoritmo DFS (Depth-First Search), Busca em Profundidade """
    def busca_em_profundidade(self, u, visitados): 
        visitados.add(u)

        for w in self.adjacente(u):
            if w not in visitados:
                self.busca_em_profundidade(w, visitados)

    """ Retorna True se existe um caminho de s para t no digrafo """
    def existe_caminho(self, s, t): 
        vertices_visitados = set()
        self.busca_em_profundidade(s, vertices_visitados)

        return t in vertices_visitados


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0,1), (0,4), (2,0), (2,4), (2,3), (3,4), (3,5), (4,1), (4,5), (5,1)]
    
    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()

    assert(digrafo.existe_caminho(3, 1) == True)
    assert(digrafo.existe_caminho(5, 4) == False)

    print(f"\nExiste um caminho de 3 para 1 no digrafo? {digrafo.existe_caminho(3, 1)}")
    print(f"Existe um caminho de 5 para 4 no digrafo? {digrafo.existe_caminho(5, 4)}\n")
       