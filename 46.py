# Uch xonali a soni berilgan. Shu sondagi eng katta raqamni aniqlovchi dastur tuzing.
a = int(input())
s = a%10
t = (a//10)%10
u = (a//100)%10
m = max(s,t,u)
print(m)