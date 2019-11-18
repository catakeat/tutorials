def fnc(*args, **kwargs):
   #print('{} {}'.format(args, kwargs))
    print(args,kwargs)


lst = [1,2,3]
tpl = (4,5,6)
dct = {'a':7, 'b':8, 'c':9}

fnc(*lst, **dct)
fnc(*tpl, **dct)

fnc(1,2,*tpl,q='bottle',**dct)