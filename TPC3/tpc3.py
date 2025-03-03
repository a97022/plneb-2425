import re

# Abrir ficheiro
file = open("C:/Users/maria/Desktop/Universidade/2semestre/PLN/git_stor/plneb-2425/data/dicionario_medico.txt", encoding="utf-8")
texto = file.read()

# Limpeza do ficheiro, remove caracteres \f (form feed), que são quebras de página 
texto = texto.replace("\f", "")

# Marcação dos conceitos
texto = re.sub(r"(\n\n)(.*)\n{1,}", r"\1@\2\n", texto)     

# Função para formatar a descrição
def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub(r'\n', " ", descricao)  
    return descricao

# Extração de conceitos 
conceitos_raw = re.findall(r'@(.*?)\n(.*?)(?=\n@|\Z)', texto)
conceitos = [(designacao.strip(), limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]    


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
f_out = open('tpc3.html','w', encoding="utf-8")
f_out.write(html)
f_out.close()
file.close()