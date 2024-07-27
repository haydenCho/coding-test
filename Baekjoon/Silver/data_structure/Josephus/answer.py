from collections import deque

N, M = map(int, input().split())
number = []

# 1부터 N까지 리스트에 저장 후 deque() 사용
for i in range(1, N+1):
  number.append(i)
number = deque(number)

# 답안 (제거한 순서)
answer = []

for i in range(N):
  # 현재 위치에서 M-1만큼 왼쪽으로 이동 (M번째 숫자 제거)
  number.rotate(-(M-1))
  # 해당하는 숫자 제거하고 answer에 추가
  value = number.popleft()
  answer.append(value)

# 결과 출력 (출력 예시를 항상 잘 보자...)
print('<' + ', '.join(map(str, answer)) + '>')
