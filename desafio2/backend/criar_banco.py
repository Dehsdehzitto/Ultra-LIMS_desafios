import sqlite3

connection = sqlite3.connect("ceps.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE registro (cep TEXT PRIMARY KEY, bairro TEXT, estado TEXT, localidade TEXT)")

connection.commit()

connection.close()