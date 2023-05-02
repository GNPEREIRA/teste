#questão 1:
indice = 13
soma = 0
k = 0
while(k<indice):
    k=k+1
    soma = soma + k

print(soma)

print(50 * '*')

#Questão 2:
def sequencia_fibonacci(num):
    lista_fibonacci = [0, 1]
    while(lista_fibonacci[-1] < num):
        lista_fibonacci.append(lista_fibonacci[-1] + lista_fibonacci[-2])
    if num in lista_fibonacci:
        print(f'{num} pertence a sequência Fibonacci')
        print(lista_fibonacci)
    else:
        print(f'{num} não pertence a sequência Fibonacci')
        print(lista_fibonacci)

    return lista_fibonacci

sequencia_fibonacci(23)

print(50 * '*')

#Questão 5:
def inverte_palavra(palavra):
    lista= []
    cont = -1
    for letra in palavra:
        lista.append(palavra[cont])
        cont += -1
    nova_palavra = ''.join(lista)
    print(nova_palavra)

inverte_palavra('gustavo')