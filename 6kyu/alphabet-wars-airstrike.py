def alphabet_war(fight):
    
    new_fight = []
    for i in range(len(fight)):
        if fight[i] == '*':
            continue
        leftstarcheck = i>0 and fight[i-1] == '*'
        rightstarcheck = i<len(fight)-1 and fight[i+1] == "*"
        
        if not leftstarcheck and not rightstarcheck:
            new_fight.append(fight[i])
        
        
    sumup_L = 0
    sumup_R = 0
    
    for i in range(len(new_fight)):
        if new_fight[i] == 'w':
            sumup_L += 4
        elif new_fight[i] == 'p':
            sumup_L += 3
        elif new_fight[i] == 'b':
            sumup_L += 2
        elif new_fight[i] == 's':
            sumup_L += 1

    for i in range(len(new_fight)):
        if new_fight[i] == 'm':
            sumup_R += 4
        elif new_fight[i] == 'q':
            sumup_R += 3
        elif new_fight[i] == 'd':
            sumup_R += 2
        elif new_fight[i] == 'z':
            sumup_R += 1

    if sumup_L > sumup_R:
        return "Left side wins!"
    elif sumup_R > sumup_L:
        return "Right side wins!"
    else:
        return "Let's fight again!"

msg = input("enter your string: ")
print(alphabet_war(msg))
