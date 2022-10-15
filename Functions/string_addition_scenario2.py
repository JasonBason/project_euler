def add_2_strings(str1, str2):
  temp1 = str1
  temp2 = str2
  if len(str1) < len(str2):
      str2 = temp1
      str1 = temp2
    
  counter1 = len(str1) - 1
  counter2 = len(str2) - 1
  answer = ''
  carry = 0
  while counter1 >= 0:
      digit1 = int(str1[counter1])
      digit2 = 0 if counter2 < 0 else int(str2[counter2])
      digit_sum = str(digit1 + digit2 + carry)
      digit = digit_sum[1] if len(digit_sum) > 1 else digit_sum[0]
      carry = int(digit_sum[0]) if len(digit_sum) > 1 else 0
      answer = digit + answer
      counter1 -= 1
      counter2 -= 1
  answer = str(carry) + answer if carry != 0 else answer
  return answer


