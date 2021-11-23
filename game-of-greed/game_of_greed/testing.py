
a = [1,2,3]
b = [4,5,6] 
l = zip(a,b)
m = map(lambda x: x[0]*x[1], l)
r = reduce(lambda x,y: x + y, m)