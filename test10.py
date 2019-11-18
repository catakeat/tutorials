import os

#print(os.walk("top", topdown=True, onerror=None, followlinks=False))

for dirpath, dirs,diles in os.walk("."):
    print (dirpath,dirs,diles)
