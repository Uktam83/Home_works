#Berilgan 4 xonali sonda minglar yoki birlar xonasida 3 raqami ishtirok etgan
#yoki etmaganligini aniqlaydigan dastur tuzing.
a = int(input("4 xonali son kiriting: "))
s = a%10
t = (a//10)%10
u = (a//100)%10
v = (a//1000)%10
if s == 3 or v == 3:
    print("ishtirok etgan")
else:
    print("ishtirok etmagan")