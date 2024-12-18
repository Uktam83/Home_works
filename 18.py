#s = int(input())

#3662 - > 3600sekund+62sekund
'''
1min - 60s
60min->3600s
1soat-> 3600s
24soat->86400s
'''
s = int(input()) 
ss=s//3600#soat
m = (s%3600)//60#minut
print(ss,m)