
"""
Escreva um método na classe Grafo (não orientado) que devolva o complemento de um grafo. Utilize uma lista de adjacências.
"""

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.adjacencia = [set() for i in range(vertices)] 
    
    def inserir(self, u, v):
        if u not in self.adjacencia[v] and v not in self.adjacencia[u]:
            self.adjacencia[u].add(v)
            self.adjacencia[v].add(u)
            self.arestas += 1
    
    def mostrar(self):
        for i in range(len(self.adjacencia)):
            print(f"{i} -> {', '.join(str(x) for x in self.adjacencia[i])}")

    """ 
    Devolve um grafo complementar ao grafo da instancia.
    Para encontrar o complemento de um grafo é preciso preencher todas as arestas que 
    faltam para obter um grafo completo e remover todas as arestas que já estavam no grafo.
    """
    def complementar(self):
        grafo_complementar_g = Grafo(self.vertices)
        arestas_grafo_complementar_g = []  # Arestas do grafo

        for vertice in range(self.vertices):  # Obtendo o grafo completo
            arestas_grafo_complementar_g.append({x for x in range(self.vertices) if x != vertice})

        # Removendo todas as arestas que já estavam no grafo
        for i in range(self.vertices):
            for j in self.adjacencia[i]:
                arestas_grafo_complementar_g[i].remove(j)

        # Passando as arestas pro grafo complementar
        grafo_complementar_g.adjacencia = arestas_grafo_complementar_g

        return grafo_complementar_g  


if __name__ == "__main__":
    #  0       4
    #   \     /
    #    1---3
    #     \ /
    #      2

    grafo_A = Grafo(5)
    arestas = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 4)] 

    for aresta in arestas:
        grafo_A.inserir(aresta[0], aresta[1])

    print("Grafo A:\n")
    grafo_A.mostrar()
        
    grafo_complementar_de_A = grafo_A.complementar()

    print("\nGrafo complementar de A:\n")
    grafo_complementar_de_A.mostrar()
     