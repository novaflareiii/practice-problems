import math

def sum_of_two_squares(n):
    result = []
    for a in range(math.isqrt(n) + 1):
        diff = n - a * a
        b = (math.isqrt(diff))
        if b * b == diff and a <= b: 
             result.append([a, b])
    return result


x = int(input("enter a number: "))
print(sum_of_two_squares(x))
   
