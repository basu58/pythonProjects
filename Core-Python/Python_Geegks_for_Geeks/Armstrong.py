num = 1634
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
if sum_of_powers == num:
    print("Arm")
else:
    print("Not Arm")
