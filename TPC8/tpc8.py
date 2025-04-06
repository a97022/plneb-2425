from bs4 import BeautifulSoup
import requests
import json 

def get_doenca_info(url_href):
    url_doenca = "https://www.atlasdasaude.pt" + url_href 
    response = requests.get(url_doenca)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    div_content = soup.find("div", class_="node-doencas")
    
    if not div_content:
        return {
            "resumo": "Não disponível",
            "causas": "Não disponível",
            "sintomas": ["Não disponível", []],
            "diagnostico": "Não disponível",
            "tratamento": "Não disponível",
            "artigos_relacionados": {},
            "nota": "Não disponível",
            "site": url_doenca
        }
    
    # Extração das informações
    resumo_div = div_content.find("div", class_="field-name-body")
    causas = div_content.find("strong", string="Causas")
    sintomas = div_content.find("strong", string="Sintomas")
    diagnostico = div_content.find("strong", string="Diagnóstico")
    tratamento = div_content.find("strong", string="Tratamento")
    nota = div_content.find("div", class_="field-name-field-nota")
    artigos_relacionados_span = div_content.find("span", string="Artigos relacionados")
    
    resumo_text = resumo_div.get_text(strip=True) if resumo_div else "Não disponível"
    causas_text = causas.find_next("p").get_text(strip=True) if causas else "Não disponível"
    
    # Extração dos sintomas como lista
    sintomas_list = []
    if sintomas:
        ul = sintomas.find_next("ul")
        if ul:
            for item in ul.find_all("li"):
                sintomas_list.append(item.get_text(strip=True))
    
    diagnostico_text = diagnostico.find_next("p").get_text(strip=True) if diagnostico else "Não disponível"
    tratamento_text = tratamento.find_next("p").get_text(strip=True) if tratamento else "Não disponível"
    nota_text = nota.get_text(strip=True) if nota else "Não disponível"
    
    # Extração dos artigos relacionados
    artigos_relacionados_dict = {}
    if artigos_relacionados_span:
        for artigo in artigos_relacionados_span.find_next_siblings("h3"):
            artigo_title = artigo.get_text(strip=True)
            artigo_url = artigo.find("a")["href"]
            artigos_relacionados_dict[artigo_title] = artigo_url
    
    return {
        "resumo": resumo_text,
        "causas": causas_text,
        "sintomas": [sintomas_list, []],
        "diagnostico": diagnostico_text,
        "tratamento": tratamento_text,
        "artigos_relacionados": artigos_relacionados_dict,
        "nota": nota_text,
        "site": url_doenca
    }

def doencas_letra(letra):
    url = "https://www.atlasdasaude.pt/doencasaaz/" + letra
    print(url)
    response = requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    doencas = {}
    for div_row in soup.find_all("div", class_="views-row"):
        designacao = div_row.div.h3.a.text.strip()
        doenca_url = div_row.div.h3.a["href"]
        doenca_info = get_doenca_info(doenca_url)
        doencas[designacao] = doenca_info  
            
    return doencas

res = {}
for a in range(ord("a"), ord("z") + 1):
    letra = chr(a)
    res = res | doencas_letra(letra)
    
#print(res)
with open("doencas_tpc.json", "w", encoding="utf-8") as f_out:
    json.dump(res, f_out, indent=4, ensure_ascii=False)