
#This is what I used to understand the solution, but I failed mulitple times to produce the full solution till I understood my mistakes

# for x in range(1,10):
#     if x*3:
#         print('Fizz')
# for x in range(1,10):
#     if x*5:
#         print("Buzz")
# for x in range(1,10):
#     if x*3 and x*5:
#         print('FizzBuzz')

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
