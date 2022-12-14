# Sum of cube of each digit of a number is equal to its actual value
# eg: 153 = 1**3 + 5**3 + 3**3

print("PROGRAM : ARMSTRONG NUMBER")

num=int(input(("Please, enter a number:: ")))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10 # it takes out the last digit.
    sum += digit ** 3
    temp = temp//10
if num == sum:
    print( sum, "is a ARMSTRONG number.")
else:
    print( num, "is not a ARMSTRONG number.")







