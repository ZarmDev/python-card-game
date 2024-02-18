import random
from replit import clear
import time
import os
#name = input("What is your name? ")
#print('Hello ', name)
card = '''
◜■■■■■■■■■■◝
|          |
|          |
|          |
|          |
|          |
|          |
|          |
◟■■■■■■■■■■◞
'''
halfCard = '''
◜■■■■■■■■■■◝
|          |
|          |
|          |
'''
otherHalfCard = '''
|          |
|          |
|          |
◟■■■■■■■■■■◞
'''
def createCard(value):
  spacing = '   '
  cardText = value[0]
  health = value[1]
  damage = value[2]
  newCard = halfCard + spacing + cardText + '\n' + spacing + 'HP: ' + str(health) + '\n' + spacing + 'DMG: ' + str(damage) + otherHalfCard
  print(newCard)
  return newCard

rivalCards = []
yourCards = []
randomCards = [["Rhino", 8, 8], ["Dinosaur", 16, 16], ["Wolf", 2, 4], ["Cat", 5, 2], ["Meerkat", 1, 1]]

def cardSortAnimation():
  for i in range(10):
    print('Sorting cards... ')
    print('| | | | |', flush=True)
    time.sleep(0.01)
    clear()
    print('Sorting cards... ')
    print(' | | | |', flush=True)
    time.sleep(0.01)
    clear()
    print('Sorting cards... ')
    print('| | | | |', flush=True)
    time.sleep(0.01)
    clear()
    randomCard = randomCards[random.randrange(1, len(randomCards))]
    if i < 5:
      yourCards.append(randomCard)
    if i >= 5:
      rivalCards.append(randomCard)

#level = random.randrange(1, 5)
level = 1

print("This game is inspired by Inscryption.")

time.sleep(2)

check = input('Do you want to see the tutorial? (Y/N)')

isCheckTrue = False

if check == 'Yes' or check == 'Y' or check == 'y':
  isCheckTrue = True

if isCheckTrue == True:
  test = input("In this game, your rival and you get 5 random cards, each with damage and health. Your cards will be shown as | | | | | and your rivals cards will be shown above your cards. You do not know your cards, but you know your opponents cards and you can get a card's information when you use it. This means that you can assume which card of your's is the best and use that to win, there are multiple strategies.")

while (True):
  if level == 1:
    cardSortAnimation()
    print('...')
    print("Make sure to not scroll up too far or you will see old messages.")
    time.sleep(4)
    if isCheckTrue == True:
      print("I will give you 5 cards...")
      time.sleep(1)
      print("Now let's play.")
      time.sleep(1)
      test = input("You have five turns. You need to maximize the amount of damage you do by either using your highest damage card or attacking in the right place. Each card will only attack it's counterpart, that means that if your first card is a Meerkat and the rival's first card is a Cat, you can only attack that Cat with your Meerkat. When judging who won, all of your cards and your rival's cards HP's will be tallied up and the one with the highest will win. Your rival will have +20 additional HP because you attack and they don't.")
    for i in range(5):
      clear()
      print("These are your Rival's cards...")
      for i in range(len(rivalCards)):
        createCard(rivalCards[i])
      print("These are your cards (which you don't know)")
      print("| | | | |")
      time.sleep(1)
      chooseCard = int(input("Choose a card to use (Enter 1-5)"))
      clear()
      # Because python list index starts at zero, not one
      chooseCard -= 1
      print(f"You used {yourCards[chooseCard][0]}")
      createCard(yourCards[chooseCard])
      time.sleep(3)
      clear()
      # My card infront of your card is damaged by your card
      applyDamage = rivalCards[chooseCard].copy()
      print(f"You damaged {applyDamage[0]} by {yourCards[chooseCard][2]}")
      applyDamage[1] -= yourCards[chooseCard][2]
      rivalCards[chooseCard] = applyDamage.copy()
      if applyDamage[1] <= 0:
        print(f"You killed {applyDamage[0]}.")
      time.sleep(2)
      clear()

    # Additional 20 for Rival
    rivalScore = 20
    for i in range(len(rivalCards)):
      rivalScore += rivalCards[i][1]
    playerScore = 0
    for i in range(len(yourCards)):
      playerScore += yourCards[i][1]
    print('Your score is', playerScore)
    if rivalScore < playerScore:
      print('You won...')
    elif rivalScore > playerScore:
      print('You lost...')
    else:
      print('Tie..')
    break
