import re

file =open("C:/Users/maria/Desktop/Universidade/2semestre/PLN/git_stor/plneb-2425/data/dicionario_medico.txt", encoding="utf-8")
texto= file.read()

#limpeza, retirar os \f
texto = re.sub(r'\f',"",texto)
#print(texto)

#colocar marca única nos nomes dos conceitos
texto= re.sub(r"\n\n","\n\n@",texto)
#print(texto)

'''conceito=[]
descricao=[]
#conceito = re.findall(r'@\w+', texto)
descricao = re.findall(r'^\w+@', texto)
print(descricao)'''



#extrair conceitos
conceitos_texto= re.split(r"\n\n@",texto)
#print(conceitos_texto)

conceitos_list=[]
for c in conceitos_texto:
    print(c)
    conceito_raw = re.split(r'\n',c,maxsplit=1)
    if len(conceito_raw) > 1:
        designacao, descricao = conceito_raw
        descricao= re.sub(r'\n'," ",descricao)
        #conceito = re.split(r"\n",c)
        conceitos_list.append((designacao,descricao))
    else:
        pass
    

print(conceitos_list)
file.close()