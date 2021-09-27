
class Grafo:
    """ Grafo não orientado utilizando lista de adjacencia. """
    
    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for i in range(self.vertices)]
    
    def inserir(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)
            self.lista_adjacente[w].add(u)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def numero_de_componentes(self):
        """  Uma busca em profundidade (DFS) iterativa (com pilha) é feita. """
        
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
        
        return componentes

    def eh_conexo(self):
        """ Retorna True se o grafo for conexo; False do contrário. """
        return self.numero_de_componentes() == 1


if __name__ == "__main__":
    grafo = Grafo(9)
    arestas = [(0, 1), (1, 2), (2, 0), (3, 4), (5, 6), (7, 6), (8, 6)]
            
    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    print("grafo G:")
    grafo.mostrar()
    print(f"\nNúmero de componentes do grafo G: {grafo.numero_de_componentes()}")
    print(f"O grafo G é conexo? {grafo.eh_conexo()}")
              