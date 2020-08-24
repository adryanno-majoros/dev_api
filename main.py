from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Majoros',
     'habilidade':['Python', 'Flask']},
    {'nome':'Galleani',
     'habilidade':['Phyon', 'Django']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/' , methods=['POST', 'GET'] )
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)


if __name__ == '__main__':
#    print_hi('PyCharm')
    app.run(debug=True)


