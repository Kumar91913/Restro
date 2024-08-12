n=18
number_of_guessess=1
print("Number of guessess is limited to only 9 times:")
while(number_of_guessess<=9):
    guess_number=int(input("Guess the number:\n"))
    if guess_number<18:
        print("you enter less number please enter greater number:\n")
    elif guess_number>18:
        print("you enter greater number please enter smaller number:\n")
    else:
        print("you won\n")
        print(number_of_guessess,"no.of guessess he took to finish.")
        break
        print(9-number_of_guessess,"no.of guessess left")
        number_of_guessess=number_of_guessess+1
if(number_of_guesses>9):
    print("Game Over")
