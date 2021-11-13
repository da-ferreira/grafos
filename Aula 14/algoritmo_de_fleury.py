
class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.qtd_vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.qtd_vertices)]
        self.grau = [0] * self.qtd_vertices  # Grau dos vertices
        self.vertices = set()
    
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
        for i in range(self.qtd_vertices):
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

        for u in range(self.qtd_vertices):
            self.vertices.add(u)

        trilha = []  
        self.trilha_euleriana(vertice, trilha)
        return trilha

    def trilha_euleriana(self, vertice, trilha):
        trilha.append(vertice)

        if len(self.lista_adjacente[vertice]) == 0:
            return

        for w in self.lista_adjacente[vertice]:
            if not self.eh_ponte(vertice, w):
                self.remover(vertice, w)

                if self.grau[vertice] == 0:
                    self.vertices.remove(vertice)
                
                if self.grau[w] == 0:
                    self.vertices.remove(w)

                self.trilha_euleriana(w, trilha)
                return 

    def eh_ponte(self, u, v):
        if len(self.lista_adjacente[u]) == 1:
            return False
        
        self.remover(u, v)

        if not self.eh_conexo():
            resultado = True
        else:
            resultado = False

        self.inserir(u, v)
        return resultado

    def eh_conexo(self):
        visitados = [False] * self.qtd_vertices
        componentes = 0

        for vertice in self.vertices:
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
    grafo = Grafo(6)
    arestas = [(0, 1), (0, 5), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    for aresta in arestas:
        grafo.inserir(aresta[0], aresta[1])

    grafo.mostrar()

    print(f"\nTrilha euleriana encontrada pelo algoritmo de Fleury: {' - '.join(str(i) for i in grafo.fleury())}\n")
