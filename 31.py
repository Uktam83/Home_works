# Uch xonali son berilgan. Uni o’ngliklar xonasidagi raqam bilan yuzliklar xonasidagi 
# raqamni almashtirishdan hosil bo’lgan sonni aniqlovchi programma tuzilsin. Input: n=358. Output: 538.
a = int(input("Iltimos 3 xonali son kiriting: "))
s = a%10
t = (a//10)%10
u = (a//100)%10
c = t*100+u*10+s
print(c)