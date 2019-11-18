s="picasso"

a="X"+s[1:]
print(a)

b=s[0:2]+"X"+s[3:]
print(b)


replaced_s=s.replace("ss","tt")
print("Dupa replace ",replaced_s)

print("Info despre s ",dir(s))

class Test:
    pass

tst=Test()
print("__dict__ for class Test ",tst.__dict__ )

#print(" __dict fc depsre s ",s.__dict__())
a=None

if a==True:
    print("true")
else:
    print("false")

if a is not True:
  print("true")
else:
 print("false")