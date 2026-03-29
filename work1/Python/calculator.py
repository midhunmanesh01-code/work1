while True: 
    print("1. Addition".upper())
    print("2. Subtraction".upper())
    print("3. Division".upper())
    print("4. Multiplication".upper())
    print("5. Exit".upper())

    userInput = int(input("Enter an Input: "))

    if userInput == 5:     
        break 

    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    
    if userInput == 1:
        print("The sum is:",num1+num2)
    elif userInput == 2:
        print("The  difference is:",num1-num2)
    elif userInput == 3:
        print("The quotient is:",num1/num2)
    elif userInput == 4:
        print("The product is:",num1*num2)
    else: 
        print("Invalid Input")
