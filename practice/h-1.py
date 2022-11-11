x = set('Book')
y = set('Bookshelves')

p = x.union(y)
print(p)

x = set('Book')
y = set('Bookshelves')

p = x.intersection(y)
print(p)

x = set('Book')
y = set('Zookeeper')

y.difference_update(x)
print(y)

x = set('Book')
y = set('Zookeeper')

y.symmetric_difference_update(x)
print(y)

x = set('Book')
y = set('Zookeeper')

y.intersection_update(x)
print(y)

x = set('Book')
y = set('Zookeeper')

y.difference_update(x)
print(y)