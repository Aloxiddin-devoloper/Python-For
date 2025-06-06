#5.​ Sonlar ketma ketligi​
#Shart: for loop dan foydalanib foydalanuvchi kiritgan i butun sondan boshlab
# foydalanuvchi kiritgan n butun songacha barcha butun sonlarni chiqaring.

i = int(input()) #boshlangan son
n = int(input()) #tugagan son

if i<n:
    for sonlar in range(i,n+1):
        print(sonlar)
else:
    for sonlar in range(n,i+1):
        print(sonlar)