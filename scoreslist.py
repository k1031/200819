s=[]
o=[]
x=0
n=100
t=0
k=0
k2=0
for i in range(5):
    a=int(input('成績'))
    c=input('名字')
    s.append(n)
    o.append(c)
    if a>x:
        x=n
        k=i
    if a<n:
        n=a
        k2=i
    t=t+n
b=t/len(s)
print('總分',t)
print('平均',b)
print('best',o[k])
print('worst',o[k2])

        
        