# 3 ta a, b, c sonlar berilgan. Agar shu sonlardan ixtiyoriy biri
# ikkinchisidan 10 taga yoki undan ko’proqqa farq qilsa, ekranga true,
# aks holda false chiqaradigan dastur tuzing.
a = int(input())
b = int(input())
c = int(input())
if a<=(b+10) or a<=(c+10) or b<=(a+10) or b<=(c+10) or c<=(a+10) or c<=(b+10):
    print("True")
else:
    print("False")