# lista ordenada a partir do metodo sorted()

# 1. lista numerica
lista_num = [55, 70, 89, 13, 5, 2, 1, 6, 4, 120, 350, 445]

# sorted() eh uma funcao embutida no python
# aceita uma lista e retorna ela em ordem
numeros_ordenados = sorted(lista_num) # do menor para  o maior Crescente

numeros_ordenados2 = sorted(lista_num, reverse=True) # do maior para o menor Descrescente

print(numeros_ordenados)
print(numeros_ordenados2)
