# To’rt xonali son berilgan. Uning raqamlari ko’paytmasini hisoblovchi dastur tuzilsin.
a = int(input("Iltimos 4 xonali son kiritng: "))
s = a%10
t = (a//10)%10
u = (a//100)%10
v = (a//1000)%10
print(s*t*u*v)