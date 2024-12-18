# Uch xonali son berilgan. Uni o’ngdan birinchi raqamni o’chirib, chap tarafiga yozishdan 
# hosil bo’lgan sonni aniqlovchi programma tuzilsin. (Masalan: input - 473, output - 347)
a = int(input("Iltimos 3 xonali son kiriting: "))
s = a%10#3
t = (a//10)%10#7
u = (a//100)%10#4
#473 = u=4,t=7,s=3
#473-347
c = s*100+u*10+t
print(c)