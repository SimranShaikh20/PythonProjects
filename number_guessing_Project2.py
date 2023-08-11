import random

low_value=int(input("Enter  lowest value : "))
high_value=int(input("Enter hihger value : "))
chc=random.randint(low_value,high_value)
# print(f'Random selected  by computer is {chc}')        
i=0
win=False
while win==False:
   guess=int(input(f'Enter number between given {low_value} and {high_value} range :'))
   i+=1
   if chc==guess:
    print(f"You win!")
    print(f'Number of guessed used are:{i}')
    win==True
    break
   else:
    if guess<chc:
     print(f"Guessed number is  low")
    else :
      print(f"Guessed number is  high") 
