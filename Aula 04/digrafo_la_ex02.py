
""" 
Digrafo com lista de adjacência
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

    def exibe_todos_caminhos(self, s, t):
        """ Exibe todos os caminhos entre dois vértices, s e t, caso exista. """
        
        caminho = []                         # Lista que guarda vai guardando o caminho corfome o grafo é percorrido
        visitados = [False] * self.vertices  # Lista de visitados
        
        print(f"\nTodos os caminhos de s={s} para t={t}:")
        self.visita(s, t, visitados, caminho)

    def visita(self, s, t, visitados, caminho):
        if s == t:
            caminho.append(t)
            print(' -> '.join(str(x) for x in caminho))
            caminho.pop()
            return True

        visitados[s] = True
        caminho.append(s)

        for w in self.lista_adjacente[s]:
            if not visitados[w]:
                self.visita(w, t, visitados, caminho)
        
        # Tira o vértice do caminho e da lista de visitados porque ele pode fazer parte de outros caminhos
        caminho.pop()
        visitados[s] = False


if __name__ == "__main__":
    digrafo = Digrafo(6)
    arestas = [(0,1), (0,4), (2,0), (2,4), (2,3), (3,4), (3,5), (4,1), (4,5), (5,1)]
    
    for aresta in arestas:
        digrafo.insere(aresta[0], aresta[1])

    digrafo.mostra()    

    digrafo.exibe_todos_caminhos(2, 1)
    digrafo.exibe_todos_caminhos(0, 5)
    digrafo.exibe_todos_caminhos(4, 3)
    digrafo.exibe_todos_caminhos(2, 5)
