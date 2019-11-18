def print_all(*args):
    for index,x in  enumerate(args):
        print(index,x)


print_all(1,2,3,4,5)

print_all('A','b','b','a')