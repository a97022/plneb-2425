from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

# Carregar conceitos do ficheiro JSON
try:
    with open("conceitos_.json", "r") as file:
        res = json.load(file)
except FileNotFoundError:
    res = {}

@app.route("/")  # Página inicial
def home():
    return render_template("home.html")

@app.route("/conceitos")  # Listar conceitos e pesquisar ocorrências
def listarconceitos():
    query = request.args.get("query")
    ocorrencias = {}
    conceito_exato = None

    if query:
        query_lower = query.lower()
        # Expressão regular para buscar o termo inteiro
        regex = re.compile(rf"\b{re.escape(query)}\b", flags=re.IGNORECASE)

        for conceito, descricao in res.items():
            if descricao is None:  # Se a descrição for None, define como string vazia
                descricao = ""

            # Verifica se o termo de pesquisa é exatamente o conceito
            if query_lower == conceito.lower():
                # Destacar o termo no conceito e na descrição
                conceito_destacado = regex.sub(r'<strong>\g<0></strong>', conceito)
                descricao_destacada = regex.sub(r'<strong>\g<0></strong>', descricao)
                conceito_exato = {conceito_destacado: descricao_destacada}
            else:
                # Verifica se o termo aparece na descrição como uma palavra inteira
                if regex.search(descricao):
                    descricao_destacada = regex.sub(r'<strong>\g<0></strong>', descricao)
                    ocorrencias[conceito] = descricao_destacada

        # Combina os resultados: conceito exato primeiro, depois as ocorrências
        resultados = {}
        if conceito_exato:
            resultados.update(conceito_exato)
        resultados.update(ocorrencias)

        return render_template("significado.html", conceitos=resultados, termo=query)

    return render_template("conceitos.html", conceitos=res)


@app.route("/conceitos/<designacao>")  # Consultar um conceito específico
def consultar_conceitos(designacao):
    if designacao in res:
        return render_template("significado.html", conceitos={designacao: res[designacao]}, termo=designacao)
    else:
        return "Conceito não encontrado", 404

if __name__ == "__main__":
    app.run(host="localhost", port=4002, debug=True)