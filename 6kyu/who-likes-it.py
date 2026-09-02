def likes(names):
    n = len(names)
    
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif n >= 4:
        diff = n - 2
        return f"{names[0]}, {names[1]} and {diff} others like this"


#for user input enter an array and continue :D
