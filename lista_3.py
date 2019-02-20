#Criar uma lista de 5 numeros inteiros, definidos pelo usuário
#e exibir seus valores nas respectivas posições

valores = list()#declarando uma lista
#looping de 0 a 4 (5 numeros)
for i in range(0, 5):
    #numero a ser inserido na lista
    numero = int(input(f'Insira o {i+1}º numero: '))
    #se for o primeiro da lista ou último
    if i == 0 or numero > max(valores):
        #insere na lista
        valores.append(numero)
        #retorna para o primeiro looping
        continue
    #se i > 0, para todos os valores da lista
    for j in range(0, len(valores)):
        #se o numero atual for menor que o valor atual da lista
        #e se este numero já não existe na lista
        if numero < valores[j] and numero not in valores:
            #insere na lista, na posição do primeiro valor
            #da lista maior que este numero
            valores.insert(j, numero)
#fim do looping
print(f'Os valores digitados foram {valores}')