contm = 0
cont = 0
contf = 0
print ('='*20)
print ('Cadastrar pessoas ')
while True:
    print ('='*20)
    idade = int(input('Qual a idade ? '))
    sexo = input('qual o sexo (F/M) ').upper().strip()
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        contm += 1
    if sexo == 'F' and idade <= 20:
        contf += 1
    print ('='*20)
    soun = input('Deseja continuar ? (S/N) ').upper().strip()
    if soun == 'N':
        break
print ('='*20)
print (f'ao todo existem no grupo {cont} pessoas maiores de idade')
print (f'{contm} homems')
print (f'e {contf} mulheres com menos de 20 anos ')
print ('='*20)
