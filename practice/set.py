x = {1, 2, 3, 'a', 'b', 'c'}
print(x)
print(type(x))
x.add(56)
print(x)
x.add(59)
print(x)
# x.remove(5) if item is not available in set python will give error in case of remove
x.discard(5)  # if item is not available in set python will not give error in case of discard

a = {"Devansh", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}

a.intersection_update(b, c)

print(a)

a = {"Devansh", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}
x = a.intersection(b, c)
print(x)

# The intersection_update() method is different from the intersection() method since it modifies the original set by
# removing the unwanted items, on the other hand, the intersection() method returns a new set.

ab = a - b
print(ab)
ab = b - a
print(ab)

a = {"Devansh", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}

d = a ^ b
print(d)

d = a ^ b ^ c
print(d)

d = a.symmetric_difference(c)
print(d)

Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday"}
Days3 = {"Monday", "Tuesday", "Friday"}

# Days1 is the superset of Days2 hence it will print true.
print(Days1 > Days2)

# prints false since Days1 is not the subset of Days2
print(Days1 < Days2)

# prints false since Days2 and Days3 are not equivalent
print(Days2 == Days3)

# The frozen sets are the immutable form of the normal sets, i.e., the items of the frozen set cannot be changed and
# therefore it can be used as a key in the dictionary.

Frozenset = frozenset([1, 2, 3, 4, 5])
print(type(Frozenset))
print("\nprinting the content of frozen set...")
for i in Frozenset:
    print(i);
# Frozenset.add(6)  # gives an error since we cannot change the content of Frozenset after creation

set1 = {1, 2, 4, "John", "CS"}
set1.update(["Apple", "Mango", "Grapes"])
print(set1)
