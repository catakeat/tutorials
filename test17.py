def kwargs(**kwargs):
    for y in kwargs.items():
        print(y[0],y[1])



kwargs(**{'a':97,'b':98,'c':99})
kwargs(jedan=1,dos='two', tres='three', uno='one')