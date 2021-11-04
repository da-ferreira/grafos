
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = [x for x in range(vertices)]
        self.lista_adjacente = [[] for _ in self.vertices]
        self.grau = [0] * len(self.vertices)  # Grau dos vertices
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[w].append(u)
        self.grau[u] += 1
        self.grau[w] += 1
    
    def remover(self, u, w):
        self.lista_adjacente[u].remove(w)
        self.lista_adjacente[w].remove(u)
        self.grau[u] -= 1
        self.grau[w] -= 1   

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def fleury(self):
        """
        O problema do carteiro chinês pode ser resolvido pelo Algoritmo de Fleury, já que ele encontra
        uma trilha de Euler no grafo euleriano. Este algoritmo constrói uma trilha sujeita à condição
        de que, em cada passo, a aresta escolhida para compor a trilha não seja de corte no grafo 
        restante, a menos que não haja alternativa. Algoritmo detalhado em 'Aula 14 > Algoritmo de Fleury.md'
        """
        
        impares = [vertice for vertice in self.grau if vertice % 2 == 1]  # Todos os vértices de grau ímpar

        if len(impares) > 2:
            return "Não é um grafo euleriano"
        
        if len(impares) == 0:  # Trilha euleriana fechada
            vertice = 0  # Começa pelo vértice 0
        else:
            vertice = impares[0]  # Trilha euleriana aberta

        trilha = []  
        self.mostra_trilha_euleriana(vertice, trilha)
        return trilha

    def mostra_trilha_euleriana(self, vertice, trilha):
        pass

    def eh_ponte(self, u, v):
        pass

    def eh_conexo(self):
        pass


if __name__ == "__main__":
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 5), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()
    print(grafo.vertices)

    print(f"\nTrilha euleriana encontrada pelo algoritmo de Fleury: {grafo.fleury()}")
    grafo.mostrar()
    print(grafo.vertices)
