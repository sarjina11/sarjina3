#!/usr/bin/env python3
'''Lab 3 Part 2 script - functions with arguments'''
# Author ID: skarki28

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    return number1 - number2

def multiply_numbers(number1, number2):
    return number1 * number2

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))

