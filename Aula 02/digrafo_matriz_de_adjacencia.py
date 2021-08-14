

class Digrafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.matriz = [[0] * vertices for x in range(vertices)]
    
    def insere(self, u, v):
        self.matriz[u][v] = 1
        self.arestas += 1
    
    def mostra(self):
        for i in range(self.vertices):
            print(f"{i}: ", end='')

            for j in range(self.vertices):
                if self.matriz[i][j] == 1:
                    print(f"{j} ", end='')

            print()

    def grau_de_entrada(self, vertice):
        grau = 0

        for linha in self.matriz:
            if linha[vertice] == 1:
                grau += 1
        
        return grau
    
    def grau_de_saida(self, vertice):
        return self.matriz[vertice].count(1)

    """
    Um vértice é uma fonte quando o grau de saída for maior que zero e o grau de entrada for igual a 0.
    Retorna True caso seja uma fonte, False do contrário.
    """
    def eh_fonte(self, vertice):
        return self.grau_de_saida(vertice) > 0 and self.grau_de_entrada(vertice) == 0

    """
    Um vértice é um sorvedouro quando o grau de entrada for maior que zero e o grau de saída for igual a 0.
    Retorna True caso seja um sorvedouro, False do contrário.
    """
    def eh_sorvedouro(self, vertice):
        return self.grau_de_entrada(vertice) > 0 and self.grau_de_saida(vertice) == 0


    """
    Um digrafo é simétrico se cada uma das arestas é anti-paralela a outra, ou seja, se há uma aresta
    (1, -> 2) deve haver uma (2, -> 1), se o digrafo tiver 2 vértices. Em todo digrafo simétrico, grau-(v) = grau+(v)
    para todo vértice v. Retorna True caso seja um digrafo simétrico, False do contrário.
    """
    def eh_simetrico(self):
        for vertice in range(self.vertices):
            if self.grau_de_entrada(vertice) != self.grau_de_saida(vertice):
                return False
        
        return True 

       
def testa_fonte_e_sorvedouro():
    grafo_orientado = Digrafo(4)
    arestas = [(0, 1), (0, 2), (2, 1), (1, 3), (3, 2), (1, 1)]

    for aresta in arestas:
        grafo_orientado.insere(aresta[0], aresta[1])

    grafo_orientado.mostra()
    
    print('-------')

    print(f"O vértice 0 é uma fonte? {grafo_orientado.eh_fonte(0)}")
    print(f"O vértice 0 é um sorvedouro? {grafo_orientado.eh_sorvedouro(0)}")
    print(f"Grau de entrada do vértice 0: {grafo_orientado.grau_de_entrada(0)}")
    print(f"Grau de saída do vértice 0: {grafo_orientado.grau_de_saida(0)}\n")

    print(f"O vértice 2 é uma fonte? {grafo_orientado.eh_fonte(2)}")
    print(f"O vértice 2 é um sorvedouro? {grafo_orientado.eh_sorvedouro(2)}")
    print(f"Grau de entrada do vértice 2: {grafo_orientado.grau_de_entrada(2)}")
    print(f"Grau de saída do vértice 2: {grafo_orientado.grau_de_saida(2)}")
  

if __name__ == "__main__":
    digrafo = Digrafo(3)
    arestas = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]

    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()

    print(f"O digrafo acima é simétrico? {digrafo.eh_simetrico()}")
