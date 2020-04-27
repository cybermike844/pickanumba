import random

msg = "What's yo numba, 1-10?: "
int1 = random.randint(1,10)
int2 = input( msg )
lives = 3

while lives > 0:
  if int1 == int(int2):
    print("Yay the number was: " + str(int1))
    break
  elif  int1 > int(int2):
    int2 = input("You are a little low: ")
    lives -= 1
    print("You have " + str(lives) + " lives remaining" )
  elif  int1 < int(int2):
    int2 = input("You are a little high: ")
    lives -= 1
    print("You have " + str(lives) + " lives remaining" )

if lives == 0 :
  print("You failed, the number was: " + str(int1))
