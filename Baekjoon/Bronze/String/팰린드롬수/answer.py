while True:
  try:
    num = input()
    # 0(마지막 값)을 입력받으면 끝
    if num == '0':
      break
    
    if num == num[::-1]:
      print("yes")
    else:
      print("no")

  except:
    break
  
  
'''
while True:
  num = input()
  
  # 마지막 입력값 0을 입력받으면 끝
  if str == '0':
    break
  
  if num == num[::-1]:
    print("yes")
  else:
    print("no")

'''