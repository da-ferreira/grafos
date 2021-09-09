
class Digrafo:
    """
    Digrafo com lista de adjacencia com o algoritmo para verificar se o grafo
    tem ciclo utilizando classificação dos arcos. O consumo de tempo do algoritmo,
    na lista de adjacencia, é O(V + E), onde E é o conjunto de arestas e V o conjunto de vertices.
    O consumo de memória é um pouco maior do que utilizando pilha, pois usa duas listas (d e f).
    """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for i in range(self.vertices)]
        self.tempo = 0  # Guarda o tempo de visita do i-esimo vértice
    
    def inserir(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)

    def mostrar(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def tem_ciclo(self):
        d = [-1] * self.vertices  # Lista dos tempos de descoberta de cada vértice 
        f = [-1] * self.vertices  # Lista dos tempos de finalização de cada vértice

        for vertice in range(self.vertices):
            if d[vertice] == -1:  # se o vértice ainda não foi visitado
                if self.tem_arco_de_retorno(vertice, d, f):
                    return True
        
        return False

    def tem_arco_de_retorno(self, u, d, f):
        d[u] = self.tempo
        self.tempo += 1

        for w in self.lista_adjacente[u]:
            if d[w] == -1:  
                if self.tem_arco_de_retorno(w, d, f):
                    return True
            elif f[w] == -1:
                return True
        
        f[u] = self.tempo
        self.tempo += 1
        return False
        

if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0, 2), (0, 4), (0, 3), (2, 1), (3, 4), (4, 2), (4, 1), (4, 5), (5, 3), (1, 5)]

    for aresta in arestas:
        digrafo.inserir(aresta[0], aresta[1])

    digrafo.mostrar()
    print(f"Tem ciclo no grafo? {digrafo.tem_ciclo()}")
 