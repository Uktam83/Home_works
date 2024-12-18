# 4 ta a, b, c, d son berilgan, kattasidan kichigini ayirib ekranga natijani chiqaruvchi,
# agar u sonlar o’zaro teng bo’lsa yig’indisini ekranga chiqaruvchi dastur tuzing.
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
d = int(input("d= "))
if a!=b!=c!=d:
    m = max(a,b,c,d)
    mn = min(a,b,c,d)
    print(m-mn)
elif a==b==c==d:
    print(a+b+c+d)