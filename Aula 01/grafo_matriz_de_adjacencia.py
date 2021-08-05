
""" 
Grafo não orientado utilizando matriz de adjacência.
Uma matriz de V x V, com índices marcados com 1 se uma aresta (u, v)
for adjacente, caso contrário é marcado com 0.
---
Espaço: O(n^2), sendo n o número de vértices do grafo.
"""

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices + 1  # Os indices começaram a partir de 1
        self.arestas = 0
        self.matriz = [[0] * self.vertices for i in range(self.vertices)]

    def insere(self, u, v):
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1
        self.arestas += 1
    
    def remove(self, u, v):
        self.matriz[u][v] = 0
        self.matriz[v][u] = 0
        self.arestas -= 1

    def mostra(self):
        print("Vértices com suas respectivas arestas\n")

        for i in range(1, len(self.matriz)):
            print(f"vértice {i}: ", end='')

            for j in range(1, len(self.matriz)):
                if self.matriz[i][j] == 1:
                    print(f"{j} ", end='')
            
            print()


# 1-----2
# |    /| \
# |   / |  \
# |  /  |   5
# | /   |  /  
# |/    | /
# 3-----4

if __name__ == "__main__":
    grafo = Grafo(5)
    arestas = [(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]

    for aresta in arestas:
        grafo.insere(aresta[0], aresta[1])

    grafo.mostra()

