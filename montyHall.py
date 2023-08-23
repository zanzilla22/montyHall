from random import randint, choice

switchDoors = False
iterations = 2000
guesses = {"car": 0, "donkey": 0} 

for q in range(iterations):
  doors = ["donkey", "donkey", "donkey"]
  
  carDoor = randint(0, 2)
  doors[carDoor] = "car"
  
  firstChoice = randint(0, 2)
  
  # print(f"First choice: Door #{firstChoice+1} | Car: Door #{carDoor+1}")
  
  revealDoor = choice([x for x in range(0, 3) if (x != carDoor and x != firstChoice)])
  
  # print(f"Revealed door: {revealDoor+1}")
  
  if switchDoors == True:
    switchChoice = [x for x in range(3) if (x!= firstChoice and x!= revealDoor)][0]
    guesses[doors[switchChoice]]+=1
    # print(switchChoice+1)
  else:
    guesses[doors[firstChoice]]+=1
    
print(guesses)

print(f'When {"switching after the reveal" if switchDoors else "maintaining your first choice"}, you guessed right {guesses["car"]/iterations * 100}% of the time!\nExpected was {"66%" if switchDoors else "33%"}')
