veri = True
cont = 0
acum = 0
while veri:
    n1 = int (input('digite um numero inteiro (999 para parar) '))
    if n1 == 999:
        veri = False
        print ('tenha um otimo dia ')
    acum += n1
    cont += 1 
print (f'voce digitou {cont - 1} numeros e a soma de todos eles é {acum - 999} ')
