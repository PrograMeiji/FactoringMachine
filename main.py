# This program takes user input and computes factors, taking account for prime numbers
# Ideal number is less than 16 digits
# Written by Bryan Johnston - 2/27/2022


import math


def intake():  # function to take users natural number entered
    user_input = input("Enter a positive integer to factor: \n")
    if user_input.isdecimal():  # checks if input is a valid decimal number
        if int(user_input) > 0:
            factor(user_input)  # calls factoring method passing the user input as parameter
        else:
            print("Invalid entry. Try again.")
            intake()
    elif user_input == 'q':  # enter q to stop program
        exit()
    elif user_input == 'Q':  # enter Q to stop program
        exit()
    else:
        print("Invalid entry. Try again.")
        intake()  # let user enter another attempt


def factor(num):  # function for computing all factors of a number and printing factors
    factors = []  # array for holding factors
    max_check = int(math.sqrt(int(num)) + 1)  # only need to check up to sqrt of num entered, 2 factors added at a time
    natural_number = 2  # start at 2 because 1 is a factor of every number
    while natural_number < max_check:  # range of 2 to sqrt of num
        if int(num) % natural_number == 0:  # checks if entered number is divisible by natural number
            factors.append(natural_number)  # adds natural number to list
            other_factor = int(num) / natural_number  # adds other factor to list so we don't need to check it
            if other_factor == natural_number:  # checks to make sure that perfect squares do not repeat a factor
                natural_number += 1  # increment natural number
            else:
                factors.append(int(other_factor))  # add the other factor to the array
                natural_number += 1  # increment natural number
        else:
            natural_number += 1  # increment natural number
    if not factors:  # if factors is empty, it is prime
        if num == "1":  # 1 is not prime and needs its own case
            print("The factor is: [1]")
            intake()
        else:
            print(num + " is a prime number.")  # if our array is empty, then the number is prime
            intake()
    else:  # add 1 and the number entered to the factor array
        factors.append(1)
        factors.append(int(num))
        factors.sort()  # sort factors in ascending order
        print("The factors are:", factors)  # print all factors
        intake()


def main():  # main method
    print("This program intakes a positive integer and outputs all its factors. To exit enter Q "
          "or q.")  # let's user know how to exit program
    intake()


if __name__ == "__main__":  # convention starting program
    main()
