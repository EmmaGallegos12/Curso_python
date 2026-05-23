from flask import Flask, render_template, request
from frases_celebres import Frase, carga_archivo_csv, crea_diccionario_titulos, buscar_palabras

app = Flask(__name__)

frases = carga_archivo_csv("frases_consolidadas.csv")
diccionario_titulos = crea_diccionario_titulos(frases)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pelicula', methods=['GET', 'POST'])
def pelicula():
    if request.method == 'POST':
        pelicula = request.form.get('pelicula')
        lista_frases_pelicula = diccionario_titulos.get(pelicula.lower(), [])
        return render_template("pelicula.html", lista_frases_pelicula=lista_frases_pelicula)
    return render_template("pelicula.html")

@app.route('/frases', methods=['GET', 'POST'])
def frase():
    if request.method == 'POST':
        palabra = request.form.get('frase')
        lista_frases_palabra = buscar_palabras(frases, palabra)
        return render_template("frases.html", frases=lista_frases_palabra)
    return render_template("frases.html", frases=[])

if __name__ == "__main__":
    app.run(debug=True) 