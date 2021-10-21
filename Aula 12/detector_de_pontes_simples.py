
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[w].append(u)   

    def remover(self, u, w):
        self.lista_adjacente[u].remove(w)
        self.lista_adjacente[w].remove(u)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def pontes(self):
        """
        Retorna todas as pontes existentes no grafo. Usa uma abordagem simples, realizando a
        remoção de arestas, uma de cada vez, e verificando se essa remoção desconecta o grafo.

        Algoritmo:
        para cada aresta {u, v} em G faça
            Remova {u, v} do grafo G
            Verifique se o grafo continua conexo
            Adicione {u, v} no grafo G

        Complexidade: O(E * (V + E))
        """
        
        pontes = set()

        for vertice in range(self.vertices):
            for aresta in self.lista_adjacente[vertice]:
                self.remover(vertice, aresta)

                if not self.eh_conexo():
                    pontes.add((vertice, aresta))
                
                self.lista_adjacente[vertice].insert(0, aresta)
        
        return pontes

    def eh_conexo(self):
        """
        Uma busca em profundidade (DFS) iterativa (com pilha) é feita para obter o
        número de componentes do grafo. Se esse número for 1, então o grafo é conexo.
        """

        visitados = [False] * self.vertices
        componentes = 0

        for vertice in range(self.vertices):
            if not visitados[vertice]:
                pilha = [vertice]
                visitados[vertice] = True
                componentes += 1

                while len(pilha) > 0:
                    u = pilha.pop()

                    for w in self.lista_adjacente[u]:  # Visita todos os filhos do vértice tirado da pilha
                        if not visitados[w]:
                            pilha.append(w)
                            visitados[w] = True
        
        return componentes == 1


if __name__ == "__main__":
    grafo = Grafo(8)
    arestas = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (4, 5), (4, 7), (5, 6), (6, 7)]
    
    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()
    
    print(f"\nPontes do grafo: {grafo.pontes()}")
