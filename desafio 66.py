cont = 0
acum = 0
while True:
    n1 = float(input('Insira um número (999 para parar) '))
    if n1 == 999:
        break
    acum += n1
    cont += 1
print (f'Voce inseriu {cont} números e a soma deles é {acum:.2f}')
