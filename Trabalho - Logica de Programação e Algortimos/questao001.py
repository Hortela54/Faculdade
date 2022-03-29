print('Bem Vindo a Loja do Samuel(3892265)') # RU: 3892265
valor = float(input("Digite o valor do produto: ")) # Valor do produto
qtd = float(input("Digite a quantidade de produtos: ")) # Quantidade de produtos

if qtd <= 9:
    print('O valor sem desconto é {:.2f}'.format(valor)) # Valor até nove os produtos é 0% de desconto
    
elif qtd >= 10 and qtd < 99:
    valortotal = valor*qtd #Calculo do valor total dos produtos vezes a quantidade
    desconto = valortotal-(valortotal*0.05) #Aplicando o desconto em cima do valor total da compra
    print('O valor sem desconto foi: {}\nO Valor com desconto foi: {}'.format(valortotal, desconto))
    
elif qtd >= 100 and qtd < 999:    
    valortotal = valor*qtd
    desconto = valortotal-(valortotal*0.10)
    print('O valor sem desconto foi: {}\nO Valor com desconto foi: {}'.format(valortotal, desconto))
    
elif qtd > 1000:  
    valortotal = valor*qtd
    desconto = valortotal-(valortotal*0.15)
    print('O valor sem desconto foi: {}\nO Valor com desconto foi: {}'.format(valortotal, desconto))
    