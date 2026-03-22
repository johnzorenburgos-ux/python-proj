import random

def guessing_number_game():
 print("lets play guess the number")
 print("I have a number in my mind up to 100")
 print("guess the number I have in my mind")

 guessthenum = random.randint(1, 100)

 while True:
  guess = int(input("your guess: "))

  if guess < guessthenum:
    print('MALIIIII, HIGHER PA BES')
  elif guess > guessthenum:
    print('MALIII, LOWERR PA BES')
  else:
    print("NAKSSS ANG GALINGG NIYAA")
    break

def main():
    guessing_number_game()
    while True:
     play_again = input("Would you like to play again? (yes/no): ")
     if play_again == "no" or 'n':
      print("👋 Thanks for playing! Goodbye!")
      break
     elif play_again == 'yes' or 'y':
       continue
     else:
       print("the choices is only yes or no")

main()

