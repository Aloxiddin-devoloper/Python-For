#11.​Eng katta va eng kichik son o‘rtachasi​
#Shart: Foydalanuvchi tomonidan kiritilgan n ta sonidan eng katta va eng kichik
#     sonlarning o‘rtachasini toping.

n = int(input("nechta son kiritasiz(n) :"))

number = float(input("1-sonni kiriting: "))
max_num = number
min_num = number

for i in range(2, n+1):
     
    numbers = float(input(f"{i}-sonni kiriting: "))
    
    if numbers > max_num:
        max_num = numbers
        
    if numbers < min_num:
        min_num = numbers

resalt = (max_num + min_num) / 2

print(resalt)



        

        


                
            


            