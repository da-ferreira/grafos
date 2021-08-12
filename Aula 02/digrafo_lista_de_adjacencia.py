
class Digrafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.lista_adjacente = [[] for i in range(self.vertices)]

    def insere(self, u, w):
        self.lista_adjacente[u].append(w)
        self.arestas += 1

    def mostra(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")
    
    """
    Inverte a ordem dos vizinhos de um dado vértice na lista de adjacencia. Se um vértice x tem 
    seus vizinhos como a, b, c, então, na sua inversão, x ficara com seus vizinhos como c, b, a.
    """
    def inverter_vizinhos(self, u):
        self.lista_adjacente[u].reverse()
    
    def grau_de_entrada(self, u):
        grau = 0

        for i in range(self.vertices):
            if u in self.lista_adjacente[i]:
                grau += 1
        
        return grau

    def grau_de_saida(self, u):
        return len(self.lista_adjacente[u])
    
    """
    Um vértice é uma fonte quando o grau de saída for maior que zero e o grau de entrada for igual a 0.
    Retorna True caso seja uma fonte, False do contrário.
    """
    def eh_fonte(self, u):
        return self.grau_de_saida(u) > 0 and self.grau_de_entrada(u) == 0

    """
    Um vértice é um sorvedouro quando o grau de entrada for maior que zero e o grau de saída for igual a 0.
    Retorna True caso seja um sorvedouro, False do contrário.
    """
    def eh_sorvedouro(self, u):
        return self.grau_de_saida(u) == 0 and self.grau_de_entrada(u) > 0


def testa_grafo_inverter_vizinhos():
    grafo_orientado = Digrafo(4)
    arestas = [(0, 1), (0, 2), (2, 1), (1, 3), (3, 2), (1, 1)]

    for aresta in arestas:
        grafo_orientado.insere(aresta[0], aresta[1])

    grafo_orientado.mostra()

    print('-----------')

    grafo_orientado.inverter_vizinhos(1)
    grafo_orientado.mostra()


if __name__ == "__main__":
    grafo_orientado = Digrafo(4)
    arestas = [(0, 1), (0, 2), (2, 1), (1, 3), (3, 2), (1, 1)]

    for aresta in arestas:
        grafo_orientado.insere(aresta[0], aresta[1])
     
    grafo_orientado.mostra()
    print(f'Grau de entrada do vértice 0: {grafo_orientado.grau_de_entrada(0)}')
    print(f'Grau de saída do vértice 0: {grafo_orientado.grau_de_saida(0)}')
    print(f'O vértice 0 é uma fonte? {grafo_orientado.eh_fonte(0)}')
    print(f'O vértice 0 é um sorvedouro? {grafo_orientado.eh_sorvedouro(0)}')
       