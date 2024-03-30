# Solution for BYU OIT coding challenge, Zach Forster 04/30/24

# Convert Roman Numerals into decimal numbers by:
# 1. Taking input and checking to make sure the input is valid
# 2. Iterating through the input, adding to a total value for each symbol
# 3. Returning the converted value and giving the option to accept another number or to exit the program

# Convert decimal numbers back to Roman numerals by:
# 1. Accepting a number to convert as input, up to 3999 as specified in the instructions
# 2. Iterating through the number, checking the value in its place against a dictionary of values, subtracting
# the number each time until 0 is left
# 3. Return the

# import re to use in checking for valid characters
import re


# check the characters in inp against the valid roman numerals
def appropriate_characters(inp):
    for char in inp:
        if not(re.match('[IVXLCDM]+', char)):
            return False
    return True


# Check for appropriate notation using values assigned to each character through a dictionary
def correct_notation(inp, vals):
    if len(inp) > 1:
        for i in range(len(inp)-1):
            # Check to see if an invalid numeral is followed by a subtractive
            if inp[i] in ['V', 'L', 'D'] and len(inp) >= 3:
                if subtractive(inp[i+1], inp[i+2], inp[i+1:]):
                    return False
            # Check to see if the first numeral is greater than the second
            if not(vals[inp[i]] > vals[inp[i+1]]):
                # If the first numeral is not greater than the second check to see if it is repeated
                if not(vals[inp[i]] == vals[inp[i+1]]):
                    # If it is not repeated, check if it is subtractive, including length to ensure that there are no
                    # repetitions of the second letter in the subtractive after the subtraction
                    if not(subtractive(inp[i], inp[i+1], inp[i:])):
                        return False
                # Checks the validity of repeated numbers that have a number after them
                elif vals[inp[i]] == vals[inp[i+1]] and len(inp[i:]) == 3:
                    if not(repeated(inp[i+1], inp[i+2])):
                        return False
                elif vals[inp[i]] == vals[inp[i+1]] and len(inp[i:]) > 3:
                    if not(repeated(inp[i+1], inp[i+2]) or subtractive(inp[i+2], inp[i+3], inp[i+2:])):
                        return False
        return True
    else:
        return True


# If repeated characters are followed by a character of lesser or equal value, return true
def repeated(a, b):
    if a > b or a == b:
        return True


# Check to see if two numerals added together are subtractive
def subtractive(a, b, remainder):
    subtractive_chars = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    if a+b in subtractive_chars:
        if len(remainder) >= 3:
            if not(remainder[2] == b):
                return True
        else:
            return True


# Evaluate all the rules, raising a type error to be caught in main if the rules aren't met
def rules(inp, vals):
    if appropriate_characters(inp) and correct_notation(inp, vals):
        return True
    else:
        return TypeError


# Convert the valid input to roman numerals
def convert_numeral_to_num(inp, vals):
    total = 0
    # If the input is one numeral, return its value
    if len(inp) == 1:
        total += vals[inp]
    else:
        i = 0
        # For every value except the last value, check to see if it is subtractive. If not, add the value to total
        while not i >= len(inp) - 1:
            if not(subtractive(inp[i], inp[i+1], inp[i:])):
                total += vals[inp[i]]
                i += 1
            # If the input is subtractive, find the value through subtraction and add it to the total
            else:
                total += (vals[inp[i+1]] - vals[inp[i]])
                # Increment twice to move past the subtractive value
                i += 2
        # If the final value was not subtractive, add it to the total (avoids double counting)
        if not subtractive(inp[-2], inp[-1], inp[-2:]):
            total += vals[inp[-1]]
    return total


def numerals_to_numbers():
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    while True:
        numeral = input('Enter a numeral to convert or \'back\' to return to the start: ')
        if numeral == 'back':
            break
        if not rules(numeral, vals) == TypeError:
            converted_numeral = convert_numeral_to_num(numeral, vals)
            print(f'{numeral} converts to {converted_numeral}')
        else:
            print('Invalid Roman numeral.')


# Check each digit in the given number against a dictionary of values, multiplied by  10, 100, or 1000 for the
# appropriate value
def numbers_to_numerals():
    letters = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
               30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC',
               400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
    while True:
        number = input('Enter a number greater than 0 and less than or equal to 3999 '
                       'or \'back\' to return to the start: ')
        if number == 'back':
            break
        if 0 < int(number) <= 3999:
            roman_numeral = []
            total = 0
            for char in number[::-1]:
                char = int(char) * (10 ** total)
                if not char == 0:
                    roman_numeral.append(letters[char])
                total += 1
            final_num = None
            for numeral in roman_numeral[::-1]:
                if final_num is None:
                    final_num = numeral
                else:
                    final_num += numeral
            print(f'{number} converts to {final_num}')
        else:
            print('Invalid number. Remember to stay within the range of 0 and 3999')


def main():
    while True:
        inp = input('Enter \'numeral\' for numeral to number, \'number\' for number to numeral '
                    'or \'exit\' to end the program: ')
        if inp == 'exit':
            break
        elif inp == 'numeral':
            numerals_to_numbers()
        elif inp == 'number':
            numbers_to_numerals()
        else:
            print('Invalid input. ')


if __name__ == '__main__':
    main()

