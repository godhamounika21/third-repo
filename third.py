program-1
st=input('enter any string:')
st1=set(st)
d={}.fromkeys(st1,0)
for i in st:
    d[i]=d[i]+1
print(d)
