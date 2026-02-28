import random

words=['TABLE','CHAIR','BOOKS','CLOTH']
a=random.choice(words)
print(a)

var=0
while var==0:
    i=input("Word: ").upper()
    
    
    if i ==a:
        print("Bullseye!")
        var=1
        break
    else:
        print("Matching letters:", "".join([ch for ch in a if ch in i]))
        print("Try again")    




    