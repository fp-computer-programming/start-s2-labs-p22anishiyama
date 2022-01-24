# Author: ATN 1/24/22

def sum_nums(first, second):
    # i will be saving this sum into total
    total = 0
    # this will make sure that the two numbers are not equal, then add the two
    if first<second:
        total = first + second
        return total
    # this will check if the two numbers are the same, then will return that value
    elif first == second:
        return first

print(sum_nums(2, 3))
print(sum_nums(4, 4))
