#10.​Maximum qiymatni topish​
#Shart: Foydalanuvchi tomonidan kiritilgan 7 ta sondan maximal qiymatni toping.

max_son = int(input("1-sonni kiriting: "))

for i in range(2, 8):
    son = int(input(f"{i}-son kiriting: "))
    if son  > max_son:
        max_son = son
        
print(max_son)

