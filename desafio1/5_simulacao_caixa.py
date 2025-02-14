def saque(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moeda = 1
    notas_usadas = []
    moedas_usadas = []
    for nota in notas:
        quantidade = 0
        while valor >= nota:
            valor -= nota
            notas_usadas.append(nota)
            quantidade += 1
        if(quantidade):
          print(f"{quantidade} nota de {nota}")
    quantidade = 0
    while valor >= moeda:
        quantidade += 1
        valor -= moeda
        moedas_usadas.append(moeda)
    if(quantidade):
      print(f"{quantidade} moeda de {moeda}")