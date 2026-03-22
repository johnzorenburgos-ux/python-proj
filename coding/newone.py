import random

while True:
    secret_num = random.randint(1, 100)

    print("lets play a game")
    print("1 to 100, guess what number is in my mind")
    print("are you ready? lets start")

    while True:

        guess = int(input("your guess: "))

        if guess < secret_num:
            print("MALIIIII,HIGHER PA BES")

        elif guess > secret_num:
            print("MALIIIII, LOWER PA BES")

        else:
            print("ANG GALING, BIGYAN NG MEDAL YAN")
            print("HALIMAW KA TALAGA SAH")
            break
    
    play_again = input("do you want to play again? yes/no ")
    if play_again == 'no':
        print("thanks for playing")
        break

    else:
        continue