#9.​ Minimal qiymatni topish​
#Shart: Foydalanuvchi tomonidan kiritilgan 7 ta sondan minimal qiymatni toping.

min_son = int(input("1-sonni kiriting: "))

for i in range(2,8):  
    son = int(input(f"{i}- kiriting: "))
    if son  < min_son:
        min_son = son

print(min_son)
