ex = 'Super hit'
a = slice(3)
b = slice(2, 4)
c = slice(2, 4, 5)
print(ex[a]) # Sup
print(ex[b]) # pe
print(ex[c]) # p

mystr = 'TutorialsTeacher'
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

portion1 = slice(2, 15, 3)
portion2 = slice(2, 15, 2)
portion3 = slice(2, 15, 4)
portion4 = slice(-2, -5, -2)
print('string: ', mystr[portion1])  # tisae
print('string', mystr[portion2])  # trasece
print('string', mystr[portion3])  # taee

print('nums', nums[portion1])  # 369
print('nums', nums[portion2])  # 3579
print('nums', nums[portion3])  # 3 7
print('nums', nums[portion4])  # 9 7
