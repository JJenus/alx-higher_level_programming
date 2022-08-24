#!/usr/bin/python3

def print_last_digit(number):
    if (number < 10):
        print(number)
        return number
    if (number < 0):
        temp = (-1 * number) % 10
    else:
        temp = number % 10
    print(temp)
    return temp
