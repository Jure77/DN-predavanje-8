# -*- encoding: utf-8 -*-

vnos = int(raw_input("Vnesi številko med 1 in 100: "))
for x in range (1, vnos + 1):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print ("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print ("FizzBuzz")
    else:
        print(x)