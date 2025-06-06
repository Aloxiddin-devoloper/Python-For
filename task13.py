#13.​Telefonlarning eng katta va eng kichik narxining o‘rtachasini topish​
#Shart: Telefon do‘konidagi telefonlarning narxlaridan eng yuqori va eng past narxlarni
# toping. Bu o‘rtacha narxni yangi telefonlar uchun belgilash mumkin. Telefonlar soni 5ta.

n = 5  # nechta telefon borligi

prace = int(input("1-telefon narxini kiriting:($)"))

max_prace = prace
min_prace = prace

for i in range(2,n+1):
    
    keyingi_telefonlar = int(input(f"{i} - telefon narxini kiriting :($)"))
    
    if keyingi_telefonlar >max_prace:
        max_prace = keyingi_telefonlar
    
    if keyingi_telefonlar<min_prace:
        min_prace = keyingi_telefonlar
        
print(f"{max_prace,min_prace}")

