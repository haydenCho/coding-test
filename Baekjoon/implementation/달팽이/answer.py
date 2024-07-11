N = int(input())
target = int(input())
mat = [[0] * N for _ in range(N)]

# 가운데에 1 넣기
x, y = N//2, N//2
mat[x][y] = 1

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 2
turn = 1    # 두 번씩 반복한 횟수
i = 0       # dx,dy 가리키는 변수
answer = [x+1,y+1]

# 숫자를 전부 할당할 때까지 상, 우, 하, 좌 방향 순서로 좌표 이동
while x != 0 or y != 0:
  flag = 0
  for _ in range(2):
    for _ in range(turn):
      x += dx[i]
      y += dy[i]
      mat[x][y] = num
      if num == target:
          answer = [x + 1, y + 1]
      if x == 0 and y == 0: 
        flag = 1
        break
      num += 1
    
    if flag == 1: break
    i = (i+1)%4
  turn += 1

for row in mat:
  print(*row)

print(*answer)
