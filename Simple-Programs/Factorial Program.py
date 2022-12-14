# find factorial (means: multiplication of all positive number descending from given number 'n')
# 5! = 5 * 4 * 3 * 2 * 1   
# 4! = 4 * 3 * 2 * 1

print("  PROGRAM TO FIND FACTORIAL  ")

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i   #same as: fact = fact * i
    return fact

num = int(input("Please Enter a number:: "))
result = factorial(num)

print("The factorial of ", num, " is ::", result)




