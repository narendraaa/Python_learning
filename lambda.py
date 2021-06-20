'''
#lambda funtion
x = lambda a,c,b : a+b+c

print(x(4,5,6))
print('A lambda function is a small anonymous function')

print('A lambda function can take any number of arguments, but can only have one expression' ,end=' ')
##

'''
def myfunc(n):
  return lambda a: a * n

mytripler = myfunc(3)
print(mytripler(7))
#print(mytripler(11))
