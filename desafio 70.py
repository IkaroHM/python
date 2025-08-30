acum = 0
cont = 0
maisbarato = ''
precomaisbarato = 0
print ('='*20)
print ('Super Mais Barato ')
print ('='*20)
while True:
    nomeproduto = input('Qual o nome do produto ? ')
    preco = float(input('Qual o preco do produto ? '))
    acum += preco
    if precomaisbarato == 0 or preco < precomaisbarato:
        precomaisbarato = preco
        maisbarato = nomeproduto
    if preco >= 1000:
        cont += 1
    print ('='*20)
    soun = input('Deseja continuar ? (S/N) ').upper().strip()
    if soun == 'N':
        break
print ('='*20)
print (f'ao todo voce gastou {acum} reais ')
print (f'voce comprou {cont} produtos de mais de 1000 (mil) reais')
print (f'o produto mais barato foi o/a {maisbarato}')
