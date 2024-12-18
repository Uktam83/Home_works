# A, B va C sonlar berilgan. A ni qiymati B ga, B ni qiymati C ga va C ni qiymati A ga almashtirilsin.
# A, B va C ning yangi qiymati ekranga chiqarilsin.
A, B, C = map(int, input().split())
A, B, C = B, C, A
print (A, B, C)