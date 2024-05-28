import phonenumbers

number=input("Enter phone number with country code including (+) symblo :")
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH") # c=city, h= history
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier # carrier is for service provider name
ser_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ser_number,"en"))