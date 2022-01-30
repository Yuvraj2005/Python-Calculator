print("\nWelcome to the Calculator: Developed by the Yuvraj Gupta")

while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    operation = input(""
                      "Please type in the math operation you would like to complete: \n"
                      "+ for the addition\n"
                      "- for the subtraction\n"
                      "* for the multiplication\n"
                      "/ for the division\n"
                      "% for the percentage\n"
                      "Enter the Choice:")

    if operation == '+':
        print("first number=", num1)
        print("second number=", num2)
        print(float(num1) + float(num2))

    elif operation == '-':
        print("first number=", num1)
        print("second number=", num2)
        print(float(num1) - float(num2))

    elif operation == '*':
        print("first number=", num1)
        print("second number=", num2)
        print(float(num1) * float(num2))

    elif operation == '/':
        print("first number=", num1)
        print("second number=", num2)
        print(float(num1) / float(num2))

    elif operation == '%':
        print("NOTE: In this Operation second number is the total Marks")
        print("first number=", num1)
        print("second number=", num2)
        print(((float(num1) / float(num2)) * 100), "%")

    else:
        print("Invalid Choice!!")

    while True:
        answer = str(input("Run The Calculator Again?? (y / n):"))
        if answer in ("y", "n"):
            break
        print("INVALID INPUT!! Type y to run again and n to exit.")

    if answer == "y":
        continue
    else:
        print("Thanks for running Calculator! Press enter to exit")
        break