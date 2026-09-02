def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):
            if numbers[i] + numbers[j] == target:
                return ( i , j)



array = eval(input("Enter your array: "))
tar = int(input("Enter a target number that is in the list: "))
print(two_sum(array, tar))
