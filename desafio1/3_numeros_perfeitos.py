def numero_perfeito(numero):
  soma = 0
  for n in range(1, numero):
    if(numero % n == 0):
      soma += n
  return soma == numero