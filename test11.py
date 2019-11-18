import os
for dirpath, dirs, files in os.walk("."):
  for filename in files:
    fname = os.path.join(dirpath,filename)
    print(fname)
    with open(fname) as myfile:
      print(myfile.read())