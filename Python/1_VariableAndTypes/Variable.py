a = 5
print(id(a))

a = 10
print(id(a))

print(type(a))

b = a + 3j
print(type(b))

c = 10

d = 20

print(a,b) # 10 (10+3j)
print(c,d) # 10 20

# end
print(a,b,end=",") # 10, (10+3j), 10
print(c,d)


print(a,b,c,sep=", ") # 10, (10+3j), 10

# format specifiers
x= 20
print("value of x is %d"%(x))
