# Funcao simples em Python que recebe um numero e retorna o valor quadrado do mesmo

def quadrado_numero(numero):
    return numero ** 2

def quadrado_numerov2(numero):
    return numero * numero

numero = float(input("Digite um numero: "))

print(quadrado_numero(numero))
print(quadrado_numerov2(numero))