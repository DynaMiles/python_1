import random


lower="abndefghijklmnopqrstuvwxyz"
upper="ABCDEFGHJIKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbol="!@#$%^&*()"

string=lower + upper + numbers + symbol
lenght=8
password="".join(random.sample(string,lenght))
print("Your Password is :",password)

