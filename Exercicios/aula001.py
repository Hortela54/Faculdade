#EXPRESSÕES ALGEBRICAS

# A)Somatorio dos 5 primeiros número interios e positivos
1 + 2 + 3 + 4 + 5
# B)Média de 23, 19, 31
(23+19+31)/3
# C)O numero de vezes que 73 cabe em 403
403//73
# D)A sobra quando 403 é dividido por 73
403%73
# E)2 elevado à 10 potencia 
2**10
# F)O valor absoluto da diferença entre 54 e 57 
abs(54-57)
# G)O menor valor entre 34, 29 e 31
min(34, 29, 31)

#ATRIBUIÇÃO 

a = 3
b = 4
c = a*a +b*b

#STRING

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

a1 = s1 + ' ' + s2 + ' ' + s3
a2 = (s1 + ' ')*10
a3 = (s1 + ' ' + s2 + ' ')*7
a4 = (s2 + s2 + s3 + ' ')*4

#EXERCICIOS

#Exercicio 1

preco = float(input('Qual o preço do produto?'))
desconto = float(input('Quanto de desconto?(0-100)'))
valortotal = preco*(desconto/100)
valor = preco - valortotal
print('O preço do produto é de {} reais, com desconto de {}%, que equivale a {} reais, totaliza {} reais'.format(preco,desconto, valortotal, valor))

#Exercicio 2

km = float(input('Quantos kms você anda com o carro alugado?'))
dias = int(input('Quantos dias você alugou o carro?'))
valor = (60 * dias) + (0.15 * km)
print('Com {} dias de aluguel, 60 reais a diaria, mais {}km rodados, 0.15 reais por Km rodado, totaliza {} reais'.format(dias,km, valor))

#Exercicio 3

palavra = input('Digite uma palavra')
tam = len(palavra)
palavra2 = palavra[:int(tam/2)]
print(palavra2[-2:])

