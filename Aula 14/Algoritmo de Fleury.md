# Algoritmo de Fleury O((V + E)^2 )

### Fleury(G)
* impares = obter-vertices-de-grau-impar(G)
* se tamanho(impares) > 2 então
    * imprima("Não existe trilha de Euler")
    * retorne
* senão se tamanho(impares) = 0 então
    * v = escolha-vertice-qualquer()
* senão
    * v = impares[0]  _# escolha um vértice de grau ímpar_
* mostra-trilha-euleriana(G, v)

### trilha-euleriana(G, v)
* insere-na-trilha(v)
* se tamanho(adj[v]) == 0 então
	* retorne
* para w adjacente ao vértice v faça
    * se eh-ponte(G, v, w) = Falso faça
        * remove-aresta(G, v, w)
        * trilha-euleriana(G, w)
        * retorne
        
### eh-ponte(G, v, w)
* se tamanho(adj[j]) == 1 então
    * retorne Falso
* remove-aresta(G, v, w)
* se eh-conexo(G) == Verdadeiro então
    * resultado = Falso
* senão
    * resultado = Verdadeiro
* insere-aresta(G, v, w)
* retorne resultado

### eh-conexo(G)

* Feito com DFS (busca em profundidade) utilizando pilha