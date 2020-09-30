
num = [0] * 10

for cont in range( 0, len(num) ):
    
    num[cont] = int(input("Digite um número: "))
    

m = num[0]

for cont in range(0, len(num)):
    
    if( num[cont] > m ):
        m = num[cont]


print("O maior valor encontrado é", m)


# Fazer tabuada do 1 ao 10 para todos os valores de um vetor
vetor = [5, 12, 4, 8]

for cont in range( 0, len(vetor) ):
      
    for n in range(1, 11):
        
        print(n, "*", vetor[cont], "=", n * vetor[cont])
        
    print("--------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    