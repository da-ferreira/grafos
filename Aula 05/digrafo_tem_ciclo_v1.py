
class Digrafo:
    """
    Digrafo com lista de adjacencia com implementacao do algoritmo para verificar
    se o grafo tem ciclo utilizando a funcao de encontrar um caminho entre dois vertices.
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
        
        for vertice in range(self.vertices):
            for u in self.lista_adjacente[vertice]:
                if self.tem_caminho(u, vertice):
                    return True
        
        return False
    
    def tem_caminho(self, s, t):
        """ Verifica se ha um caminho do vertice s para o t no grafo. """
        
        visitados = [False] * self.vertices
        self.dfs_visita(s, visitados)

        return visitados[t]  # Se t está na lista de visitados de do DFS de s então tem caminho s-t

    def dfs_visita(self, u, visitados):
        """ Executa a busca em profundidade. """
        
        visitados[u] = True

        for w in self.lista_adjacente[u]:
            if not visitados[w]:
                self.dfs_visita(w, visitados)


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0, 2), (0, 4), (0, 3), (2, 1), (3, 4), (4, 2), (4, 1), (4, 5), (5, 3), (1, 5)]

    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])

    digrafo.mostrar()
    print(f"Tem ciclos no grafo? {digrafo.tem_ciclo()}")
    