#4.​ Sonlar ketma ketligi​
#Shart: for loop dan foydalanib foydalanuvchi kiritgan i butun sondan boshlab 15
#gacha barcha butun sonlarni foydalanuvchi kiritgan step butun son qadam bilan chiqaring.

n = 15
i = int(input())
step = int(input())

if i<15:
    for number in range(i,15,step): 
        print(number)
else:
    for number in range(15,i+1,step):
        print(number)