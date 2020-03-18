import random
from twilio.rest import Client

totalCards = 21

phoneNumbers = []

playerHands = {}

numPlayers = input("Enter the number of players: ")

print(str(numPlayers) + " players are active.")

for x in range(0,int(numPlayers)):
    phoneNumber = input("Enter the next players number: ")
    phoneNumbers.append(phoneNumber)
print(phoneNumbers)

people = ['Col Mustard', 'Mr Green', 'Miss Scarlet', 'Mrs Peacock', 'Prof Plum', 'Mrs White']
weapons = ['Candlestick', 'Revolver', 'Rope', 'Lead Pipe', 'Knife', 'Wrench']
rooms = ['Hall', 'Lounge', 'Ballroom', 'Billiard Room', 'Study', 'Kitchen', 'Dining Room', 'Conservatory', 'Library']

#shuffle the respective sets
random.shuffle(people)
random.shuffle(weapons)
random.shuffle(rooms)

#pull out the winning combo
person = people.pop()
weapon = weapons.pop()
room = rooms.pop()

#add all remaining cards to a single set to hand out
allCards = people + weapons + rooms
random.shuffle(allCards)
player = 0
while(allCards):
    if("player{0}".format(player) in playerHands):
        previousVal = playerHands["player{0}".format(player)]
        playerHands["player{0}".format(player)] = str(previousVal)+ ", " + str(allCards.pop())
    else:
        playerHands["player{0}".format(player)] = str(allCards.pop())
    if player == (int(numPlayers) - 1):
        player = 0
    else:
        player = player + 1

print(playerHands)

client = Client("AC25de11e51e71ab285f5e0c6d984e513d", "0f9bfca3b026ef1a2758a1d6fd639fff")

for x in range(0,int(numPlayers)):
    client.messages.create(to="+1" + str(phoneNumbers[x]), from_="+12057363355", body=str(playerHands["player{0}".format(x)] + " -- ANSWER SET: " + str(person) + ", " + str(weapon) + ", " + str(room)))
