
class Digrafo:
    """ Digrafo utilizando lista de adjacencia. """

    def __init__(self, vertices): 
        self.vertices = vertices
        self.lista_adjacente = [set() for i in range(self.vertices)]
        self.tempo = 0  # Guarda o tempo de visita do i-esimo vértice
    
    def inserir(self, u, w):
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

    def ordenacao_topologica(self):
        """ Ordenação topológica com os vértices organizados em ordem decrescente de tempo de término. """

        if self.tem_ciclo():  # Se o grafo contém ciclo, nenhuma ordenação topológica é possivel
            return []

        d = [-1] * self.vertices  # Tempo de descoberta
        f = [-1] * self.vertices  # Tempo de finalização
        ordem_topologica = []
        self.tempo = 0

        for vertice in range(self.vertices):
            if d[vertice] == -1:  # se o vértice ainda não foi visitado
                self.visita(vertice, d, f, ordem_topologica)

        return list(reversed(ordem_topologica))

    def visita(self, vertice, d, f, ordem_topologica):
        """ Faz a busca em profundidade (DFS) marcando os tempos dos vértices. """

        d[vertice] = self.tempo
        self.tempo += 1

        for w in self.lista_adjacente[vertice]:
            if d[w] == -1:
                self.visita(w, d, f, ordem_topologica)

        f[vertice] = self.tempo
        self.tempo += 1
        ordem_topologica.append(vertice)
        

if __name__ == "__main__":
    grafo = Digrafo(9)
    arcos = [(0, 4), (0, 3), (1, 4), (3, 4), (3, 5), (5, 8), (6, 5), (6, 7), (7, 8)]

    for arco in arcos:
        grafo.inserir(arco[0], arco[1])

    tarefa = {
        0: 'cueca',
        1: 'meias',
        2: 'relogio',
        3: 'calça',
        4: 'sapatos',
        5: 'cinto',
        6: 'camisa',
        7: 'gravata',
        8: 'paleto'
    }

    ordenacao_topologica = grafo.ordenacao_topologica()

    if len(ordenacao_topologica) > 0:
        for v in ordenacao_topologica:
            print(tarefa[v])
    else:
        print("O grafo contém ciclo, nenhuma ordenação topológica é possivel!")
     