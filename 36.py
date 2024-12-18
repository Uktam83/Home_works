#Berilgan 3 ta sondan bir xil bo’lmaganini ekranga chiqaradigan dastur tuzing.
#Agar barcha sonlar bir xil bo’lsa ‘=’ belgisi chiqsin.
a = int(input())
b = int(input())
c = int(input())
if a == b and a == c and b==c:
    print('=')
elif a==b and b!=c and a!=c:
    print(c)
elif b==c and c!=a and a!=b:
    print(a)
elif a==c and b!=c and b!=a:
    print(b)
else:
    print(a,b,c)