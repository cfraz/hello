from flask import Flask, render_template, request

app = Flask(__name__)

# Dados simulados para o exemplo
precos = {
    "milho": 85.50,
    "soja": 123.30,
    "arroz": 45.10,
    "trigo": 33.45
}
historico = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        produto = request.form.get("produto")
        qtd = float(request.form.get("quantidade"))
        historico.append({"produto": produto, "quantidade": qtd})
    return render_template("index.html", precos=precos, historico=historico)

if __name__ == "__main__":
    app.run(debug=True)