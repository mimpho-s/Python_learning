'''This is a Magic 8-Ball program that takes a user's question and provides a random answer from a predefined list of responses. The user is prompted to enter their question, and the program selects and prints one of the possible answers at random.'''

import random

question = input('Enter your question: ')
answers = ['Yes - definitely',  'It is decidedly so',  'Reply hazy, try again',  'Ask again later',  'Better not tell you now',  'My sources say no',  'Outlook not so good',  'Very doubtful']

answer = random.choice(answers)

print(answer)


# Below I will show another way to do the same thing usong if-elif-else statements.

import random

question = input('Enter your question: ')
answer = random.randint(0,8)

if answer == 0:
 print('Yes - definitely.')
elif answer == 1:
 print('It is decidedly so.')
elif answer == 2:
 print('Without a doubt.')
elif answer == 3:
 print('Reply hazy, try again.')
elif answer == 4:
 print('Ask again later.')
elif answer == 5:
 print('Better not tell you now.')
elif answer == 6:
 print('My sources say no.')
elif answer == 7:
 print('Outlook not so good.')
elif answer == 8:
 print('Very doubtful.')
else:
  print('error')