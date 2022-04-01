# Write a Python program to remove the parenthesis area in a string.
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for x in items:
    ind1 = x.index('(')
    ind2 = x.index(')')
    x = "" + x[:ind1] + x[(ind2 + 1):]
    print(x)
