menu={
    
    'espresso':{
        'ingrediants':{
            'water':50,
            'coffee':18,
        },
        'cost':100,
    },
    'latte':{
        'ingrediants':{
            'water':200,
            'coffee':24,
            'milk':150,
        },
        'cost':150,
    },
    'capachino':{
        'ingrediants':{
            'water':250,
            'coffee':10,
            'milk':24,
        },
        'cost':200,
    }
}

profit=0
resource={
   'water':500,
   'milk':300,
    'coffee':100
}
def check_resource(remainIngrediants):
    for item in remainIngrediants:
        if remainIngrediants[item]>resource[item]:
            print(f'Sorry there is not enough resource')
            return False
    return True 
def process_cions():
    cions=int(input("pay money :"))
    return cions   
def is_payment_done(money_recieved,coffee_cost):
    if money_recieved>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_recieved-coffee_cost
        print(f"Here is your {change}.")
        return True
    else:
        print("Sorry it is not enough money")
        return False
def make_coffee(coffee_name,coffeeIngrediants):
    for item in coffeeIngrediants:
        resource[item]-=coffeeIngrediants[item]
    print(f'Here is your coffee {coffee_name}')

flag=True
while flag:
    userValue=input("Enter name of coffee that do you want (espresso/latte/capachino):")
    if userValue=="stop":
        exit
        flag=False
    elif userValue=="report":
        print(f'Water= {resource["water"]}')
        print(f'Milk= {resource["milk"]}')
        print(f'Coffe= {resource["coffee"]}')
        print(f'Cost = {profit}')    
    else:
        coffee_type=menu[userValue]
        print(coffee_type)                 
        if check_resource(coffee_type['ingrediants']): 
           payment=process_cions()   
           if is_payment_done(payment,coffee_type['cost']):
               make_coffee(userValue,coffee_type['ingrediants'])