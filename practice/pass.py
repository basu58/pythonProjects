list = [1, 2, 3, 4, 5]
flag = 0
for i in list:
    print("Current element:", i, end=" ");
    if i == 3:
        pass
        print("\nWe are inside pass block\n");
        flag = 1
    if flag == 1:
        print("\nCame out of pass\n");
        flag = 0
# pass is just a placeholder for
values = {'P', 'y', 't', 'h', 'o', 'n'}
for val in values:
    pass

for i in [1, 2, 3, 4, 5]:
    if i == 4:
        pass
        print("This is pass block", i)
    print(i)


# Empty Function
def function_name(args):
    pass


# Empty Class
class Python:
    pass
