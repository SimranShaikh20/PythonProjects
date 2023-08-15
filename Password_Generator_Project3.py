import random

word=int(input("Enter how many number of word do you want :"))
value="abcdefghijklmonpqrstuiwxyz"
p1="".join(random.sample(value,word))
symbols=int(input("Enter how many number of symbols do you want :"))
value="!@#$%^&*(?)`:"
p2="".join(random.sample(value,symbols))
number=int(input("Enter how many number  do you want :"))
value="1234567890"
p3="".join(random.sample(value,number))
print(f'Strong password is here -> {p1+p2+p3}')