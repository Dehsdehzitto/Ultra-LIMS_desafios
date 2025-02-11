# primeira solução de fibonnaci
# 0 1 1 2 3 5 8 13 21 34 55 89 144

def fibonnaci_solucao_1(n):
  if(n == 0): return 0
  if(n == 1): return 1
  primeiro = 0
  segundo = 1
  for _ in range(2, n + 1):
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
  return proximo

retorno = fibonnaci_solucao_1(2)
print(retorno)

# 0 1 1 2 3 5 8 13 21 34 55 89 144
# fibonacci de n = fibonnaci de n - 1 + fibonnaci de n - 2
def fibonnaci(n):
  if(n == 0): return 0
  if(n == 1): return 1
  return fibonnaci(n - 1) + fibonnaci(n - 2)

# n == 4
# fibonnaci(3) + fibonnaci(2)
# fibonnaci(2) + fibonnaci(1) + fibonnaci(1) + fibonnaci(0)
# fibonnaci(2) + 1 + 1 + 0
# fibonnaci(1) + fibonnaci(0) + 1 + 1 + 0
# fibonnaci(1) + fibonnaci(0) + 1 + 1 + 0
retorno2 = fibonnaci(4)
print(retorno2)