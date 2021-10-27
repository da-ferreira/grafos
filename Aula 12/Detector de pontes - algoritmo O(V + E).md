
# Algoritmo O(E + V) para detectar pontes em grafos

A ideia é utilizar a estratégia de busca em profundidade, partindo de algum vértice arbitrário.  
  
Suponha que v é um vértice atual no percurso DFS, e w algum vértice adjacente a v.  
  
A aresta {v, w} é ponte se e somente nenhum descendente de w tem alguma aresta de retorno para v ou  
para algum ancestral de v. Assim, a única maneira de sair de v para alcançar w seria pela aresta {v, w}.  
Em outras palavras a aresta {v, w} é ponte se ela não está contida em um ciclo de G.  
  
### Considerações:  

- **pre[v]** é o tempo de descoberta usando busca em profundidade  

- Se pre[v] < pre[w], significa que v foi descoberto antes de w no percurso DFS.
  Logo, v pode ser ancestral de w, ou pode estar em alguma árvore distinta.
  
- Se pre[v] > pre[w], então o arco de v para w é um arco de retorno.  
    
### Menor ancestral alcançável    
    
Vamos agora utilizar um novo vetor, denotado por **low**, que armazena para cada vértice v ∈ V(G) o menor número de pré-ordem  
(lowest preorder number) alcançado utilizando arcos de arborescência e até um arco de retorno (arco pai não vale).  
Dado algum vértice v ∈ V (G), low[v] é, portanto, o menor tempo de descoberta dentre todos os vértices que são alcançáveis  
a partir da subárvore (ou subgrafo) cuja raiz é v.    

### Observações

Para todo vértice v, **low[v] <= pre[v]**

Para todo arco (v, w) do grafo  

- Se (v, w) é um arco de arborescência, então **low[v] ≤ low[w]**
- Se (v, w) é um arco de retorno, então **low[v] ≤ pre[w]**

### Identificando pontes

Seja G(V, E) um grafo conexo e s ∈ V o vértice de partida de um DFS.  
Um arco de arborescência **(v, w)** faz parte de uma ponte se: 

- **low[w] > pre[v]**
- **low[w] == pre[w]**

# Algoritmo

### detectar-pontes(G)

* tempo = 0  
* para cada vértice v em V(G) faça  
* pre[v] = -1  
* pai[v] = -1  
* para cada vértice v em V(G) faça  
    * se pre[v] == -1 então  
        * pai[v] = v  
        * DFS-visita(G, v)  

### DFS-visita(G, v)

* tempo = tempo + 1
* pre[v] = tempo
* low[v] = pre[v]
* para cada vértice w em adj(v) faça
    * se pre[w] == -1 então
        * pai[w] = v
        * DFS-visita(G, w)
        * low[v] = min(low[v], low[w])
        * se low[w] == pre[w] então
            * imprima(v, w) # _(v, w) é uma ponte_
    * else if w != pai[v] então
        * low[v] = min(low[v], pre[w])
