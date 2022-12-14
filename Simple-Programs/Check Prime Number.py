# PRIME number are only divisible by 1 or itself

print(" PROGRAM : CHECK PRIME NUMBER: ")

num=int(input(" Please enter a number: "))
if num > 1:
    for i in range(2,num): 
        if(num%i==0):            
            print(num, " is not a PRIME number.")
            print(i, " times ", num//i, " is ", num)
            break;
    else:
        print(num, " is a PRIME number.")