def eh_palindromo(palavra):
  return palavra == palavra[::-1]


texto = "Desdehzitto e Ysarot eht otizshde oossoossoosso "
texto2 = "Socorram me subi no onibus em Marrocos"

def maior_palindromo(texto):
  maior_palindromo_atual = 1
  for inicio in range(0, len(texto) - 1):
    for fim in range(len(texto) -1, 0, -1):
      if(inicio > fim):
        break
      palavra = texto[inicio:fim]
      palindromo = eh_palindromo(palavra)
      if(palindromo):
        tamanho_palavra = len(palavra)
        if(tamanho_palavra > maior_palindromo_atual):
          maior_palindromo_atual = tamanho_palavra
  
  return maior_palindromo_atual