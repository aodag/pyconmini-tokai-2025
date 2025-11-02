import dis

x = 1

def f():
    x = 2
    def f():
        print(x)
    return f


print(eval("f()", locals={"x": -33})())
c = dis.Bytecode(f())
print(type(c))
for op in c:
    print(op)
exec(c.codeobj, closure="x")

