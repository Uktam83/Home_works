#478-784
#a = int(input())
def mus(a):
    b = a%10#8
    u = (a//10)%10#7
    y = (a//100)%10#4
    c = u*100+b*10+y
    return c
#print(c)
def man(a):
    n=abs(a)
    bb = n%10#8
    uu = (n//10)%10#7
    yy = (n//100)%10#4
    cc = uu*100+bb*10+yy
    return cc*-1
a=int(input())
if a>0:
    print(mus(a))
else:
    print(man(a))