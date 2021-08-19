
"""
Digrafo com lista de adjacência
"""

class Digrafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.lista_adjacente = [[] for i in range(self.vertices)]

    def insere(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].append(w)
            self.arestas += 1

    def mostra(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    """ Retorna True se um vértice for adjance a outro. """
    def eh_adjancete(self, u, v):
        return v in self.lista_adjacente[u]
    
    """ Retorna True caso uma dada sequencia de vértices for um caminho do digrafo. """
    def eh_caminho(self, sequencia):
        if len(sequencia) <= 1:
            return True

        for i in range(len(sequencia) - 1):
            if not self.eh_adjancete(sequencia[i], sequencia[i + 1]):
                return False
        
        return True

    """ 
    Um caminho é simples se não tem vértices repetidos. 
    Retorna True caso uma dada sequencia de vértices for um caminho simples do digrafo.
    """
    def eh_caminho_simples(self, sequencia):
        return self.eh_caminho(sequencia) and len(sequencia) == len(set(sequencia))  # O set remove elementos iguais


if __name__ == "__main__":
    digrafo = Digrafo(5)
    arestas = [(0, 1), (1, 0), (0, 2), (1, 3), (3, 2), (3, 4), (2, 4)]

    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()

    print(f"\n0 -> 2 -> 4 é um caminho? {digrafo.eh_caminho([0, 2, 4])}")
    print(f"0 -> 1 -> 3 -> 2 -> 4 é um caminho? {digrafo.eh_caminho([0, 1, 3, 2, 4])}\n")

    print(f"0 -> 1 -> 3 -> 2 -> 4 é um caminho simples? {digrafo.eh_caminho_simples([0, 1, 3, 2, 4])}")
    print(f"0 -> 1 -> 0 -> 2 -> 4 é um caminho simples? {digrafo.eh_caminho_simples([0, 1, 0, 2, 4])}")
     