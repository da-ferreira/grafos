# Algoritmo de Hierholzer O(E)

> Entrada: Um grafo com uma trilha euleriana  
> Saída: Uma trilha de Euler (fechada ou não)
  
* Todas as arestas iniciam-se desmarcadas.
* Escolha um vértice inicial v e insira na pilha.
* Enquanto a pilha não está vazia.
    * Seja **u** o vértice do topo da pilha.
    * Para **w** adjacente a **u** faça
        * Se a aresta **(u, w)** está desmarcada então
            * Adicione **w** a pilha e marque a aresta **(u, w)**
            * **break**  # A aresta u tem incidente
    * Se **u** não possui aresta incidente desmarcada
        * remova **u** do topo da pilha e imprima **u**.

Quando a pilha estiver vazia, o algoritmo terá imprimido uma sequência de vértices da trilha de Euler.
