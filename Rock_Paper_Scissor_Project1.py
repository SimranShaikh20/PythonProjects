import random

user_input=int(input("Enter your chioce 0->Rock   1->Paper  2->Scissor :"))
if(user_input>=3 or  user_input<0):
    print("Invalid number")
    print("user input "f'{user_input} ')
else:
 comp_input=random.randint(0,2)
 print("computer input "f'{comp_input}')

 if(user_input==comp_input):
     print(f'{user_input} and {comp_input}'" both input are same its tie")
 elif(comp_input==0 and user_input==2):
     print("Computer wins")
 elif(user_input==0 and comp_input==2):
    print("User wins, Computer Lose")
 elif(comp_input>user_input):
    print("Computer wins , User lose")
 elif(user_input>comp_input):
    print("User wins , computer lose")
 
 else:
    print("niether user nor computer wins")
