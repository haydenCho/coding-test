import re
import sys
input = sys.stdin.readline

T = int(input())
pattern = re.compile(r'^[A-F]?A+F+C+[A-F]?$')

for _ in range(T):
  input_data = input().rstrip()
  if pattern.match(input_data):
    print("Infected!")
  else:
    print("Good")


'''
init = ['A', 'B', 'C', 'D', 'E', 'F']

results = []
for _ in range(T):
  input_data = input().rstrip()
  strs = ''
  strs += input_data[0]
  
  # 다른 문자가 나올 때마다 저장
  for i in range(1, len(input_data)):
    if input_data[i] != input_data[i-1]:
      strs += input_data[i]
  
  if strs[0] in init and strs[-1] in init and 'AFC' in strs:
    results.append(1)
  else:
    results.append(0)
    
for result in results:
  if result:
    print("Infected!")
  else:
    print("Good")
'''