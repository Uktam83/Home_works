#A son berilgan. Agar A musbat bo’lsa 1 qo’shilgan, 
# manfiy bo’lsa absolyut qiymatiga (moduliga) 2 qo’shilgan,
# aks holda 100 ga bo’lingan qiymatini chiqaruvchi dastur tuzilsin.
a = int(input("Son kiriting "))
# if a>0:
#     print(a+1)
# elif a<0:
#     print(abs(a)+2)
# else:
#     print (a/100)
if a>0:
    c=a+1
elif a<0:
    c=abs(a)+2
else:
    c=a//100
print(c)