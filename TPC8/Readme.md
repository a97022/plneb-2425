# TPC8 - Extração de Informações de Doenças

## Funções Principais

### 1. `doencas_letra(letra)`
**Objetivo:**  
- Para uma dada letra, acessar a página que lista os termos correspondentes e extrair para cada termo:
  - **Designação:** O nome do termo (doença).
  - **Resumo:** Um resumo curto extraído da listagem.
  - **URL detalhado:** O link para a página completa do termo.
- Chamar a função `get_doenca_info(url)` para obter informações detalhadas de cada termo.
- Organizar e armazenar todas as informações coletadas em um dicionário global (`doencas`).

**Resumo do Funcionamento:**  
- Constrói a URL específica para a letra, faz a requisição e processa o HTML resultante.
- Para cada elemento que representa um termo (identificado pela classe `views-row`):
  - Extrai a designação e o link contido na tag `<a>`.
  - Constrói a URL completa para a página do termo e chama `get_doenca_info(url)` para extrair detalhes.
  - Reúne o resumo e as informações detalhadas, armazenando-as no dicionário `doencas`.

---

### 2. `get_doenca_info(url_href)`
**Objetivo:**  
- Acessar a página individual de um termo (doença) e extrair informações detalhadas sobre o conteúdo clínico.
- Organizar os dados extraídos em um dicionário com chaves como:
  - **resumo:** Texto introdutório.
  - **causas:** Informações sobre as causas, que podem incluir parágrafos.
  - **sintomas:** Estruturados em uma parte textual e, se disponíveis, em listas de sintomas.
  - **diagnostico:** Detalhes sobre o diagnóstico da doença.
  - **tratamento:** Descrição do tratamento proposto.
  - **artigos_relacionados:** Links e títulos de artigos relacionados à doença.
  - **nota:** Notas adicionais, caso existam.
  - **site:** URL da página da doença.

**Resumo do Funcionamento:**  
- Realiza uma requisição à URL da página do termo e usa BeautifulSoup para processar o HTML.
- Localiza a div principal (`node-doencas`) e extrai as informações das seções correspondentes.
- Utiliza um loop para coletar o conteúdo antes do primeiro `<h2>` e processa as seções seguintes com base no título de cada `<h2>`.

---

## Armazenamento dos Dados

Ao final do processo, o dicionário `doencas` contém os dados extraídos para cada termo, organizados em uma estrutura clara e consistente. Esse dicionário é, então, gravado num ficheiro JSON (`doencas_3.json`) utilizando a codificação UTF-8, facilitando sua utilização em futuras análises ou integrações.

```python
with open("doencas_3.json", "w", encoding="utf-8") as f_out:
    json.dump(doencas, f_out, indent=4, ensure_ascii=False)