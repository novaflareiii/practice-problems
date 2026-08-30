def count_bits(n):
    count = 0
    binary_n = bin(n)
    len1 = len(binary_n)
    for i in range(len1):
        if str(binary_n[i]) == '1':
            count+=1
    return count

print(count_bits(1234))
