from flask import Flask, request, render_template
import json
import re

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

@app.route("/conceitos")
def adicionar_conceito():
    descricao=request.form.get("descricao")
    designacao=request.form.get("designacao")

    db[designacao] = descricao
    f_out = open("conceitos_.json", "w")
    json.dump(db,f_out,indent=4,ensure_ascii=False)
    f_out.close()
    #form data

    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos") 
    

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
def api_conceito_designacao(designacao):
    if designacao in db:
        return render_template("conceitos_descricao.html", designacao=designacao, descricao=db[designacao], title="Conceito e desginação")
    else:
        return render_template("conceitos_descricao.html", designacao="Not Found", descricao="Not Found",title="Conceito e desginação")

@app.route('/conceitos/<designacao>')
def conceitos_descricao(designacao):
    descricao = db[designacao]
    return render_template('conceitos_descricao.html', designacao=designacao, descricao=descricao)

def find_conceito(db,query,word_bound,case_sensitive):
    res=[]
    if word_bound == "on":
        pattern= r"\b(" + query +r")\b"
    else:
        pattern= r"(" + query +r")"
    if case_sensitive == "on":
        flags = 0
    else:
        flags = re.IGNORECASE

for designacao, descricao in db.items():
    if re.search(pattern, designacao, flags) or re.search(pattern, descricao, flags):
        bold_designacao = re.sub(pattern, r"<strong> \1</strong>", designacao, flags)
        bold_descricao = re.sub(pattern, r"<strong> \1</strong>", descricao, flags)
        res.append((designacao, bold_designacao, bold_descricao))

@app.get("/pesquisa")
def pesquisa():
    query= request.args.get("query")
    word_bound=request.args.get("word_bound")
    case_sensitive=request.args.get("case_sensitive")

    if not query:
        return render_template("pesquisa.html", title="Pesquisa")
    
    res= find_conceito(db,query,word_bound,case_sensitive)
    return render_template("pesquisa.html", conceitos=res, query=query, word_bound=word_bound, case_sensitive=case_sensitive, title="Pesquisa")


app.run(host="localhost", port=4002, debug=True)