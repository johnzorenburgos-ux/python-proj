while True:
    Num1 = float(input("Enter first number: "))
    Num2 = float(input("Enter second number: "))

    print("select operation to perform")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")

    choice = input("Enter choice 1/2/3/4: ")
    if choice == '1':
        print(Num1 + Num2)
    elif choice == '2':
        print(Num1 - Num2)
    elif choice == '3':
        print(Num1 * Num2)
    elif choice == '4':
        print(Num1 / Num2)
    else:
        print("MALIIIIIIIII")
    restart = input("do you want to calculate again? Y/N ")
    if restart == 'N' or restart == 'n':
        print("GOODBYEEEEEEEEEE")
        break 
    elif restart == 'Y' or restart == 'y':
        continue
    else:   print('THE CHOICES ARE ONLY Y OR N, IDIOT')