#12.​Juft va toq sonlarning yig‘indisini alohida hisoblash​
#Shart: 1 dan boshlab foydalanuvchi tomonidan kiritilgan n soniga qadar bo‘lgan juft
# va toq sonlarning yig‘indisini alohida hisoblang.

n = int(input("oxirgi sonni kiriting :"))

juft = 0
toq = 0

for i in range(1,n+1):
    if i %2 ==0:
        juft +=i
    
    if i%2 ==1:
        toq += i
print(juft,",",toq)