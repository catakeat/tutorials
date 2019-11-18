def square(nums):
    for i in nums:
        yield(i*i)

gen=square([1,2,3,4,5])

for x in gen:
    print(x)