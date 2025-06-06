#8.​ Sonning kvadratini yig‘ish​
#Shart: 1 dan N gacha bo‘lgan sonlarning kvadratlarini yig‘ing.

n = int(input())
sum = 0

for i in range(1,n+1):
    sum += i*i
print(sum)