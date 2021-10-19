
"""
Em uma rede social, dado um conjunto de n pessoas (numeradas de 0, 1, · · · n − 1),
gostaríamos de dividir em dois grupos de tamanho arbitrário.

Cada pessoa pode enviar um dislike para alguma outra pessoa, quando isso ocorre, elas devem
ser separadas em dois grupos distintos (digamos o grupo da esquerda e o grupo da direita).

Formalmente, se o dislikes[i] = (a,b), significa que as pessoas
numerada por a e b devem ser colocadas em grupos diferentes.

Devolva True se somente se for possível dividir todos em dois grupos, e False caso contrário.

RESOLUÇÃO:

O exercício será resolvido verificando se o grafo montado, onde os vértices serão cada pessoa e
as arestas os dislikes entre elas, é bipartido. Se for, é possivel dividir todos em dois grupos.
"""

INCOLOR = -1
VERMELHO = 0
AZUL = 1

class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [[] for _ in range(self.vertices)]
    
    def inserir(self, u, w):
        self.lista_adjacente[u].append(w)
        self.lista_adjacente[w].append(u)

    def eh_bipartido(self):
        """ 
        Verifica, utilizando bicoloração do conjunto de vértices, se o grafo é bipartido.
        Atribui-se cores a cada vértice de tal modo que dois vértices adjacentes não tenham
        a mesma cor. Se isso acontecer o grafo é bipartido.
        """
        
        cores = [INCOLOR] * self.vertices
        return self.DFS(0, VERMELHO, cores)

    def DFS(self, vertice, cor, cores):
        """ Executa a busca em profundidade atribuindo cores aos vértices (vermelho ou azul). """
        cores[vertice] = cor

        for u in self.lista_adjacente[vertice]:
            if cores[u] == INCOLOR:
                if self.DFS(u, cor ^ 1, cores) == False:  # A cor varia em [0, 1], a operação ^ 1 alterna entre 0 e 1.
                    return False
            elif cores[vertice] == cores[u]:
                return False
        
        return True


if __name__ == "__main__":
    grafo1 = Grafo(4)
    dislikes = [(0, 1), (0, 2), (1, 3)]
    
    for dislike in dislikes:
        grafo1.inserir(dislike[0], dislike[1])

    print(f"(Grafo 1) É possivel separar as n pessoas em dois grupos? {grafo1.eh_bipartido()}")

    grafo2 = Grafo(4)
    dislikes = [(0, 1), (0, 2), (1, 2)]
    
    for dislike in dislikes:
        grafo2.inserir(dislike[0], dislike[1])

    print(f"(Grafo 2) É possivel separar as n pessoas em dois grupos? {grafo2.eh_bipartido()}")

    grafo3 = Grafo(5)
    dislikes = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    
    for dislike in dislikes:
        grafo3.inserir(dislike[0], dislike[1])

    print(f"(Grafo 3) É possivel separar as n pessoas em dois grupos? {grafo3.eh_bipartido()}")
  