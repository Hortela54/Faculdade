valor = 0
#Apresentação e opções de escolha do usuario
print('Bem vindo a Lanchonete do Samuel(3892265)')
print('              ****Cardápio****             ')
print('| Código |        Descrição       | Valor |')
print('|   100  |     Cachorro Quente    | 9,00  |')
print('|   101  | Cachorro Quente duplo  | 11,00 |')
print('|   102  |        X-Egg           | 12,00 |')
print('|   103  |        X-Salada        | 12,00 |')
print('|   104  |        X-Bacon         | 14,00 |')
print('|   105  |        X-Tudo          | 17,00 |')
print('|   200  |    Refrigerante Lata   | 5,00  |')
print('|   201  |       Chá Gelado       | 4,00  |')
print('|    0   |          Sair          | 0,00  |')

while True:   
    cod = int(input('Digite o Código do item desejado: ')) #Pede para o usuario inserir o codigo do item.
    if(cod == 100): #Começa a cadeia de IF para verificar o que o usuario escolheu.
        print("Você pediu um Cachorro Quente no valor de 9,00")
        valor += 9 # adiciona o valor do produto, que vai sendo iterado a cada item adicionado 
    elif(cod == 101):
        print("Você pediu um Cachorro Quente Duplo no valor de 11,00")
        valor += 11
    elif(cod == 102):
        print("Você pediu um X-Egg no valor de 12,00")
        valor += 12         
    elif(cod == 103):
        print("Você pediu um X-Salada no valor de 12,00")
        valor += 12  
    elif(cod == 104):
        print("Você pediu um X-Bacon no valor de 14,00")
        valor += 14
    elif(cod == 105):
        print("Você pediu um X-Tudo no valor de 17,00")
        valor += 17
    elif(cod == 200):
        print("Você pediu um Fefrigerante Lata no valor de 5,00")
        valor += 5 
    elif(cod == 201):
        print("Você pediu um Chá Gelado no valor de 4,00")
        valor += 4      
    elif(cod == 0):  
        print('Encerrando o programa') #Se o usuario não quiser fazer nada ele digita 0 e o programa fecha.
        break
    else:
        print('Opção invalida') #Se for digitado um valor fora da lista apresentada à o usuario, o programa vai dar opção invalida
    qst = int(input('Você deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n'))#Pergunta para o usuario se ele quer adicionar mais um item, repetindo os IFs com o continue
    if(qst == 1):
        continue #Fazendo o laço repetir
    else:
        break #Quebrando o laço
print('O total a ser pago é: {} reais'.format(valor)) # Demonstra um somatorio de todos os itens adicionados

        


