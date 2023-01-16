import pyshorteners

print("!!! WELCOME TO URL SHORTNER !!!")

url = input("Please enter the original url: ")
s = pyshorteners.Shortener()

print(s.tinyurl.short(url))



