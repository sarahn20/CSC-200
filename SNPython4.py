#Assignment Description: Write the necessary code to convert a string representation of a binary number into its decimal equivalent.  
#           For example: "11011101" should convert to 221.  Your program should work for any binary number.

#My Code:

binary_num = '11011101'
multiplier = 1
final_decimal = 0
for i in range(len(binary_num)-1,-1,-1):
  decimal_num = (int(binary_num[i])) * (multiplier)
  final_decimal = final_decimal + decimal_num
  multiplier = multiplier * 2
  i = i + 1
print(final_decimal)

