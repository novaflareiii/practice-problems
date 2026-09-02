def solution(number):
    sum = 0
    for i in range(number):
        if i%3 == 0:
            sum += i
        elif i%5 == 0:
            sum += i
        else :
            continue
    return sum

num = int(input("Enter a number: "))
print(solution(num))
