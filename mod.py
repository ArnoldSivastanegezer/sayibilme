import random

puan=0
a=random.randint(0,10)
b=int(input("hangi rakamı tuttum ?: "))

while True:
    if b <= 0:
        print("rakamlar pozitif olur.")

    elif b >=10:
        print("bu bir rakam değil")
        
    
    if a==b:
        print("DOĞRU!")
        break
    elif a<b:
        print("Aşağı")
        b=int(input("bir daha dene: "))
    else:
        print("Yukarı")
        b=int(input("bir daha dene: "))
       
