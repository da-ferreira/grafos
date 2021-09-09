
BRANCO = 1  # O vértice não foi processado ainda

# Os vértices estão sendo processados. Ou seja, o vértice que estiver em CINZA foi descoberto,
# mas o seu processamento só será finalizado depois que todos os seus descendentes na recursão
# da busca em profundidade forem processados (visitados)
CINZA = 2   

PRETO = 3  # O vértice e todos os seus descendentes já foram processados (visitados)

class Digrafo:
    """
    Digrafo com lista de adjacencia com o algoritmo para verificar se o grafo tem ciclo utilizando cores.
    O consumo de tempo do algoritmo, na lista de adjacencia, é O(V + E), onde E é o conjunto de arestas
    e V o conjunto de vertices.
    """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for i in range(self.vertices)]
    
    def inserir(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def tem_ciclo(self):
        cor = [BRANCO] * self.vertices

        for vertice in range(self.vertices):
            if cor[vertice] == BRANCO:
                if self.tem_arco_de_retorno(vertice, cor):
                    return True
        
        return False

    def tem_arco_de_retorno(self, u, cor):
        cor[u] = CINZA

        for w in self.lista_adjacente[u]:
            if cor[w] == CINZA:  # Se w for cinza, então há um arco de retorno no grafo, logo tem ciclo
                return True
            elif cor[w] == BRANCO:
                if self.tem_arco_de_retorno(w, cor):
                    return True

        cor[u] = PRETO
        return False


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0, 2), (0, 4), (0, 3), (2, 1), (3, 4), (4, 2), (4, 1), (4, 5), (5, 3), (1, 5)]

    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])

    digrafo.mostrar()
    print(f"Tem ciclo no grafo? {digrafo.tem_ciclo()}")
