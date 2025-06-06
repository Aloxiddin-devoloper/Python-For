#3.​ Sonlar ketma ketligi​
#Shart: for loop dan foydalanib foydalanuvchi kiritgan butun sondan boshlab 15 gacha barcha butun sonlarni chiqaring.

a = int(input())
n =15


if a<15:
    for i in range(a,n+1):
        print(i)
else:
    for i in range(n,a+1):
        print(i)
