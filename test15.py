def intersect(seq1,seq2):
    res=[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = "WORLD"
s2 = "WORDS"
print(intersect(s1, s2))

ls=[]
x=""
ls=[x  for x in s1 if x in s2]

print(ls)