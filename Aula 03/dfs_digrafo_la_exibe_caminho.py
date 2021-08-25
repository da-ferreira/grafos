
"""
Digrafo com lista de adjacência, com implementação do algoritmo DFS (Depth-First Search - Busca em Profundidade),
para exibir um caminho, se existir, entre dois vértices s e t no digrafo.
Consumo de tempo para a lista de adjacência do DFS é O(V + A)
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

    """ Retorna todos os vértices adjancentes de u """
    def adjacente(self, u):
        return self.lista_adjacente[u]

    """ 
    Aplica o algoritmo DFS (Depth-First Search), Busca em Profundidade,
    para encontrar e exibir um caminho entre dois vértices, s e t, no grafo.
    """
    def busca_em_profundidade(self, u, visitados, caminho): 
        visitados.add(u)

        for w in self.adjacente(u):
            if w not in visitados:
                caminho[w] = u
                self.busca_em_profundidade(w, visitados, caminho)    
    
    """ Exibe o caminho (caso exista) de s para t no digrafo """
    def exibe_caminho(self, s, t):
        vertices_visitados = set()
        caminho = {s: s}  # O inicio do caminho veio dele mesmo

        self.busca_em_profundidade(s, vertices_visitados, caminho)

        if t in vertices_visitados:  # Verifica se o caminho de s para t existe
            caminho_s_t = []         # Guarda o caminho de s para t
            temp = t
            
            while True:
                if temp == caminho[temp]:
                    caminho_s_t.insert(0, temp)
                    break

                caminho_s_t.insert(0, temp)
                temp = caminho[temp]

            return caminho_s_t

        return False  # O caminho não existe
            

if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0,1), (0,4), (2,0), (2,4), (2,3), (3,4), (3,5), (4,1), (4,5), (5,1)]
    
    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()    

    print(f"O caminho de s=3 para t=1 é: {digrafo.exibe_caminho(3, 1)}")
    print(f"O caminho de s=2 para t=5 é: {digrafo.exibe_caminho(2, 5)}")
    print(f"O caminho de s=0 para t=2 é: {digrafo.exibe_caminho(0, 2)}")
      