## Importamos flask
from flask import Flask
app=Flask(__name__)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

## Definimos una segunda ruta
@app.route("/ruta2")
def ruta2():
    return "<strong> Estamos en la segunda ruta </strong> <hr>"

## Definimos una tercera ruta
@app.route("/ruta3")
def ruta3():
    return "<em> Estamos en la tercera ruta </em> <hr>"

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

if __name__=='__main__':
    ## El valor True indica que la app se deja en modo debug
    app.run(debug=True)
    