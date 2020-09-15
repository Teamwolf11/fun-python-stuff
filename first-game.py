print("This is my first python program");

name = input("What is your name? ")
age= int(input("What is your age? "))

if(age>=18):
  print("Welcome to the game\n")
elif(age>13):
  print("You can do it if you have adult supervision\n")
else:
  print("You are not old enough for this very smart and intelligent program\n")
print("Your goal of this game is to not die, eventually if you reach the finish line you will win. There is no strategy to the game it is purely luck")
turn = input("Are you going to go across the river or around it? (around/across)")
turn=turn.lower()
if turn=="around":
  print("You won the game "+name)
elif turn == "across":
  print("You got bit by the alligator and died " + name)
else:
  print("You have not input a legit answer, you lose "+name)




