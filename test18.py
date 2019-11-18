def fnc(*args, **kwargs):
   print('{} {}'.format(args, kwargs))

print('fnc()')
fnc()
fnc(1,2,3)
fnc(1,2,3,'flask')
fnc(a=1, b=2, c=3)
fnc(a=1, b=2, c=3, d='ansible')
fnc(1, 2, 3, a=1, b=2, c=3)

lst = [1,2,3]
tpl = (4,5,6)
dct = {'a':7, 'b':8, 'c':9}

fnc(*lst, **dct)
fnc(*tpl, **dct)

fnc(1,2,*lst)
fnc(1,2,*tpl)
fnc('jupyter',**dct)
fnc(arg='django',**dct)
fnc(1,2,*tpl,q='bottle',**dct)
print

def fnc2(arg1, arg2, *args, **kwargs):
   print('{} {} {} {}'.format(arg1, arg2, args, kwargs))

print('fnc2()')
#fnc2() # error
fnc2(1,2)
fnc2(1,2,3,'haystack')
fnc2(arg1=1, arg2=2, c=3)
fnc2(arg1=1, arg2=2, c=3, d='Spark')
fnc2(1,2,3, a=1, b=2)
fnc2(*lst, **dct)
fnc2(*tpl, **dct)
fnc2(1,2,*tpl)
fnc2(1,*tpl,d='nltk')
fnc2(1,2,*tpl,d='scikit')

