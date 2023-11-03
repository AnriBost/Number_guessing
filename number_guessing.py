#This is a number guessing game.Enter a number between 1 and 10,after that code will ask you if it guessed your number:)

user_number = int(input("enter a number between 1 and 10:"))
guess = 1
while True:
    user_response = input(f'is it {guess}?(y/n):')
    if user_response == 'y':
        print('i guessed it!')
        break
    elif user_response == 'n':
        guess += 1
    else:
        print('Please enter "y" for yes or "n" for no')