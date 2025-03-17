from flask import Flask, request, render_template
import json

app = Flask(__name__)

db_file = open("conceitos_.json", "r", encoding="utf-8")
#db_file = open("conceitos_.json", "r")

db = json.load(db_file) #carregamos este json de maneira global pq muitas rotas vao precisar dessa bd
db_file.close()

@app.route("/")
def hello_world():
    return "<p>TPC5</p>"

@app.route('/conceitos')
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")


@app.route('/api/conceitos')
def api_conceitos():
    return db

@app.post("/api/conceitos")
def adicionar_conceito():
    #json
    data = request.get_json()
    #{"designacao": "vida", "descricao":"a vida é"}
    db[data["designacao"]] = data["descricao"]
    f_out= open("conceitos_.json", "w", encoding="utf-8")
    json.dump(db,f_out,indent=4,ensure_ascii=False)
    f_out.close()
    #form data
    return data

@app.post("/conceitos/<designacao>")
def api_conceito(designacao):
    
    return {"designacao": designacao, "descricao":db[designacao]}



@app.route('/conceitos/<designacao>')
def conceitos_descricao(designacao):
    descricao = db[designacao]
    return render_template('conceitos_descricao.html', designacao=designacao, descricao=descricao)

app.run(host="localhost", port=4002, debug=True)