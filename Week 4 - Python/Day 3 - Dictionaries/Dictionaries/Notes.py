l=[]
for i in range(10):
    l.append(i**2)

print (l)

l= [i**2 for i in range(10)]

print (l)

d = {}
for i in range(10):
    d[str(i)] = i**2

print(d)

d = {str(i):i**2 for i in range(10)}

print(d)

conditional list generation
l = [do stuff if conditional else do other stuff for element in iterable]

conditional list generation 2 (filtered iterable)
l = [do stuff for element in iterable if condition]



def calculation(a, b):
    return a+b, a-b