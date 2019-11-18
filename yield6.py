'''
def f():
    while True:
        val=yield
        yield val*10


g=f()
print(g.next())
g.send(1)
'''
def f():
    while True:
        val = yield
        yield val*10
g = f()
g.next()
g.send(1)
10
g.next()
g.send(10)
100
g.next()
g.send(0.5)