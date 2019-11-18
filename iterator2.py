D = {'a':97, 'b':98, 'c':99}
for k in D.keys():
    print(k,D[k])

print(next(iter(D)))

L=range(6)
print(iter(L).__next__())
print(list(L))

E=enumerate('Pyhtron')
print(E.__iter__().__next__())
