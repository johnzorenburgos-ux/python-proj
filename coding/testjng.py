import random

def show_menu():
 print("-------bank------")
 print("1.check balance")
 print("2.deposit")
 print("3.withdraw")
 print("4.play slot machine")
 print("5.exit")

def spin_row():
  return[random.choice(symbols) for _ in range(3)]
 
def print_row(row):
  print("-------------")
  print(" ".join(row))
  print("-------------")

def check_win(row, bet):
  if row[0] == row[1] == row[2]:
   return bet * 5
  elif row[0] == row[1] or row[0] == row[2] or row[1] == row[2]:
   return bet * 2
  else:
   return 0

balance = 0
symbols = ["🍒", "🍇", "🍓", "🍌","🍑"]

while True:
 show_menu()
 choice = input("enter your choice (1-5): ")

 if choice == "1":
  print("---------------------------")
  print(f"your balance is ₱{balance}")
  print("---------------------------")

 elif choice == "2":
  amount = float(input("put an amount to deposit: "))
  if amount > 0:
   balance += amount
  else:
   print("your amount is invalid")
 
 elif choice == "3":
  withdrawen = float(input("put an amount to withdraw: "))
  if withdrawen > balance:
   print("you dont have enough balance")
  elif withdrawen <= 0:
   print("your amount is invalid")
  else:
   balance -= withdrawen
   print(f"withdrawn ₱{withdrawen}. New balance:₱{balance}")

 elif choice == "4":
  if balance == 0:
   print("you dont have enough money to play")
   continue
  
  while True:
   bet = float(input("enter an amount to bet: "))
  
   if bet > balance or bet <= 0:
    print("invalid bet")
    continue
  
   balance -= bet

   row = spin_row()
   print("spinning...\n")
   print_row(row)

   payout = check_win(row, bet)

   if payout > 0:
    print(f"you won ₱{payout}")

   else:
    print("you lost this round sorry")


   balance += payout


   play_again = input("do you want to play again? (Y/N): ").upper()


   if play_again != "Y":
    break

 elif choice == "5":
  print("Thank you, goodbye")
  break
 
 else:
  print("invalid choice, try again")




   