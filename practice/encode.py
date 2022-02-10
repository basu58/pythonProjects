# Python encode() function example
# Variable declaration
str = "HELLO"
encode = str.encode()
# Displaying result
print("Old value", str)
print("Encoded value", encode)

# Ë into default encoding.
# Variable declaration
str = "HËLLO"
encode = str.encode()
# Displaying result
print("Old value", str)
print("Encoded value", encode)

'''str = "DËV"
encode = str.encode('ascii')
print('Old Value', str)
print('encode value', encode)'''

# Python encode() function example
# Variable declaration
str = "HËLLO"
encode = str.encode("ascii", "ignore")
# Displaying result
print("Old value", str)
print("Encoded value", encode)

txt = "My name is Ståle"
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

from encodings.aliases import aliases

# Printing list available
print("The available encodings are : ")
for i in aliases.keys():
    print(i)
