

my_list = [1,2,3,4,5]

print("Reverse using slicing")
# very simple way to reverse list using slicing.
print(my_list[::-1])   

print("Reverse using .reverse method(it permanently reverses the list): ")
# it reverses in place making permanent changes
my_list.reverse()
print(my_list)