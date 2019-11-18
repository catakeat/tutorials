import sys

print(sys.path)


for pt in enumerate(sys.path):
    print(pt)
    print(pt[0],pt[1])
'''
for index,pt in enumerate(sys.path):
    print(index,pt)
'''