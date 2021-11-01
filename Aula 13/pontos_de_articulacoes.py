
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    tempo = 0
    INFINITO = float("inf")

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for _ in range(self.vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].add(w)
        self.lista_adjacente[w].add(u)   

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def pontos_de_articulacoes(self):
        """
        Retorna os vértices que são pontos de articulações do grafo.
        Um vértice é ponto de articulação se:

        - Se pai[v] == −1 (v é a raíz da árvore DFS) e v tem pelo menos dois filhos na árvore DFS.
        - Se pai[v] != −1 (v não é raiz da árvore no DFS) e v tem pelo menos um filho w tal que nenhum
          descendente na sub-árvore(w) está conectado a algum ancestral de v usando aresta de retorno.

        Usando o vetor low (lowest preorder number):

        - Uma aresta {v, w} identifica o ponto de articulação v se pai[v] != nulo e low[w] >= pre[v].
        """

        Grafo.tempo = 0
        pre = [-1] * self.vertices
        pai = [-1] * self.vertices
        low = [Grafo.INFINITO] * self.vertices

        self.DFS(0, pre, pai, low)  # Assumindo que o grafo é conexo (começa o DFS do vértice 0)

    def DFS(self, vertice, pre, pai, low):
        Grafo.tempo += 1
        pre[vertice] = Grafo.tempo
        low[vertice] = Grafo.tempo
        eh_ponto_de_articulacao = False
        filhos = 0

        for w in self.lista_adjacente[vertice]:
            if pre[w] == -1:  # Aresta de arborescencia
                pai[w] = vertice
                filhos += 1
                self.DFS(w, pre, pai, low)
                
                low[vertice] = min(low[vertice], low[w])

                if low[w] >= pre[vertice]:
                    eh_ponto_de_articulacao = True
                
            elif w != pai[vertice]:  # Aresta de retorno
                low[vertice] = min(low[vertice], pre[w])
        
        if (pai[vertice] != -1 and eh_ponto_de_articulacao) or (pai[vertice] == -1 and filhos > 1):
            print(vertice)


if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()

    print("\nPontos de articulações (ou vértices de corte) do grafo:")
    grafo.pontos_de_articulacoes()
    
