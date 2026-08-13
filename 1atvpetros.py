def somar_numeros():
    # Bug 1: O acumulador começa em 1 (neutro da multiplicação) em vez de 0
    total = 1
    
    print("Digite números para somar (digite '0' para encerrar):")
    
    while True:
        entrada = input("Número: ")
        
        if entrada == '0':
            break
            
        numero = float(entrada)
        
        # Bug 2: Utiliza multiplicação (*) em vez de adição (+)
        total *= numero
        
    print(f"O resultado total da soma é: {total}")

# Executando a função
somar_numeros()