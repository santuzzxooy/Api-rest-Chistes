from flask import(
    Flask,
    render_template,
    request,
    redirect,
)


# pip install dadjokes
# esta aplicacion toma los datos de https://icanhazdadjoke.com/api
from dadjokes import Dadjoke

import random

app = Flask(__name__)
app.secret_key = '48fiuis871fe5g'


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")


# vista de inicio
@app.route('/')
def index():
   numero = random.randint(0, 1)
   print(numero)
   return render_template('index.html',
                           numero=numero)

a = 46
b = 10

def maximo_comun_divisor(a, b):

   temporal = 0
   while b != 0:
      temporal = b
      b = a % b
      a = temporal
   return a

def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)

mcm = minimo_comun_multiplo(a, b)
print(f"El mínimo común múltiplo de {a} y {b} es {mcm}")

@app.route('/matematica_uno', methods=['GET'])
def numeros():
   args = request.args
   a = args.get("number1", default=0, type=int)
   b = args.get("number2", default=0, type=int)
   return f'la respuesta es = mínimo común múltiplo de {a} y {b} = {mcm}'

@app.route('/matematica_dos', methods=['GET'])
def numero():
   args = request.args
   print(args.get("number"))
   numero = args.get("number", default=0, type=int)
   number = numero + 1
   return f'la respuesta es = {number}'


if __name__ == '__main__':
   app.run(debug=True, port=5000)