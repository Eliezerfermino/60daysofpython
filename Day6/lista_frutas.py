# Lista de frutas

frutas = ["banana", "maca", "uva", "morango", "abacate", "melancia", "laranja", "manga"]

for fruta in frutas:
    print(fruta)
    
# Utilizando Input para criar a lista de frutas

frutas = []

while True:
    fruta = input("Digite o nome da fruta! \nOu digite sair para terminar o programa! ").title()
    if fruta == "Sair":
        print(frutas)
        break
        
    frutas.append(fruta)
    
    print(fruta)
    
    



