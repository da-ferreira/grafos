
class MinHeap:
    """ Implementa uma fila de prioridades MinHeap. """
    pass

    def __init__(self):
        self.heap = [0]
        self.n = 0

    def vazio(self):
        return self.n == 0

    def pai(self, i):
        return i // 2

    def esquerdo(self, i):
        return 2 * i

    def direito(self, i):
        return 2 * i + 1

    def trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def subir(self, i):  # O(log n)
        pai = self.pai(i)

        while pai >= 1 and self.heap[i] < self.heap[pai]:
            self.trocar(i, pai)
            pai = self.pai(pai)

    def inserir(self, item):  # O(log n)
        self.heap.append(item)
        self.n += 1
        self.subir(self.n)

    def descer(self, i=1):  # O(log n)
        n = self.n

        while (2 * i) <= n:
            e = self.esquerdo(i)
            d = self.direito(i)

            if (d <= n) and (self.heap[d] < self.heap[e]):
                j = d
            else:
                j = e
            
            if self.heap[i] > self.heap[j]:
                self.trocar(i, j)
            else:
                i = n + 1

    def extrair_minimo(self):  # O(log n)
        min = self.heap[1]
        self.heap[1] = self.heap[self.n]
        self.heap.pop()
        self.n -= 1
        self.descer(1)

        return min

class Grafo:
    """ Grafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.qtd_vertices = vertices
        self.adjacente = [[] for _ in range(self.qtd_vertices)]
    
    def inserir(self, arco):
        u, w, peso = arco
        self.adjacente[u].append((w, peso))
        self.adjacente[w].append((u, peso))

    def mostrar(self):
        for i in range(self.qtd_vertices):
            print(f"{i}: {', '.join(f'(aresta={x[0]}, peso={x[1]})' for x in self.adjacente[i])}")

    def prim(self, s):
        """
        Gera uma árvore geradora mínima em um grafo conexo com pesos. Complexidade usando MinHeap: O(E log V)

        :param s: vértice inicial.
        :return: Um vetor de chaves e o vetor de pais.
        """


if __name__ == "__main__":
    pass