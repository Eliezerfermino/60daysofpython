numero = input("Digite o numero: ")

try: # tente rodar
    numero = int(numero)
    if numero % 2  == 0:
        print(f"Numero par")
    else:
        print(f"Numero impar")
except ValueError:
    print("Voce não digitou um numero correto")
           