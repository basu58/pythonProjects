# Python count() function example
# Variable declaration
str = "Hello Basudev"
str2 = str.count('a')
# Displaying result
print("occurrences:", str2)

# Variable declaration
str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a')
# Displaying result
print("occurrences:", oc)

# Variable declaration
str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a', 3)
# Displaying result
print("occurrences:", oc)

# Variable declaration
str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a', 3, 8)
# Displaying result
print("occurrences:", oc)

# Variable declaration
str = "ab bc ca de ed ad da ab bc ca 12 23 35 62"
oc = str.count('2')
# Displaying result
print("occurrences:", oc)
