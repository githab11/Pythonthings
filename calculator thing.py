import random
import math

digit = input("Would you like to do double or single digit?: ")
if digit[0].lower() == 'd':
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
elif digit[0].lower() == 's':
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)


negative = input("Negative or positive?: ")
if negative[0].lower() == 'n':
    number1 = number1 * -1
    number2 = number2 * -1

input1 = input("Would you like to do a subtraction, addition, multiplication, or division problem?: ")

if input1[0].lower() == 'd':
    math0 = number1, "/", number2
    print(math0)
    math_input0 = float(input("What is the answer?: "))  # Corrected variable name and converted input to a float
    if math_input0 == number1 / number2:  # Corrected variable name
        print("You got it correct!")
        print("The number was: ", math_input0)
    else:
        print("Wrong!")
        print("The number was: ", number1 / number2)

if input1[0].lower() == 'a':
    math1 = number1, "+", number2
    print(math1)
    math_input1 = float(input("What is the answer?: "))
    if math_input1 == number1 + number2:
        print("You got it correct!")
        print("The number was: ", math_input1)
    else:
        print("Wrong!")
        print("The number was: ", number1 + number2)

if input1[0].lower() == 'm':
    math2 = number1, "x", number2
    print(math2)
    math_input2 = float(input("What is the answer?: "))
    if math_input2 == number1 * number2:
        print("You got it correct!")
        print("The number was: ", math_input2)
    else:
        print("Wrong!")
        print("The number was: ", number1 * number2)

if input1[0].lower() == 's':
    math3 = number1, "-", number2
    print(math3)
    math_input3 = float(input("What is the answer?: "))
    if math_input3 == number1 - number2:
        print("You got it correct!")
        print("The number was: ", math_input3)
    else:
        print("Wrong!")
        print("The number was: ", number1 - number2)
