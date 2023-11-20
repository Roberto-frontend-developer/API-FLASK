from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/api/json', methods=['GET'])
def ler_json():
  with open('dados.json', 'r') as arquivos:
    dados = json.load(arquivos)
  return jsonify(dados)

if __name__ == '__main__':
  app.run()