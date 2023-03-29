def foo(a,b):
    foo.licznik +=1
    return a+b
foo.licznik = 0

foo(5,4)
foo(5,4)
foo(5,4)
print(foo.licznik)