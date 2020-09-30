"""
Escreva um algoritmo que exiba todos os
números PARES de 0 até 100.
"""
cont = 0

while(cont <= 100):
    
    if(cont%2 == 0):
        
        print(cont)
    
    cont = cont + 2
    
    
for x in range(0, 101):
    
    if(x%2 == 0):
        print(x)
        
"""
Escreva um algoritmo que exiba todos 
os números IMPARES entre os 
limites mínimo e máximo fornecidos pelo usuário.
"""        
inicio = int( input("Início: ") )
fim = int( input("Final: ") )

while(inicio <= fim):
    
    if(inicio%2 != 0):
        print(inicio)
        
    inicio = inicio + 1


inicio = int( input("Início: ") )
fim = int( input("Final: ") )

for x in range(inicio, fim+1):
    
    if(x%2 != 0):
        print(x)

"""
Escreva um algoritmo que permaneça solicitando
 números ao usuário até que ele forneça um número ímpar.
 Neste caso, finalize o programa.
"""
# Resposta do Gabriel
n = int(input("Digite um número:"))

while((n%2)==0):
    n = int(input("Digite OUTRO número: "))
    
print("\nNúmero impar detectado.")

# Resposta do Matheus
numero = 0

while(numero%2 != 1):
    numero = (int(input("Digite um número: ")))


"""
Escreva um algoritmo que solicite números
ao usuário até que ele informe um
número negativo ou zero. 
 
Neste caso, apresente na tela a soma de todos
os números válidos digitados
(números positivos informados).
"""

# Reposta do Gabriel
n = int(input("Digite um número:"))

s = 0

while(n>0):
    s += n # é a mesma coisa que s = s + n
    n = int(input("Digite outro número:"))
    
print("\nNúmero nulo ou negativo detectado, a soma é",s)

# Resposta do Matheus
numero = 1
soma = 0

while(numero >= 1):
    numero = int(input("Digite um número: "))
    if(numero >= 1):
        soma = soma + numero
        
print("A soma dos valores digitados é:",soma)








