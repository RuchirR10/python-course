#Fstring
import math

me = "Ruchir"
a1 =9

a = "This is %r and he is in %r class"%(me, a1)
#print(a)

a = "This is {1} {0}"
b = a.format(me , a1)

#print(b)

r = f"This is {me} {a1} {math.cos(65)}"
print(r)