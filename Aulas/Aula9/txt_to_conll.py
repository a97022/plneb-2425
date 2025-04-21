import spacy
import sys

nlp= spacy.load('pt_core_news_lg')
nlp.add_pipe("merge_entities")
doc1= nlp("""O Manuel da Silva gosta de papas de sarrabulho e francesinhas.
Faz ele muito bem.
O Presidente da Câmara de Vila Nova de Famalicão.""")

def main():
    file = sys.argv[1]
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    doc= nlp(text)
    n=1
    for frase in doc.sents:
        print(f"# {n}")
        for p in frase:
            if p in frase:
                if p.pos_ != "SPACE":
                    if p.ent_type_:
                        print(p.text, "|", p.pos_, "|", p.ent_type_)
                    else:
                        print(p.text, "|", p.pos_, "|", p.lemma)
        n+=1


if __name__ == "__main__":
    main()
