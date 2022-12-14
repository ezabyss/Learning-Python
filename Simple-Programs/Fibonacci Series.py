# Fibonacci Series: Every Next term is the sum of Preceding two values
# 0 1  (0+1) (1+1) (2+1) (3+2) (5+3) (8+5)
# 0 1 1 2 3 5 8 13

print(" PROGRAM : FIBONACCI SERIES ")
print(" FIBONACCI SERIES ")

num = int(input("Please enter the number of series you want:: "))
val_1 = int(input("Please enter the 1st value:: "))
val_2 = int(input("Please enter the 2nd value:: "))
print(val_1, val_2, end=" ") # end=" " will give space instead of new line afte printing

while num-2:
    sum = val_1 + val_2
    val_1 = val_2
    val_2 = sum
    print(sum, end=" ")
    num-=1   #same as: num = num - 1 





