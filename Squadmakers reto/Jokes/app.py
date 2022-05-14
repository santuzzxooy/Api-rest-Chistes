from flask import(
    Flask,
    render_template,
    request,
    redirect,
)

# importamos la funcion de la clase de donde tomamos chuck_jokes
from api.request_api import chuck_joke

import sqlite3 as sql

# pip install dadjokes
# esta aplicacion toma los datos de https://icanhazdadjoke.com/api
from dadjokes import Dadjoke

import random

app = Flask(__name__)
app.secret_key = '48fiuis871fe5g'



number = 1
if number == number:
   number = number+1

print(number)


@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

# vista de inicio con chiste aleatorio from dad or chuck
@app.route('/')
def index():
   numero = random.randint(0, 1)
   print(numero)

   if numero == 0:
      joke = chuck_joke.api()
      res = chuck_joke.api()
      joke = res['value']
      created = res['created_at']
      updated = res['updated_at']
      url = res['url']
      id = res['id']
      conn = sql.connect('data.db')
      cursor = conn.cursor()
      instruccion = f"INSERT INTO jokes VALUES ('{joke}', '{id}', {number})"
      cursor.execute(instruccion)
      conn.commit()
      conn.close()

      return render_template('index.html', 
                           joke=joke,
                           created=created,
                           updated=updated,
                           url=url,
                           id=id,
                           numero=numero)
   else:
      dadjoke = Dadjoke()
      joke = dadjoke.joke
      id = dadjoke.id
      print(joke, id)
      conn = sql.connect('data.db')
      cursor = conn.cursor()
      instruccion = f"INSERT INTO jokes VALUES ('{joke}', '{id}', {number})"
      cursor.execute(instruccion)
      conn.commit()
      conn.close()

      return render_template('index.html',
                           joke=joke,
                           id=id,
                           numero=numero)


# vista de chistes dad
@app.route('/dad')
def dad():
   dadjoke = Dadjoke()
   joke = dadjoke.joke
   id = dadjoke.id
   print(joke, id)

   conn = sql.connect('data.db')
   cursor = conn.cursor()
   instruccion = f"INSERT INTO jokes VALUES ('{joke}', '{id}', {number})"
   cursor.execute(instruccion)
   conn.commit()
   conn.close()

   return render_template('dad.html',
                           joke=joke,
                           id=id)


# vista de chistes chuck
@app.route('/chuck', methods=['GET'])
def chuck():
   args = request.args
   numero = args.get("number", default=0, type=int)
   
   res = chuck_joke.api()
   joke = res['value']
   created = res['created_at']
   updated = res['updated_at']
   url = res['url']
   id = res['id']

   conn = sql.connect('data.db')
   cursor = conn.cursor()
   instruccion = f"INSERT INTO jokes VALUES ('{joke}', '{id}', {numero})"
   cursor.execute(instruccion)
   conn.commit()
   conn.close()

   return render_template('chuck.html', 
                           joke=joke,
                           created=created,
                           updated=updated,
                           url=url,
                           id=id)


# vista de chistes dad
@app.route('/update')
def update():
   dadjoke = Dadjoke()
   joke = dadjoke.joke
   id = dadjoke.id
   print(joke, id)

   conn = sql.connect('data.db')
   cursor = conn.cursor()
   instruccion = f"INSERT INTO jokes VALUES ('{joke}', '{id}', {number})"
   cursor.execute(instruccion)
   conn.commit()
   conn.close()

   return render_template('dad.html',
                           joke=joke,
                           id=id)

if __name__ == '__main__':
   app.run(debug=True, port=5000)