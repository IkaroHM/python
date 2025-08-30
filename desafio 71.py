n1 = int(input('Qual valor sera sacado ? (apenas numeros inteiros ) '))
notas50 = n1 // 50
restodas50 = n1 % 50
notas20 = restodas50 // 20
restodas20 = restodas50 % 20
notas10 = restodas20 // 10
restodas10 = restodas20 % 10
notas1 = restodas10 // 1
print (f'''serao sacadas: 
{notas50} notas de 50 reais
{notas20} notas de 20 reais
{notas10} notas de 10 reais
e {notas1} de 1 real ''')   