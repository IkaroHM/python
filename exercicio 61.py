ptermo = int (input ('quaklo primeiro termo da PA ? '))
razao = int (input('qual a razao da PA ? '))
decimotermo = ptermo + (10-1)* razao
while ptermo < decimotermo :
    ptermo += razao
    print (ptermo, end= '-> ')