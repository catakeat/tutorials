def foo():
    yield 1
    yield 2
    yield 3

for x in foo():
    print(x)

test=foo()
for t in test:
#    print(next(test))
     print(t)