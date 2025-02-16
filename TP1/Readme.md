
# TPC1 Exercícios de Manipulação de Strings em Python

### 1. Reverse String  
**Descrição:** Inverte a string dada.  
**Input:** Uma string `s`.  
**Output:** A string invertida.  
**Exemplo:**  
Input: aMoR
Output: RoMa


### 2. Contagem de 'a' e 'A'  
**Descrição:** Conta o número de caracteres 'a' e 'A' na string.  
**Input:** Uma string `s`.  
**Output:** Um tuplo com a contagem de 'a' e 'A'.  
**Exemplo:**  
Input: AnabelA e a anA
Output: (4, 2)

### 3. Contagem de Vogais  
**Descrição:** Conta o número total de vogais na string (a, e, i, o, u).  
**Input:** Uma string `s`.  
**Output:** Um inteiro com o número de vogais.  
**Exemplo:**  
Input: AnabelA e a anA
Output: 10

### 4. Converter para Minúsculas  
**Descrição:** Converte todos os caracteres da string para minúsculas.  
**Input:** Uma string `s`.  
**Output:** A string em minúsculas.  
**Exemplo:**  
Input: AnabelA e a anA
Output: anabela e a ana

### 5. Converter para Maiúsculas  
**Descrição:** Converte todos os caracteres da string para maiúsculas.  
**Input:** Uma string `s`.  
**Output:** A string em maiúsculas.  
**Exemplo:**  
Input: AnabelA e a anA
Output: ANABELA E A ANA

### 6. Verificar Capicua  
**Descrição:** Verifica se a string é capicua (lê-se igual de trás para frente).  
**Input:** Uma string `s`.  
**Output:** `True` se for capicua, caso contrário `False`.  
**Exemplo:**  
Input: 5321235
Output: True

Input: amor
Output: False

### 7. Strings Balanceadas  
**Descrição:** Verifica se todos os caracteres de `s1` estão presentes em `s2`.  
**Input:** Duas strings `s1` e `s2`.  
**Output:** `True` se estiverem balanceadas, caso contrário `False`.  
**Exemplo:**  
Input: ('abc', 'cab')
Output: True

Input: ('abc', 'xyz')
Output: False

### 8. Número de Ocorrências  
**Descrição:** Conta quantas vezes a string `s1` aparece em `s2`.  
**Input:** Duas strings `s1` e `s2`.  
**Output:** Número de ocorrências de `s1` em `s2`.  
**Exemplo:**  
Input: ('is', 'This is a test.')
Output: 1

Input: ('an', 'Ana banana')
Output: 3

### 9. Anagramas  
**Descrição:** Verifica se `s1` é um anagrama de `s2`.  
**Input:** Duas strings `s1` e `s2`.  
**Output:** `True` se forem anagramas, caso contrário `False`.  
**Exemplo:**  
Input: ('listen', 'silent')
Output: True

Input: ('hello', 'world') 
Output: False

### 10. Tabela de Classes de Anagramas  
**Descrição:** Dado um dicionário (lista de palavras), calcula a tabela das classes de anagramas, agrupando palavras que são anagramas entre si.  
**Input:** Uma lista de palavras `L`.  
**Output:** Um dicionário com chaves ordenadas e listas de anagramas.  
**Exemplo:**  

Input: L = ["listen", "silent", "enlist", "rat", "tar", "art", "god", "dog"]
 
Output: {'eilnst': ['listen', 'silent', 'enlist'], 'art': ['rat', 'tar', 'art'], 'dgo': ['god', 'dog']}


