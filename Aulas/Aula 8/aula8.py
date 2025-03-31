from bs4 import BeautifulSoup
import requests
import json


def doencas_letra(letra):

    url= "https://www.atlasdasaude.pt/doencasAaZ/" 
    response = requests.get( url + letra)
    html_content = response.text
    soup= BeautifulSoup(html_content, 'html.parser')


    doencas= {}

    for div_row in soup.find_all("div", class_="views-row"):

        designacao = div_row.div.h3.a.text.strip()
        #print(designacao)
        desc_div= div_row.find("div", class_="views-field-body")

        desc= desc_div.div.text

        #if desc_div.div.p:
        #   desc = desc_div.div.p.text
        #elif desc_div.div.div:
        #   desc = desc_div.div.div.text

        doencas[designacao] = desc.strip().replace(" "," " )
    return doencas

res={}
for a in range(ord("a"), ord("z") +1):
    letra = chr(a)
    res = res | doencas_letra(letra)
    

f_out = open("doencas_.json", "w", encoding="utf-8")
json.dump(res, f_out, indent=4, ensure_ascii=False)
f_out.close()




