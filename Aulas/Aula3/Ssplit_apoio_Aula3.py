import re

file =open("C:/Users/maria/Desktop/Universidade/2semestre/PLN/plneb-2425/Aulas/Aula3/dicionario_medico.txt", encoding="utf-8")
texto= file.read()

#limpeza, retirar os \f
texto = re.sub(r'\f',"",texto)
#print(texto)

#colocar marca única nos nomes dos conceitos
texto= re.sub(r"\n\n","\n\n@",texto)

def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub(r'\n', " ", descricao)
    return descricao

#extrair conceitos
conceitos_raw= re.findall(r'@(.*)\n([^@]*)', texto)
conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
print(conceitos)

#gerar HTML

def gera_html(conceitos):
    html_header = f"""
        <!DOCTYPE html>
            <head>
            <meta charset="UTF-8"/>
            </head>
            <body>
            <h3>Dicionário de conceitos Médicos</h3>
            <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/
            2025<p>
            """
    
    html_conceitos= ""

    for designacao, descricao in conceitos:
        html_conceitos += f"""
                    <div>
                    <p><b>{designacao}</b></p>
                    <p>{descricao}</p>
                    </div>
                    <hr/>
                """

    html_footer= """
        </body>
    </html>"""
    
    return html_header + html_conceitos + html_footer
html = gera_html(conceitos)
f_out = open('dicionario_medico.html','w', encoding="utf-8")
f_out.write(html)
f_out.close()
file.close()
