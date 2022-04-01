Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print("Name : %s" % Employee["Name"])
print("Age : %d" % Employee["Age"])
print("Salary : %d" % Employee["salary"])
print("Company : %s" % Employee["Company"])

dic = {}
dic[0] = 'Basu'
dic[1] = 'Dev'
dic[2] = 'Basudev'
print(dic)

dic['name'] = 'Basudev', 'Chhotaray'
print(dic)

print('0 = %s' % dic[0])
print('1 = %s' % dic[1])
print('2 = %s' % dic[2])
print('Name = ', dic['name'])
tu = dir(dic)
print(len(tu))
print(dic.items())
print(dic.values())
print(dic.keys())
print(dic.)


