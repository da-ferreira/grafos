
class Digrafo:
    """ Digrafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def kosaraju(self, digrafo_transposto):
        """ 
        Algoritmo de Kosaraju (1978) obtém os componentes fortemente conexos do grafo orientado. 
        1. Execute DFS(G) para obter f[v] para v ∈ V
        2. Obter o grafo transposto GT
        3. Execute DFS(GT) considerando os vértices em ordem decrescente de f[v].
        4. Devolva os conjuntos de vértices de cada árvore da floresta de busca em profundidade obtida
        """

        visitados = [False] * self.vertices
        ordem = []  # Vetor dos tempos de finalização de cada vértice

        for vertice in range(self.vertices):
            if not visitados[vertice]:
                self.DFS(vertice, ordem, visitados)
        
        print(ordem)

    
    def DFS(self, u, ordem, visitados):
        """ Faz a busca em profundidade para obter os tempos de finalização. """
        
        visitados[u] = True

        for w in self.lista_adjacente[u]:
            if not visitados[w]:
                self.DFS(w, ordem, visitados)
        
        ordem.append(u)


    def DFS_transponto(self, digrafo_transposto, u, ordem, visitados):
        """ 
        Executa a busca em profundidade considerando os vertices em ordem decrescente no vetor de tempos de
        finalização e retorna os conjuntos de vértices obtidos que são os componentes fortemente conexos do digrafo.
        """
        pass
    

if __name__ == "__main__":
    digrafo = Digrafo(8)
    digrafo_transposto = Digrafo(8)
    arestas = [(0, 1), (1, 2), (1, 4), (1, 5), (2, 3), (2, 6), (3, 2), (3, 7), (4, 0), (4, 5), (5, 6), (6, 5), (6, 7), (7, 7)]
    
    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])
        digrafo_transposto.inserir(aresta[1], aresta[0])

    print("Grafo G:")
    digrafo.mostrar()
    
    print("Grafo transposto G:")
    digrafo_transposto.mostrar()

    print("Componentes fortemente conexos:")
    print(digrafo.kosaraju(digrafo_transposto))
  