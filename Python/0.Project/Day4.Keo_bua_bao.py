import random
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

game = [rock, paper, scissors]

name = ["rock", "paper", "scissors"]

choose = int(input("What do you choose? 0 to 'rock' 1 to 'paper' and 2 'scissors'\n"))

computer = random.randint(0, 2)

print("You Choose " + name[choose] + game[choose])
print("Computer Choose " + name[computer] + game[computer])

if choose == 1 and computer == 0:
  print("You Win")
elif computer == 1 and choose == 0:
  print("Computer Win")
elif choose == 2 and computer == 1:
  print("You Win")
elif computer == 2 and choose == 1:
  print("Computer Win")
elif choose == 0 and computer == 2:
  print("You Win")
elif computer == 0 and choose == 2:
  print("Computer Win")
else:
  print("Draw")