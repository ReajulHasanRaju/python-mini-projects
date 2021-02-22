# Password Generator Using Python

import random, string

# I use only 10 most used punctuation
char = string.ascii_uppercase + '!@#$%&+=/?' + string.digits + string.ascii_lowercase

how_long = int(input('How long password do you want? '))
how_much = int(input('How many password do you want? '))

print('\n-----Here are your Passwords-----\n')
for x in range(how_much):
    for y in range(how_long):
        print(random.choice(char), end='')
    print('')