import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3



app = Flask(__name__)
CORS(app)

#/historico?bairro=asc&localidade=desc&estado=asc

@app.route('/historico', methods=['GET'])
def historico():
  connection = sqlite3.connect("ceps.db")
  cursor = connection.cursor()
  enderecos = []
  bairro = request.args.get('bairro')
  localidade = request.args.get('localidade')
  estado = request.args.get('estado')
  order = "ORDER BY "
  if(bairro): order += "bairro " + bairro
  if(localidade): order += "localidade " + localidade
  if(estado): order += "estado " + estado
  # ordenar por bairro ou localidade ou estado ascendente / descendente
  for registro in cursor.execute("SELECT cep, estado, bairro, localidade FROM registro " + order ):
    dado = {}
    dado['cep'] = registro[0]
    dado['estado'] = registro[1]
    dado['bairro'] = registro[2]
    dado['localidade'] = registro[3]
    enderecos.append(dado)
  connection.close()
  return jsonify(enderecos)

@app.route('/cep/<cep>', methods=['GET'])
def consulta_cep(cep):
  endereco = f"https://viacep.com.br/ws/{cep}/json/"
  resposta = requests.get(endereco)
  if(resposta.ok):
    connection = sqlite3.connect("ceps.db")
    cursor = connection.cursor()
    resposta = resposta.json()
    cursor.execute("INSERT OR REPLACE INTO registro (cep, estado, bairro, localidade) VALUES (?, ?, ?, ?)", (resposta['cep'], resposta['uf'], resposta['bairro'], resposta['localidade']))
    connection.commit()
    connection.close()
    return jsonify(resposta)
  else:
    return jsonify({"erro": "CEP não encontrado"}), 404


app.run(port=8000)
#http://127.0.0.1:8000/cep