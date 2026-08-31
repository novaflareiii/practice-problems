def valid_phone_number(ph):
    if len(ph)!= 14:
        return False
    if ph[0] != '(' or ph[4] != ')' or ph[5] != ' ' or ph[9] != '-':
        return False
    for i in range(len(ph)):
        if i in (0,4,5,9):
            continue
        if not ph[i].isdigit():
            return False
        
    return True

msg = input("Enter A Phone Number: ")
print(valid_phone_number(msg))



''' 
"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
'''
