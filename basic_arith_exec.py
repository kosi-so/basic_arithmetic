import basic_arith
import time 

def main ():
    while True:
        action = input("What would you like to do? \n (1) Addition \n (2) Subtraction \n (3) Multiplication \n (4) Division \n (5) Floor \n (6) Power \n")
        val1 = int(input("Insert your 1st input \t"))
        val2 = int(input("Insert your 2nd input \t"))

        if action == "1":
            x = basic_arith.add(val1, val2)
            print(f' \n The sum of {val1} and {val2} is {x} \n')
            time.sleep(1.5) # Delay of 1.5 seconds

        if action == "2":
            x = basic_arith.subtract(val1, val2)
            print(f' \n The difference between {val1} and {val2} is {x} \n')
            time.sleep(1.5) # Delay of 1.5 seconds

        if action == "3":
            x = basic_arith.multiply(val1, val2)
            print(f' \n The product of {val1} and {val2} is {x} \n')
            time.sleep(1.5) # Delay of 1.5 seconds

        if action == "4":
            x = basic_arith.divide(val1, val2)
            print(f' \n {val1} divided by {val2} is {x} \n')
            time.sleep(1.5) # Delay of 1.5 seconds

        if action == "5":
            x = basic_arith.floor(val1, val2)
            print(f' \n The floor of {val1} and {val2} is {x} \n')
            time.sleep(1.5) # Delay of 1.5 seconds

        if action == "6":
            x = basic_arith.power(val1, val2)
            print(f' \n {val1} to the power of {val2} is {x} \n')
            time.sleep(1.5) # Delay of 1.5 seconds

if __name__ == "__main__":
    main()