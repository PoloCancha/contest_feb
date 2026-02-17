from asyncio import print_call_graph

a = [1, 2, 3,]
a.append(27) # adds 1 item to the end
print(a)
b = ["Bob"] * 4
a.extend(b) # adds one list at the end, same as a + b
print(a)

# pip removes by position
x = a.pop(3)
print(x)
print(a)

a.remove("Bob")
print(a)
a.remove(3)
print(a)