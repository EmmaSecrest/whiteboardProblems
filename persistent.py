'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
'''
def num_to_array(n):
    number_string = str(n)
    digits = [int(digit) for digit in number_string if digit.isdigit()]
    return digits

def multiply_digits(digits):
    product = 1
    for digit in digits:
        product *= digit  # Corrected line
    return product

def persistence(n):
    digits = num_to_array(n)
    product = multiply_digits(digits)
    product_digits = num_to_array(product)
    persistence = 0
    
    if len(digits) == 1:
        return persistence
    else:
        while len(product_digits) > 1:
            product = multiply_digits(product_digits)
            print("the product so far is:  " , product)
            product_digits = num_to_array(product)
            persistence += 1
        persistence += 1
        return persistence

print(persistence(39))
