def keep_order(ary, val):

    ary.append(val)
    ary.sort()
    return ary.index(val)

ary = eval(input("enter your array")) #-->ary = list(map(int, input("enter your array: ").split()))   , much safer
val = int(input("enter a value: "))
print(keep_order(ary , val))
