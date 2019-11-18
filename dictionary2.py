keys = ['a', 'b', 'c']
values = [1, 2, 3]

print(list(zip(keys,values)))

D2={}
for(k,v) in zip(keys,values):
    D2[k]=v

print(D2)
D={k:v for (k,v) in zip(keys,values)}

print(D)

print(dict(zip(keys,values)))

for el in D.keys():
    print(el)
for index,el in D.items():
    print(k," ",v)