weight = float(input("enter weight: "))
measure = input("kgs or lbs: ")

if measure == str("lbs"):    
    print(int(weight * 0.4536))
else: 
    print(weight + measure)
    #1lbs * 0.4536 = kg