cont = 0
acum = 0
maiorn = 0
soun = True
while soun:
    soun = input('deseja continuar ? (s/n) ').strip().upper()
    n1 = int(input('Insira um numero '))
    if soun == 'N':
        soun = False
    acum += n1
    cont += 1
    menorn = n1
    if n1 > maiorn:
        maiorn = n1
    if n1 < menorn:
        menorn = n1
media = acum / cont
print (f'voce digitou {cont} numeros e a media deles é {media} ')
print (f'o maior valor foi {maiorn} e o menor foi {menorn}')
    
