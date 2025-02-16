#Create a function that:
 #1. given a string “s”, reverse it.

s='AnabelA e a anA comem anAnas'
ss= 'aMor'

def reverse_s(s):
    return(s[::-1])

print(f'Ex1: string: {ss} \nreversed string: {reverse_s(ss)}')

 #2. given a string “s”, returns how many “a” and “A” characters are present in it.

def contA(s):
    c_a= s.count('a')
    c_A= s.count('A')
    return (c_a,c_A)

print(f'Ex2: Dada a string: "{s}", contamos {contA(s)[0]} letras "a" e {contA(s)[1]} letras "A".')

 #3. given a string “s”, returns the number of vowels there are present in it.

def conta_vogais(s):
    s = s.lower()
    vogais = 'aeiou'
    c_v=0
    for vogal in vogais:
        if vogal in s:
            c_v= s.count(vogal) + c_v
    return c_v

print(f'Ex3: na string "{s}", existem {conta_vogais(s)} vogais')

 #4. given a string “s”, convert it into lowercase.

def lower_that_string(s):
    s = s.lower()
    return s
print(f'Ex4: string original: {s} \nstring in lowercase: {lower_that_string(s)}')

 #5. given a string “s”,  convert it into uppercase.

def upper_that_string(s):
    s = s.upper()
    return s

print(f'Ex5: string original: {s} \nstring in uppercase: {upper_that_string(s)}')

 #6. Verifica se uma string é capicua

def capicua(s):
    s = s.lower()
    inv_s = reverse_s(s)
    if inv_s  == s:
        return True
    return False

print(f'Ex6: A string "{s}" é capicua? {capicua('5321235')}')

 #7. Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2.)

s1= 'an'
s2= 'Ana banana'

def balanceadas(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for l in s1:
        if l not in s2:
            return False
    return True

print(f'Ex7: As strings "{s1}" e "{s2}" estão balanceadas? {balanceadas(s1,s2)}')
            
 #8. Calcula o número de ocorrências de s1 em s2

def occ(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return s2.count(s1)

print(f'Ex8: Número de ocorrências de "{s1}" em "{s2}": {occ(s1,s2)}')

 #9. Verifica se s1 é anagrama de s2. 

a1='listen'
a2='silent'
a3='hello'

def anagrama(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if sorted(s1) == sorted(s2):
        return True
    return False

print(f'Ex9: "{a1}" é anagrama de "{a2}"? {anagrama(a1,a2)}')
print(f'Ex9: "{a1}" é anagrama de "{a3}"? {anagrama(a1,a3)}')

 #10. Dado um dicionário, calcular a tabela das classes de anagramas.

def tabela_anagramas(L):
    tabela = {}
    for palavra in L:
        chave = ''.join(sorted(palavra))
        if chave not in tabela:
            tabela [chave] = []
        tabela[chave].append(palavra)
    return tabela

L = ["listen", "silent", "enlist", "rat", "tar", "art", "god", "dog"]
print(f'Ex10: tabela de classes de anagramas: {tabela_anagramas(L)}')

