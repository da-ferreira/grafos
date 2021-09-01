
""" 
Digrafo com lista de adjacência, com implementação do algoritmo DFS para
mostrar, de modo iterativo, um caminho entre dois vértices, caso exista.
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

    def busca_em_profundidade(self):
        """ Implementa o algoritmo DFS, busca em profundidade, de forma iterativa """

        visitados = [False] * self.vertices  # Lista de visitados
        pilha = []

        for vertice in range(self.vertices):
            if not visitados[vertice]:
                pilha.append(vertice)
                visitados[vertice] = True

                while len(pilha) > 0:
                    u = pilha.pop()
                    print(u)

                    for w in self.lista_adjacente[u]:
                        if not visitados[w]:
                            pilha.append(w)
                            visitados[w] = True
    

if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0,1), (0,4), (2,0), (2,4), (2,3), (3,4), (3,5), (4,1), (4,5), (5,1)]
    
    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()
    print("Busca em profundidade:")    
    digrafo.busca_em_profundidade()
       