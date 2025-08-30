import random
import pyfiglet
from colorama import init, Fore, Back
import time
print (Fore.GREEN + pyfiglet.figlet_format('JOGO DE FUTEBOL'))
gol = Fore.YELLOW + """
     /---------------------\\
    /            G          \\
   /                         \\
  /                           \\
                 .
"""

jogador = Fore.WHITE + "■"
print(gol)
print("             " + jogador)
pts = 0
soun = True
while soun:
    init(autoreset=True)
    goleiro = random.randint(1, 3)
    print( Fore.GREEN + "Quando o alerta vermelho aparecer digite 1(esquerda) 2(meio) 3(direita)")
    time.sleep(10)
    print( Fore.GREEN + '3')
    time.sleep(1)
    print( Fore.YELLOW + '2')
    time.sleep(1)
    print(Fore.RED + '1')
    time.sleep(1)
    print (Fore.RED + 'ja')
    inicio = time.time()
    chute = int(input(''))
    fim = time.time()
    if fim - inicio > 3:
        print (Fore.RED + 'Voce demorou muito!')
    elif fim-inicio < 3:
        if chute == goleiro:
            print ( Fore.RED +'O goleiro pegou o seu chute')
        if chute != goleiro:
            pts += 1
            print (Fore.GREEN + f'Parabéns, voce fez um gol! e tem {pts} pontos')
            soueni = input('Deseja continuar ? (s/n)').upper().strip()
            if soueni == 'N':
                soun = False
            
