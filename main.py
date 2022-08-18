rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
playcpu = [rock,paper,scissors]
randoncpu = int(random.randint(0,len(playcpu)-1))
playcpux = playcpu[randoncpu]
escolha = input('\Qual você escolhe "rock","paper","scissors"?')
if escolha == 'rock':
  print('player')
  print(rock)
  print('cpu')
  print(playcpux)
  if playcpux == paper and escolha == 'rock':
    print('você perdeu')
  if playcpux == scissors and escolha == 'rock':
      print('você Ganhou')
  if playcpux == rock and escolha == 'rock':
    print('Empate')
    escolha = input('\Qual você escolhe "rock","paper","scissors"?')
if escolha == 'paper':
  print('player')
  print(paper)
  print('cpu')
  print(playcpux)
  if playcpux == scissors and escolha == 'paper':
    print('você perdeu')
  if playcpux == rock and escolha == 'paper':
      print('você Ganhou')
  if playcpux == paper and escolha == 'paper':
    print('Empate')
    escolha = input('\Qual você escolhe "rock","paper","scissors"?')
if escolha =='scissors':
  print('player')
  print(scissors)
  print('cpu')
  print(playcpux)
  if playcpux == rock and escolha == 'scissors':
    print('você perdeu')
  if playcpux == paper and escolha == 'scissor':
      print('você Ganhou')
  if playcpux == scissors and escolha == 'scissors':
    print('Empate')
    escolha = input('\Qual você escolhe "rock","paper","scissors"?')
  
    
      