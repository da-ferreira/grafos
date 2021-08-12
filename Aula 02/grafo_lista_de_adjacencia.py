
""" 
Grafo não orientado utilizando lista de adjacência.
Uma lista de lista de 1 x V, com os valores dos vértices
que são subjacentes a posição i da lista.
---
Espaço: n + 2m, onde n é o número de vértice e m é o número de arestas.
"""

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices + 1  # Os indices começaram a partir de 1
        self.arestas = 0
        self.lista = [[] for i in range(self.vertices)]
    
    def insere(self, u, v):
        self.lista[u].append(v)
        self.lista[v].append(u)
        self.arestas += 1

    def remove(self, u, v):
        self.lista[u].remove(v)
        self.lista[v].remove(u)
        self.arestas -= 1

    def mostra(self):
        print("Vértices com suas respectivas arestas\n")

        for i in range(1, len(self.lista)):
            print(f"{i}: {', '.join(str(x) for x in self.lista[i])}")
    
    """ Compara o grafo atual com outro grafo. Retorna True caso ambos forem iguais. """
    def ehIgual(self, outro_grafo):
        for i in range(self.vertices):
            if self.lista[i] != outro_grafo.lista[i]:
                return False

        return True


if __name__ == "__main__":
    grafo1 = Grafo(5)
    arestas_g1 = [(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    grafo2 = Grafo(5)

    for aresta in arestas_g1:
        grafo1.insere(aresta[0], aresta[1])
        grafo2.insere(aresta[0], aresta[1])

    grafo3 = Grafo(5)
    arestas_g3 = [(1, 1), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    for aresta in arestas_g3:
        grafo3.insere(aresta[0], aresta[1])

    print(f'O grafo 1 é igual ao grafo 2? {grafo1.ehIgual(grafo2)}')
    print(f'O grafo 2 é igual ao grafo 1? {grafo2.ehIgual(grafo1)}')
    print(f'O grafo 1 é igual ao grafo 3? {grafo1.ehIgual(grafo3)}')
