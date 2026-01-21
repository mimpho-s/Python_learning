answer = ""

while answer.lower() != "yes":
  answer = input("Are we there yet?") #Add .strip() to remove all the spaces from both ends of the string
  if answer == "yes":
   break
  
#This is another way to solve this problem!!
# Collect user input until they say "done"

all_names = ""

while True:
    name = input("Enter a name (or 'done'): ")
    if name == "done":
        break
    all_names += name + ", "

print(f"All names: {all_names}")