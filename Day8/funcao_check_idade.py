def podedirigir(idade):
    if idade >= 18:
        return True
    else:
        return False
    
    
try:
    input_user = int(input("Digite a sua idade: "))
    print(podedirigir(input_user))
except ValueError:
    print("Entrada invalida. Por favor, digite um numero inteiro.")