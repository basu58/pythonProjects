Dist_1 = "5km,124m"
Dist_2 = "2km,432m"
str1 = Dist_1.replace('km', '')
str2 = str1.replace(',', '')
str3 = str2.replace('m', '')
str4 = Dist_2.replace('km', '')
str5 = str4.replace(',', '')
str6 = str5.replace('m', '')
print(int(str3) - int(str6))