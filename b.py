import sys
import a

a.x = sys.modules["b"]
a.v += 1
print(f"{a.x=}")
raise ValueError
