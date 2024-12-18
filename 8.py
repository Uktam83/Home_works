# 4 xonali son berilgan.
# Soning o’nlar va minglar xonasidagi raqamlar ko’paytmasini aniqlovchi dastur tuzing.
a = int(input("Iltimos 4 xonali son kiriting: "))
s = a%10
t = (a//10)%10
u = (a//100)%10
v = (a//1000)%10
print(t*v)