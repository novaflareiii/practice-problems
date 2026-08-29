def first_non_repeated(s):
    count = {}
    for char in s:
        if char in count:
            count[char] = count[char] + 1
        else :
            count[char] = 1
            
    result = sorted(count.items() , key = lambda x : x[1])[0]
    if result[1] == 1:
        return result[0]       
    else:
        return None

msg = input("enter your string: ") #-->for user input
print(first_non_repeated(msg)) #--> for user input
