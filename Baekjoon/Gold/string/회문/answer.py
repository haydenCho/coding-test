import sys
input = sys.stdin.readline

def check_palindrome(s: str, left: int, right: int) -> int:
  while left <= right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    else:
      return False
  return True

def twoPointer(s: str) -> int:
  left = 0
  right = len(s) - 1
  while left <= right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    else:     # 중간에 다른 문자가 발견되면
      check1 = check_palindrome(s, left + 1, right)   # 왼쪽 하나 건너뛰어보기
      check2 = check_palindrome(s, left, right - 1)   # 오른쪽 하나 건너뛰어보기
      
      if check1 or check2:    # 둘 중 하나라도 회문이라면
        return 1
      else:
        return 2
  
  return 0

T = int(input())    # 개수 받기
results = []        # 회문 여부를 담을 리스트

# 회문 여부 확인
for _ in range(T):
  value = input().strip()
  results.append(twoPointer(value))

# 출력
for result in results:
  print(result)

'''
def twoPointer(s: str) -> int:
  num = 0
  left = 0
  right = len(s) - 1
  while left <= right:
    if s[left] == s[right]:
      left += 1
      right -= 1
    else:     # 중간에 다른 문자가 발견되면
      if s[left + 1] == s[right]:
        left += 1
        num += 1
      elif s[left] == s[right - 1]:
        right -= 1
        num += 1
      else:
        return 2
  
  return num

T = int(input())    # 개수 받기
results = []        # 회문 여부를 담을 리스트

# 회문 여부 확인
for _ in range(T):
  str = input().rstrip()
  result = twoPointer(str)
  if result >= 2:
    results.append(2)
    continue
  results.append(result)

# 출력
for result in results:
  print(result)

'''