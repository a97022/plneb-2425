#Create a function that:
 #1. given a string “s”, reverse it.

def reverse_s(s):
    return(s[::-1])
reverse_s('aMoR')

 #2. given a string “s”, returns how many “a” and “A” characters are present in it.

def contA(s):
    c_a= s.count('a')
    c_A= s.count('A')
    print(f'Dada a string: "{s}", contamos {c_a} letras "a" e {c_A} letras "A".')
contA('AnabelA e a anA comem anAnas')

 #3. given a string “s”, returns the number of vowels there are present in it.

def conta_vogais(s):
    s = s.lower()
    vogais = 'aeiou'
    c_v=0
    for vogal in vogais:
        if vogal in s:
            c_v= s.count(vogal) + c_v
    return c_v
conta_vogais('AnabelA e a anA comem anAnas')

 #4. given a string “s”, convert it into lowercase.

def lower_that_string(s):
    s = s.lower()
    return s
lower_that_string('AnabelA e a anA comem anAnas')

 #5. given a string “s”,  convert it into uppercase.

def upper_that_string(s):
    s = s.upper()
    return s
upper_that_string('AnabelA e a anA comem anAnas')

 #6. Verifica se uma string é capicua

def capicua(s):
    s = s.lower()
    inv_s = reverse_s(s)
    if inv_s  == s:
        return True
    return False
capicua('5321235')

 #7. Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2.)

def balanceadas(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for l in s1:
        if l not in s2:
            return False
    return True
balanceadas('abc','cab')
            
 #8. Calcula o número de ocorrências de s1 em s2

def occ(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return s2.count(s1)

print(occ('listen', 'silent')) 
print(occ('is', 'This is a test. Is it working?'))  
print(occ('an', 'Ana banana'))  

 #9. Verifica se s1 é anagrama de s2. 

def anagrama(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if sorted(s1) == sorted(s2):
        return True
    return False

anagrama('listen','silent')
anagrama('hello','world')

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
print(tabela_anagramas(L))

