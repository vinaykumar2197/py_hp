
# Write a Python program to converting an integer to a string in any base.
def to_string(n,base):
    conv_str = "0123456789ABCDEF"
    if n<base:
        return conv_str[n]
    else:
        return to_string(n//base,base)+ conv_str[n%base]

# print(to_string(2835,16))

#  -------------------------------------------------------------------------

# Write a Python program to calculate the sum of a list of numbers.
def list_sum(num_list):
    if len(num_list) ==1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])

# print(list_sum([2, 4, 5, 6, 7]))

#  -------------------------------------------------------------------------

# Write a Python program of recursion list sum.
def find_sum(list_val):
    total = 0
    for element in list_val:
        if type(element) == type([]):
            total = total + find_sum(element)
        else:
            total = total + element

    return total
# print(find_sum([1, 2, [3,4], [5,6]]))
#  -------------------------------------------------------------------------


# Write a Python program to get the factorial of a non-negative integer.
def factorial(num):
    if num <=1 :
        return 1
    return num*factorial(num-1)

# print(factorial(5))

# -------------------------------------------------------------------------


# Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(num):
    if num ==1 or num ==2 :
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# print(fibonacci(5))

# -------------------------------------------------------------------------

# Write a Python program to get the sum of a non-negative integer.

def sumDigits(number):
    if number == 0:
        return 0
    else:
        return number%10 + sumDigits(number//10)

# print(sumDigits(345))
# print(sumDigits(45))
# -------------------------------------------------------------------------


# 7 Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(numbers):
    if numbers == 0:
        return 0
    else:
        return numbers+sum_series(numbers-2)


print(sum_series(6))
print(sum_series(10))
# -------------------------------------------------------------------------


# Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
def harmonic_sum(number):
    if number ==1:
        return 1
    else:
        return 1/number + harmonic_sum(number-1)


print(harmonic_sum(7))
print(harmonic_sum(4))
# -------------------------------------------------------------------------
