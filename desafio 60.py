soun = True
while soun:
    n1 = int (input('escolha o número inteiro que voce deseja ver o seu fatorial '))
    for c in range (n1, 0, -1):
        fat = 1
        fat *= c 
    sorn = input (f'o fatorial desse numero é {fat}, deseja continuar ? (s/n)').upper()
    if sorn == 'N':
        soun = False
        print ('Tenha um ótimo dia! ')
    elif sorn == 'S':
        soun = True
    else:
        print ('Insira algo valido!')
