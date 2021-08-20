
"""
Um grafo simples tal que cada par de vertices distintos está ligada por um aresta é chamado grafo completo.
Um grafo completo G, com |V(G)| = n, é denominado Kn.
Escreva um metodo eh_completo() que devolve True se o grafo é completo e False caso contráio.

Grafo não orientado utilizando lista de adjacência.
"""

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.adjacencia = [set() for i in range(vertices)]  # Sets para na hora de comparar não gerar problemas
    
    def inserir(self, u, v):
        if u not in self.adjacencia[v] and v not in self.adjacencia[u]:
            self.adjacencia[u].add(v)
            self.adjacencia[v].add(u)
            self.arestas += 1
    
    def mostrar(self):
        print("Vértices com suas respectivas arestas:\n")

        for i in range(len(self.adjacencia)):
            print(f"{i} -> {', '.join(str(x) for x in self.adjacencia[i])}")

    def eh_completo(self):
        for vertice in range(self.vertices):  # Verificando se cada vértice tem ligação com os demais vértices
            outros_vertices = {x for x in range(self.vertices) if x != vertice}

            for u in outros_vertices:
                if u not in self.adjacencia[vertice]:
                    return False
        
        return True
        

if __name__ == "__main__":
    # Grafo completo K4:
    grafo1 = Grafo(4)
    arestas = [(0, 1), (0, 2), (0, 3),
               (1, 0), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 3),
               (3, 0), (3, 1), (3, 2)]

    for aresta in arestas:
        grafo1.inserir(aresta[0], aresta[1])

    grafo1.mostrar()
    print(grafo1.eh_completo(), "\n")

    grafo2 = Grafo(4)
    arestas = [(0, 1), (0, 2), (0, 3),
               (1, 0), (1, 2), (1, 3),
               (2, 0), (2, 1),
               (3, 0), (3, 1)]  # Tirando a ligação do vértice 2 pro 3 (2 --- 3), ou seja, o grafo2 não é completo

    for aresta in arestas:
        grafo2.inserir(aresta[0], aresta[1])

    grafo2.mostrar()
    print(grafo2.eh_completo())
    