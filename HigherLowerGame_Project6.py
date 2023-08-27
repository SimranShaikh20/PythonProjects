import random
data= [ {
        'name':'Simran',
         'followers':89,
         'description':'Student',
          'country':"India",
        },
        {
        'name':"Abrar",
         'followers':90,
         'description':"Employee",
          'country':'USA',
        },
        {
        'name':'Nazneen',
         'followers':100,
         'description':'MBA Student',
          'country':'Indonasia',
        },
         {
        'name':'Firoza',
         'followers':1000,
         'description':'Home Made',
          'country':'India',
        }
     ]
flag=True
score=0
while flag:
 comp_guess1=random.choice(data)
 comp_guess2=random.choice(data)
 if comp_guess1['name']==comp_guess2['name']:
        print('both comparing value are same')
        exit
 else:
    print(' A {0}  is {1} it lives in {2}'.format(comp_guess1['name'],comp_guess1['description'],comp_guess1['country']))
    print('--------------------------VS--------------------------------')
    print('A  {0}  is {1} it lives in {2}'.format(comp_guess2['name'],comp_guess2['description'],comp_guess2['country']))
    user_input=int(input("Who has more follower? Type 1 or 2 : "))
    
    if comp_guess1['followers'] > comp_guess2['followers']:
         if user_input==1:
          score+=1
          print(f'you win  {score} ')     
         else:
            flag=False
            print(f'you lose ') 
    elif comp_guess2['followers']>comp_guess1['followers']:
         if user_input==1:
           flag=False
           print(f'you lose ')   
           
         else:
            score+=1
            print(f'you win {score}') 
