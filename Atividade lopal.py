'''
contador_multiplos_3 = 0

for _ in range(10):
    if int(input("Digite um número: ")) % 3 == 0:
        contador_multiplos_3 += 1

print(f"Quantidade de múltiplos de 3: {contador_multiplos_3}")

'''



contador = 0

for num in range(10):
    resposta = int(input("Digite um número: "))
    if resposta % 3 == 0:
        contador += 1
print(f"Quantidade de números multiplos {contador}")