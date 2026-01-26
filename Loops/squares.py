#This is to show the sum(total) of all the squares from 0 till the number the user has input.

total = 0
number = int(input("Enter a number: "))

for i in range(number + 1): #This is inclusive of the number as well in the range
  total += i * i  #This acts as the counter to add to the existing total
  
print(total)

#Another way to write the code

