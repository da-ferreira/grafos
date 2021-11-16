
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.qtd_vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.qtd_vertices)]
        self.grau = [0] * self.qtd_vertices  # Grau dos vertices
        self.arestas = []
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[w].append(u)
        self.grau[u] += 1
        self.grau[w] += 1
        self.arestas.append((u, w))

    def mostrar(self):
        for i in range(self.qtd_vertices):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def hierholzer(self):
        """ 
        O problema do carteiro chinês pode ser resolvido pelo Algoritmo de Hierholzer,
        já que ele encontra uma trilha euleriana fechada em um grafo conexo euleriano.
        Algoritmo detalhado em 'Aula 15 > Algoritmo de Hierholzer.md'.
        Complexidade: O(E).
        """
        
        impares = [vertice for vertice in self.grau if vertice % 2 == 1]  # Todos os vértices de grau ímpar
        
        if len(impares) > 2:
            raise Exception("Grafo não contém trilha euleriana!")

        arestas_marcadas = {}  # Todas as arestas do grafo (indo e voltando, porque o grafo é não direcionado)

        for u, v in self.arestas:
            arestas_marcadas[(u, v)] = False
            arestas_marcadas[(v, u)] = False
        
        if len(impares) == 0:
            v = 0
        else:
            v = impares[0]

        pilha = [v]  # Começa pelo vértice 0
        trilha = []

        while len(pilha) != 0:
            u = pilha[-1]
            avancou_para_os_filhos = False

            for w in self.lista_adjacente[u]:
                if not arestas_marcadas[(u, w)]:
                    avancou_para_os_filhos = True
                    pilha.append(w)
                    arestas_marcadas[(u, w)] = True
                    arestas_marcadas[(w, u)] = True
                    break
            
            if not avancou_para_os_filhos:
                trilha.append(pilha.pop())

        return trilha
        

if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 3), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()
    print(f"\nTrilha euleriana encontrada pelo algoritmo de Hierholzer: {grafo.hierholzer()}\n")

    grafo2 = Grafo(4)
    arestas2 = [(0, 1), (1, 2), (1, 3), (2, 3)]

    for aresta in arestas2:
        grafo2.inserir(aresta[0], aresta[1])

    grafo2.mostrar()
    print(f"\nTrilha euleriana encontrada pelo algoritmo de Hierholzer: {grafo2.hierholzer()}")

      