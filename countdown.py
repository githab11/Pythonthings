import random
import time
amount = int(input("What number would you like to countdown from: "))

print(amount)
while amount != 0:
    amount -= 1
    print(amount)
    time.sleep(1)
    if amount <= 0:
        print("Timers up!")
else:
    print("Invalid input, please try again")

