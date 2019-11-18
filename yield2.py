def gen(n):
    while True:
        yield n
        #print(n)
        n+=1

rez=gen(2)
for _ in range(10):
 print(next(rez))
