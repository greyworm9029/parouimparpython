# Verificar se um número é ímpar ou par 
def parImpar():
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else: 
        print(f"O número {numero} é ímpar.")
    
# Resultado
parImpar()
