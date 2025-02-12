def busca_binaria(lista, elemento):
  inicio = 0
  fim = len(lista) - 1
  while(inicio <= fim):
    posicao_meio = (inicio + fim) // 2
    if(lista[posicao_meio] == elemento):
      return posicao_meio
    if(elemento < lista[posicao_meio]):
      fim = posicao_meio - 1
    if(elemento > lista[posicao_meio]):
      inicio = posicao_meio + 1
  return -1
