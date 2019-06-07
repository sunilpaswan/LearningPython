number = 23
guess = int(input('Enter your number: '))

if guess == number:
    print('Congratulation you guessed correct number')
    print('But you do not win any prizes')

elif guess > number:
    print('No it is little higher')

else:


    
    print('No it is little smaller')

print('Done')