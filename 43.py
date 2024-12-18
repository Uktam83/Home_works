#Uchta butun a, b, c sonlar berilgan. Jumlani rostlikka tekshiring:
# a, b, c sonlarning faqat ikkitasi musbat son.
a = int(input())
b = int(input())
c = int(input())
if (a>0 and b>0 and c<0) or (b>0 and c>0 and a<0) or (a>0 and c>0  and b<0) :
    print("True")
else:
    print("False")