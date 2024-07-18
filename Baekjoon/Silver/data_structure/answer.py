from collections import deque

N = int(input())
paper = deque(enumerate(map(int, input().split()), start=1))
# print(paper)  ->   deque([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

# 답안 (터뜨린 순서)
answer = []

# 예외 상황 처리
if N != len(paper):
  exit()
if 0 in [x[1] for x in paper]:
  exit()

for i in range(N):
  # 현재 위치에 해당하는 아이템 pop
  value = paper.popleft()
  # pop한 아이템의 인덱스 추가
  answer.append(value[0])
  print(value[0], end=' ')

  # 종이의 값이 양수이면 왼쪽으로 이동 (-1) -> 현재 위치는 pop되어서 제외
  if value[1] > 0:
    paper.rotate(-(value[1]-1))
  else:
    paper.rotate(-value[1])
