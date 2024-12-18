# Berigan 3 xonali sonning raqamlari ko’paymasini toping.
a = int(input("Iltimos 3 xonali son kiriting: "))
s = a%10
t = (a//10)%10
u = (a//100)%10
print (s*t*u)