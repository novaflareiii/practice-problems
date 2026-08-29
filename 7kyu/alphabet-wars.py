def alphabet_war(fight):
    sumup_L = 0
    sumup_R = 0

    for i in range(len(fight)):
        if fight[i] == 'w':
            sumup_L += 4
        elif fight[i] == 'p':
            sumup_L += 3
        elif fight[i] == 'b':
            sumup_L += 2
        elif fight[i] == 's':
            sumup_L += 1

    for i in range(len(fight)):
        if fight[i] == 'm':
            sumup_R += 4
        elif fight[i] == 'q':
            sumup_R += 3
        elif fight[i] == 'd':
            sumup_R += 2
        elif fight[i] == 'z':
            sumup_R += 1

    if sumup_L > sumup_R:
        return "Left side wins!"
    elif sumup_R > sumup_L:
        return "Right side wins!"
    else:
        return "Let's fight again!"

msg = input("enter your string: ")
print(alphabet_war(msg))
