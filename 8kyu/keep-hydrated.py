def litres(time):
    litre_drank = time * 0.5
    litre = int(litre_drank)
    return litre

user_input = float(input("enter the time: "))
print(litres(user_input))
