n=int(input())
c=0
m=[]
for i in range(n):
    n1=input().split()
    a=n1[0]
    a=int(a)
    b=n1[1]
    b=int(b)
    for i in range(1,a+1):
        c=c+1
    for i in range(0,c,2):
        m.append(i)
    k=len(m)
    l=k*b
    print(l)
    m=[]
    c=0
