# from snake case to camel
str = 'basudev_chhotray'
str = str.replace("_", " ")
str = str.title()
str = str.replace(" ", "")
print(str)