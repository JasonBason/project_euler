# check_list =   [11,12,13,14,15,16,17,18,19,20]
check_list =   [3,5]

upperlimit = 999999999
remainderFlag = False

for num in range(31, 50, 1):
  remainderFlag = False
  for i in range(len(check_list)):
    if remainderFlag == True:
      break
    if num % check_list[i] == 0:
      continue
    # print(num)
    remainderFlag = True
    break
  if remainderFlag == False:
    print(num)