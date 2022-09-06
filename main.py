
a = "The quick brown fox jumps over the lazy dog"
for i in a.split():
    print(i)

b = list(range(100))
print(b)

c = []
for i in b:
    c.append(i**2)
print("---")
print(c)

h = {}
for elem in c:
    h[elem] = str(elem)*3
print(h)


g = c[-1::-1]
print("---")
print(g)
