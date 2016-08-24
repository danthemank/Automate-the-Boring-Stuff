#Scope example

def func1():
    a = 'b local'
    print(a) # prints 'b local'

def func2():
    a = 'a local'
    print(a) # prints 'a local'
    func1()
    print(a) # prints 'a local'

a = 'a global'
func2()
print(a) # prints 'a global'