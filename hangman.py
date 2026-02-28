from wonderwords import RandomWord
r = RandomWord()

a= r.word(word_min_length=3, word_max_length=5)
attempts=5
stat=0

print(f"Welcome to HANGMAN \nThe word is {len(a)} letters long")
print("_ "* len(a))
print("You have 5 attempts")


while stat==0:
    i=input("\nGUESS: ")
    if i.isalpha():
        if i==a:
           print(f"Bingo you won! With {attempts} attempts remaining")
           break
        
        elif len(i)!=len(a):
            print(f"{len(a)-len(i)} words are missing")
            attempts-=1
            print(f"\n{attempts} attempts are remaining")     
        else:
             for n in range(len(a)):
               if i[n]==a[n]:
                print(i[n],end="")
                               
               else:
                print("_",end="")        
             attempts-=1         
             print(f"\nYou {attempts} attempts are remaining")     
        if attempts==0:
         print(f"Ohh! Try again next time.\nThe word was {a}")  
         break   

    else:
        print("Only Alphabets")    


