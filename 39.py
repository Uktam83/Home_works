# Butun son berilgan. Agar son musbat bo’lsa 15 martaga oshiring,
# manfiy bo’lsa absolut qiymatini (ya’ni modulini),
# aks holda berilgan sonning o’zini ekranga chiqaruvchi dastur tuzing.
a = int(input("Son kirting: "))
if a>0:
    print(a*15)
elif a<0:
    print(abs(a))
else:
    print (a)