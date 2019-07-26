# pyvec

# Installing pyvec

```bash
pip install pyvec
```

# Usage Example

```python
from vector import *

v1 = Vector()

# Add 3 elements to vector
v1.push_back("a")
v1.push_back("b")
v1.push_back("c")

print v1
print

# ['a', 'b', 'c']

assert(v1.empty() == False)

# Remove last element from vector
v1.pop_back()

print v1 
print
#['a', 'b']

# Add element at specifiec possition
pos = 0
element = "e"
v1.insert(pos, element)

print v1
print

assert(len(v1) == 3)


# Print all elements using begin() & end()

v = v1.begin()

while v != v1.end():
    print v[0]
    v +=1



#e
#a
#b


# clear vector 
v1.clear()

print
print v1 
# []

assert(v1.empty() == True)
```
