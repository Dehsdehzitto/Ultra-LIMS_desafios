#solução recursiva
def fibonnaci(n):
  if(n == 0): return 0
  if(n == 1): return 1
  return fibonnaci(n - 1) + fibonnaci(n - 2)

#solução não recursiva
def fibonnaci_solucao_2(n):
  if(n == 0): return 0
  if(n == 1): return 1
  primeiro = 0
  segundo = 1
  for _ in range(2, n + 1):
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
  return proximo
