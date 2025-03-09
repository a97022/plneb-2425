import re
import json

file = open("git_stor/plneb-2425/data/LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="utf-8")
texto = file.read()
#print(texto)

file_conceitos = open("Aula4/conceitos.json", encoding="utf-8" )
conceitos = json.load(file_conceitos)
file_conceitos.close()

#limpar
#texto = re.sub("\f","",texto)

black_list= ["de", "e", "para", "os"]

def gera_termo_bold(matched):
    text = matched.group(0)
    #print(text)
    if text in conceitos and text not in black_list:
        return f'<a href= "" title="{conceitos[text]}">{text}</a>'
    else:
        return text

texto = re.sub(r"\n", "<br>", texto)
texto = re.sub("\b(\w+)\b",gera_termo_bold,texto) #para ir palavra a palavra e ver se está no dicionário

file_html = open("Aula4/LIVRO-Doenças-do-Aparelho-Digestivo.html", "w", encoding="utf-8")
file_html.write(texto)

file.close()