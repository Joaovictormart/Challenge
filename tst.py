#PEDRA PAPEL E TESOURA

import random
def start():
     jogador = input('Qual o seu nome jogador? ')

     print(f'seja muito bem vindo jogador {jogador} vamos começar')
     
     print('faça sua jogada escolhendo entre as opções')
     print('[0] pedra')
     print('[1] papel')
     print('[2] tesoura')
     x=input('qual sua escolha? ')
     x=int(x)
     y=random.randrange(0,2)

     if x == 0 and y == 0:
          print('ambos os jogadores jogaram pedras')
     elif x == 1 and y == 1:
          print('ambos os jogadores jogaram papel')
     elif x == 2 and y == 2:
          print('ambos os jogadores jogaram tesoura')
     elif x == 0 and y == 1:
          print(f'O {jogador} jogou pedra contra o papel vitoria da casa')
     elif x == 1 and y == 2:
          print(f'O {jogador} jogou papel contra a tesoura vitoria da casa')
     elif x == 2 and y == 0:
          print(f'O {jogador} jogou tesoura contra a pedra vitoria da casa')
     elif x == 1 and y == 0:
          print(f'O {jogador} jogou papel contra a pedra vitoria')
     elif x == 0 and y == 2:
          print(f'O {jogador} jogou pedra contra a tesoura vitoria')
     elif x == 2 and y == 1:
          print(f'O {jogador} jogou tesoura contra o papel vitoria')

     else:
        print('voce jogou tesoura')
    
        

        





        


start()



print("so exitem eu e voce amigão")