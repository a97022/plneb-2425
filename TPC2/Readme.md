
# TPC2 Exercícios de Expressões Regulares

## 1.1 Hello no início da linha 
**Descrição:** Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece no início da linha.  
- **expressão regular:** re.match(r'^hello', s)

## 1.2. Encontrar a palavra hello 
**Descrição:** Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece em qualquer posição da linha.  
- **expressão regular:** re.search(r'hello', s)  
- **comentário:** usa-se o search para encontrar o padrão independentemente da sua localização no texto, ao contrário do match que apenas verifica o início do mesmo

## 1.3. Hhello
**Descrição:** Dada uma linha de texto, este é o programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, admitindo que a palavra seja escrita com maiúsculas ou minúsculas.  
- **expressão regular:** re.findall(r"hello", s, re.IGNORECASE)  
- **comentário:** neste exercício aprendi uma nova forma de tornar a expressão regular case-insensitive, com o uso de (?i:...).  
(?i: ... ): É um grupo de modificação que aplica a flag i (case-insensitive) apenas ao conteúdo entre os dois pontos e o parêntesis final.


## 1.4. YEP 
**Descrição:** Dada uma linha de texto, este é o programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, substituindo cada uma por "\*YEP\*".  
- **Expressão Regular:** re.sub(r'hello', '*YEP*', s,flags=re.IGNORECASE) 


## 1.5. Vírgulas  
**Descrição:** Dada uma linha de texto, este é o programa que pesquisa por todas as ocorrências do caracter vírgula, separando cada parte da linha por esse caracter.   
- **Expressão regular:** re.split(r',', s)   
- **comentário:** se quisesse separar por vírgulas e ainda retirar os whitespaces, podia adicionar um .strip()


## 2. Por favor 
**Descrição:** Função `palavra_magica` que recebe uma frase e determina se a mesma termina com a expressão "por favor", seguida de um sinal válido de pontuação.  
- **Expressão Regular:** re.search(r'por favor[\.,?!]+$', frase)

## 3. Contar eus  
**Descrição:** Função `narcissismo` que calcula quantas vezes a palavra "eu" aparece numa string.  
- **Expressão  Regular:** re.findall(r'eu',linha,flags=re.IGNORECASE)


## 4. Trocar de Curso
**Descrição:** Função `troca_de_curso` que substitui todas as ocorrências de "LEI" numa linha pelo nome do curso dado à função.  
- **Expressão Regular:** re.sub(r'LEI', novo_curso, linha)  
- **input:** troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", 'Engenharia Biomédica')  
- **output:** Engenharia Biomédica é o melhor curso! Adoro Engenharia Biomédica! Gostar de Engenharia Biomédica devia ser uma lei.


## 5. Somar strings  
**Descrição:** Função `soma_string` que recebe uma string com vários números separados por uma vírgula (e.g., "1,2,3,4,5") e devolve a soma destes números.   
- **Expressão Regular:** re.findall(r'-?\d+',linha)


## 6. Pronomes
**Descrição:** Função `pronomes` que encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu", "ele", "ela", etc., com atenção para letras maiúsculas ou minúsculas.  
- **Expressão Regular:** re.findall(lista_pronomes, frase, re.IGNORECASE)  
- **comentário:** Neste exercício quis criar uma lista de todos os pronomes e arranjar uma maneira de a incluir na expressão regular. Aprendi 2 maneiras diferentes para o mesmo efeito: criar a lista já em raw string para facilitar a sua implementação na expressão ou utilizar o join para concatnar uma lista de strings numa expressão regular.  
- **Exemplo:**     lista_pronomes = r'\b(eu|tu|ele|ela|nós|vos|eles|elas|vós|mim|me|te|ti|o|a|nos|vos|lhe|lhes|se|si)\b'  

PRONOMES_PESSOAIS = [
    "eu", "tu", "ele", "ela", "nós", "vós", "eles", "elas", 
    "mim", "me", "te", "ti", "o", "a", "nos", "vos", "lhe", "lhes", "se", "si"
]

## 7. Variáveis Válidas 
**Descrição:** Define a função `variavel_valida` que recebe uma string e determina se a mesma é um nome válido para uma variável, ou seja, se começa por uma letra e apenas contém letras, números ou *underscores*.  
- **Expressão Regular:**re.match(r'^[A-Za-z][A-Za-z0-9_]*$', linha)  
- **comentário:** Neste exercício fiquei a conhecer uma nova função reggex, a fullmatch que verifica e apenas procura a string que corresponder extamente ao padrão pedido, poderia substituir neste caso o uso de ^ e $.

## 8. Inteiros 
**Descrição:** Função `inteiros` que devolve todos os números inteiros presentes numa string. Um número inteiro pode conter um ou mais dígitos e pode ser positivo ou negativo.  
- **Expressão Regular:** re.findall(r'[^0-9a-zA-Z_\.](-?\d+)\b(?!\.)',linha)  
- **comentário:** Este exercício deu trabalho...a expressão regular para número positivo ou negativo foi fácil de alcançar, '-?\d+'.  Contudo, não queria que a expressão validasse números decimais nem números que estivessem na composição de palavras. Por esse motivo, pensei em usar \b para limitar a busca por apenas números isolados mas não foi suficiente.  
Queria que a função fosse capaz de reconhecer o ponto (.) e não o considerasse, para isso aprendi novos conceitos: **negative lookbehind** e o **negative lookahead**. O primeiro verifica se o caractere imediatamente à esquerda do padrão não é, neste caso, o ponto; o negative lookahead garante que após o padrão não aparece, neste caso, um ponto (.).  
Estes dois conceitos levaram a minha expressão regular a ser capaz de retornar um output muito satisfatório contra a minha string de teste.

- **input:** inteiros("4,-6,2,3,8,-3,0,2,-5,1,maria,ines,2023,18fevereiro,0.35,leonor_98,xavier43")  
- **output:** ['-6', '2', '3', '8', '-3', '0', '2', '-5', '1', '2023']

## 9. Underscores 
**Descrição:** Função `underscores` que substitui todos os espaços numa string por *underscores*. Se aparecerem vários espaços seguidos, devem ser substituídos por apenas um *underscore*.  
- **Expressão  Regular:** re.sub(r'[ ]+','_',linha)  
- **comentário:** também poderia ter usado \s para referenciar whitespaces; usei o símbolo + para evidenciar que ao encontrar um ou mais whitespaces, a funcção deveria substituí-los por apenas 1 underscore.

## 10. Codigos Postais
**Descrição:** Função `codigos_postais` que recebe uma lista de códigos postais válidos e divide-os com base no hífen. A função devolve uma lista de pares.  
- **Expressão Regular:** re.split(r'-', codigo)



