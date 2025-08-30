mult = 0
while True:
    n1 = float(input('Qual valor voce deseja ver a tabuada ? (use o ponto como virgula e numero negativo para cancelar) '))
    if n1 < 0:
         break
    print ('='*20)
    for c in range(0, 11):
         mult = n1 * c
         print (f'{n1} x {c} = {mult:.2f} ')
    print ('='*20)
print ('Tabuada encerrada, tenha um otimo dia ')
