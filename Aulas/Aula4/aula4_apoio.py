import re
import json

file =open("C:/Users/maria/Desktop/Universidade/2semestre/PLN/git_stor/plneb-2425/data/dicionario_medico.xml", encoding="utf-8")
texto= file.read()
file.close()

#limpeza, retirar as page info
texto = re.sub(r'</?page(.*)',"",texto)
texto = re.sub(r'</?text.*?>',"",texto)

conceitos = re.findall(r'<b>(.*)</b>\n([^<]*)',texto)

def limpa_descricao(desc):
    desc=desc.strip()
    desc=re.sub(r'\n',"",desc)
    return desc

#conceitos_dict={designacao : limpa_descricao(descricao) for designacao, descricao in conceitos}
conceitos_dict={}

for designacao, descricao in conceitos:
    if designacao in conceitos_dict:
        conceitos_dict[designacao] += " @ " + limpa_descricao(descricao)
    else:
        conceitos_dict[designacao] = limpa_descricao(descricao)


file_out = open("conceitos.json","w", encoding="utf-8")
json.dump(conceitos_dict)

print(conceitos_dict)