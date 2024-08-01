from collections import deque

N, K = map(int, input().split())
# 최대 좌표
max_num = 100000
# 최단 시간 구하기 -> 시간(순서)을 저장할 리스트 (일단 0으로 초기화)
time_arr = [0] * (max_num+1)

# 시작점을 기준으로 하는 큐
queue = deque()
queue.append(N)

while queue:
  X = queue.popleft()
  # 접근한 노드(큐에서 빼낸 값)가 K(목적지)라면 현재 시간 출력하고 마무리
  if X == K:
    print(time_arr[X])
    break
  # 가능한 세 가지 이동 범위 확인
  for move in (X-1, X+1, 2*X):
    # 만약 이동 좌표가 범위 내에 있으면서 접근한 적 없는 좌표라면
    if 0 <= move <= max_num and not time_arr[move]:
      queue.append(move)                # 큐에 이동할 노드 추가
      time_arr[move] = time_arr[X] + 1  # 이동 시간 리스트에 현재 시간 추가
