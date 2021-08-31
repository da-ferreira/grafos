
""" 
Digrafo com lista de adjacência, com implementação de DFS
para mostrar um caminho entre dois vértices, caso exista
"""

class Digrafo:
    def __init__(self, vertices): 
        self.vertices = vertices
        self.arestas = 0
        self.lista_adjacente = [set() for i in range(self.vertices)]
    
    def insere(self, u, w):
        if w not in self.lista_adjacente[u]:
            self.lista_adjacente[u].add(w)
            self.arestas += 1

    def mostra(self):
        for i in range(len(self.lista_adjacente)):
            print(f"{i}: {', '.join(str(x) for x in self.lista_adjacente[i])}")

    def exibe_caminho(self, s, t):
        """ Exibe o caminho de entre dois vértices, s e t, caso exista. """

        caminho = []                         # Lista que guarda o caminho, se existir
        visitados = [False] * self.vertices  # Lista de visitados
        existe_caminho = self.dfs_visita(s, t, visitados, caminho)

        if existe_caminho is None:
            print(f"O caminho de s={s} para t={t} não existe.")
        else:
            print(f"O caminho de s={s} para t={t} é {caminho}")

    def dfs_visita(self, s, t, visitados, caminho):
        """ Faz a busca em profundidade, BFS """

        if s == t:
            caminho.append(t)
            return True

        visitados[s] = True
        caminho.append(s)
        
        for w in self.lista_adjacente[s]:
            if not visitados[w]:
                if self.dfs_visita(w, t, visitados, caminho) == True:
                    return True
        
        caminho.pop()


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0,1), (0,4), (2,0), (2,4), (2,3), (3,4), (3,5), (4,1), (4,5), (5,1)]
    
    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()    

    digrafo.exibe_caminho(3, 1)
    digrafo.exibe_caminho(2, 1)
    digrafo.exibe_caminho(4, 0)
    