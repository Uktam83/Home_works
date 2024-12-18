# Uch xonali son berilgan. Uning raqamlarini teskari tartibda yozilishidan hosil bo’lgan 
# sonni chiqaruvchi dastur tuzilsin. Masalan: 123 --> 321
a = int(input("Iltimos 3 xonali son kiriting: "))
s = a%10
t = (a//10)%10
u = (a//100)%10
c = s*100+t*10+u
print(c)