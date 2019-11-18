def cubic(n):
    for i in range(n):
        yield i**3

cub=cubic(5)

for _ in range(3):
    print(next(cub));print(next(cub))
    #print(cub.__next__())