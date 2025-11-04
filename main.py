from flask import Flask, render_template, request
import random

app = Flask(__name__)

def a_romano(numero):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numero = int(request.form["numero_correcto"])
        respuesta = request.form["respuesta"]
        if respuesta.isdigit() and int(respuesta) == numero:
            mensaje = "✅ ¡Correcto!"
        else:
            mensaje = f"❌ Incorrecto. Era {numero}."
        nuevo_numero = random.randint(1, 3999)
        return render_template("index.html",
                               romano=a_romano(nuevo_numero),
                               numero_correcto=nuevo_numero,
                               mensaje=mensaje)
    else:
        numero = random.randint(1, 3999)
        return render_template("index.html",
                               romano=a_romano(numero),
                               numero_correcto=numero,
                               mensaje="")

if __name__ == "__main__":
    app.run(debug=True)


