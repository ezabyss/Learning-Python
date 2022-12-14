# leap year: has 366 days. 

# features of leap year
# 1. YEAR is exactly divisible by 4, 
# 2. If YEAR is divisible by only 100 not LEAP YEAR 
# 3. if YEAR is divisible by both 100 and 400 then LEAP YEAR

# % : gives the REMAINDER

print("PROGRAM: CHECK LEAP YEAR")

year=int(input("Please enter a year : "))

if (year % 4) == 0:
    if (year % 100 == 0) & (year % 400 == 0):
        print(" YEAR : ", year, " is a LEAP YEAR.")
    else:
        print(" YEAR : ", year, " is not a LEAP YEAR.")
else:
    print(" YEAR : ", year, " is not a LEAP YEAR.")

        
        