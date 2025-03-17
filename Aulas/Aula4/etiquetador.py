import json
import re

file = open("git_stor/plneb-2425/data/LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="utf-8")
texto=file.read()
file.close()

with open("conceitos.json", "r", encoding="utf-8") as file_conceitos:
    conceitos = json.load(file_conceitos)

blacklist=["de","a","e","o","mas","para","este","os","as"]

def gera_termo_bold(matched):
    #print(matched)
    titulo = matched.group(0)
    if titulo in conceitos.keys() and titulo not in blacklist:
        return f"<a href='plneb-2425/Aulas/Aula3/dicionario_medico.html#{titulo}' target = '_blank' title='{conceitos[titulo]}'>{titulo}</a>" #vai buscar aos conceitos a definição do titulo
        #return f"<b>{titulo}</b>"
    else:
        return f"{titulo}"
    

texto = re.sub("\n","<br>",texto)

texto = re.sub(r"\f", "<hr>",texto)

texto=re.sub(r"\b(\w+)\b",gera_termo_bold,texto)

#print(repr(texto))

with open("dic_novo.html", "w", encoding="utf-8") as file_dic:
    file_dic.write(texto)
    file_dic.close()