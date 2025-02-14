#Exercicios aula0

#Programa que pergunta ao utilizador o nome e imprime em maiúsculas
def nome ():
    nome = input("qual o teu nome? ")
    print(nome.upper())

#nome()

#Funcao que recebe array de numeros e imprime numeros pares
array = [1,2,3,4,5,6,7,8,9,10]
lista=[]
def pares(array):
    for i in array:
        if i%2==0:
            lista.append(i)
            i= i+1
    print (lista)

#pares(array)

#funcao que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa
file= "C:/Users/maria/Desktop/Universidade/2semestre/PLN/plneb-2425/ola.txt"
def linhas_inversas(file):
    file = open(file)
    line = file.readlines()
    print(line[::-1])

#linhas_inversas(file)

#funcao que recebe nome de ficheiro e imprime numero de ocorrencias das 10 palavras mais frequentes no ficheiro

def ocorrencias(file): #CORRIGIR
    dic={}
    file =open(file)
    for line in file:
        words = line.split()
        for word in words:
            if word not in dic:
                occ=1
                dic[word] = occ
            else:
                occ = occ + 1
                dic[word]= occ
    print (dic)

ocorrencias(file)

from collections import Counter

def ocorrencias(file_path):
    dic = Counter()  # Usamos Counter() para contar ocorrências de forma eficiente
    
    with open(file_path, "r", encoding="utf-8") as f:  # Garantir fecho correto do ficheiro
        for line in f:
            palavras = line.split()  # Dividir a linha em palavras
            dic.update(palavras)  # Atualizar contador com as palavras da linha
    
    # Obter as 10 palavras mais frequentes
    palavras_mais_frequentes = dic.most_common(10)

    # Imprimir as palavras mais frequentes e o número de ocorrências
    for palavra, ocorrencias in palavras_mais_frequentes:
        print(f"{palavra}: {ocorrencias}")




#Funcao que recebe um texto como argumento e o "limpa": separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc

#def limpa(file):
