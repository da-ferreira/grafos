
"""  Digrafo com lista de adjacência """

class Digrafo:
    def __init__(self, vertices): 
        self.vertices = vertices
        self.arestas = 0
        self.lista_adjacente = [set() for i in range(self.vertices)]
        self.tempo = -1  # Guarda o tempo de visitado do i-esimo vértice
    
    def inserir(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)
            self.arestas += 1

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def DFS_visita(self, u, pai, d, f, visitados):
        visitados[u] = True
        self.tempo += 1
        d[u] = self.tempo

        for w in self.lista_adjacente[u]:
            if not visitados[w]:
                pai[w] = u
                self.DFS_visita(w, pai, d, f, visitados)
        
        self.tempo += 1
        f[u] = self.tempo
    
    def classificacao(self, v, w):
        """ Retorna a classificação (arborescência, descendente, retorno ou cruzado) do arco v - w, caso exista """

        visitados = [False] * self.vertices
        d = [-1] * self.vertices    # Vetor dos tempos de descoberta de cada vértice
        f = [-1] * self.vertices    # Vetor dos tempos de finalização de cada vértice
        pai = [-1] * self.vertices  # Vetor dos pais
        
        self.tempo = -1

        for vertice in range(self.vertices):
            if not visitados[vertice]:
                pai[vertice] = vertice
                self.DFS_visita(vertice, pai, d, f, visitados)

        if d[v] < d[w] < f[w] < f[v] and pai[w] == v:
            print(f"{v} - {w} é arco de arborescência")
        
        elif d[v] < d[w] < f[w] < f[v] and pai[w] != v:
            print(f"{v} - {w} é arco de descendente")            
        
        elif d[w] < d[v] < f[v] < f[w]:
            print(f"{v} - {w} é arco de retorno")
        
        elif d[w] < f[w] < d[v] < f[v]:
            print(f"{v} - {w} é arco cruzado")
        else:
            print(f"Não existe arco entre {v} - {w}")


if __name__ == "__main__":
    digrafo = Digrafo(8)
    arestas = [(0, 5), (0, 7), (5, 2), (5, 7), (2, 1), (7, 1), (1, 5), (4, 0), (4, 7), (3, 4), (3, 6), (6, 3), (6, 4)]

    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])

    digrafo.classificacao(2, 1)
    digrafo.classificacao(0, 7)
    digrafo.classificacao(1, 5)
    digrafo.classificacao(7, 1)
    digrafo.classificacao(0, 3)
    digrafo.classificacao(0, 1)
