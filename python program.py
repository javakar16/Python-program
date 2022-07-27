#finding the number appearence in the given loop;
n1=0
a=[]
m=list(map(int,input().split()))
for i in range(m[0],m[1]+1):
    a.append(str(i))
s=0
for i in a:
    if str(n1) in i:
        s=s+1
print(s)
        
    
