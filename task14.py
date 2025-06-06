#14.​Sinfdagi talabalarning o‘rtacha yoshini hisoblash​
#Shart: Sinfdagi 5 ta talabalarning yoshini kiriting. Ularning o‘rtacha yoshini toping.

n = int(input("Sinfda nechta o'quvchi o'qishini kiriting :"))

jami = 0

for i in range(1,n+1):
    
    oquvchin = int(input(f"{i}-o'quvchi yoshini kiriting :")) 
    
    jami += oquvchin

ortacha = jami/n
    
print(ortacha)
    
    