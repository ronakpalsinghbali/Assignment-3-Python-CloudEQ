# Difference between == and === :-
# == operator checks whether the value is equal or not, i.e it checks the equality of the values.
# === operator check the identity of the two values i.e checks the type of the values.




s = "Ronak"
for a in s:
    if a == "o" :
        pass                             # This will do nothing as this is a null operation.
    elif a == "a":
        print("\'a\' just got skipped")
        continue                         # This will skip 'a' and will return back to the loop.
    print(a)


print()

for x in range (10):
    if x == 5:
        break                           # This will break the loop when 'x' will be equal to 5.
    x = x + 1
    print(x)        
      

print()      
       
for z in range (1,21,2):
    print(z)                           # This will print all the numbers between 1 and 21 with a setp size of 2, i.e this will print all the odd numbers from 1 to 21.
