from sys import stdin
from collections import defaultdict
import heapq

N = int(stdin.readline().strip())    # 문제 개수
min_heap = []       # 난이도 낮은 순
max_heap = []       # 난이도 높은 순
problems = defaultdict(int)   # 문제번호와 난이도 저장

for _ in range(N):
  problem, level = map(int, stdin.readline().rstrip().split())
  heapq.heappush(min_heap, (level, problem))
  heapq.heappush(max_heap, (-level, -problem))      # 최소힙만 지원 -> 최대힙은 - 붙이고 pop할 때도 - 붙이기
  problems[problem] = level

M = int(stdin.readline().strip())    # 명령어 개수
for _ in range(M):
  query = list(stdin.readline().rstrip().split())
  # add만 3개의 입력 내용이 존재함 -> 따로 처리해주기
  if len(query) == 2:
    query_1, query_2 = query[0], int(query[1])    # query_2 - solved: 문제 번호 / recommend: 1 or -1
  else:
    query_1, query_2, query_3 = query[0], int(query[1]), int(query[2])
  
  # 명령어가 add이면 데이터 추가 과정 진행
  if query_1 == 'add':
    heapq.heappush(min_heap, (query_3, query_2))
    heapq.heappush(max_heap, (-query_3, -query_2))
    problems[query_2] = query_3
  # 문제 풀었으면 추천 리스트에서 해당 문제 난이도를 -1로 저장하여 풀었음을 표시
  elif query_1 == 'solved':
    problems[query_2] = -1
  # 명령어가 recommend이면 상황에 따라 문제 추천
  else:
    # 값이 1이면 가장 어려운 문제 + 문제 번호 큰 순서대로
    if query_2 == 1:
      while True:
        level, problem = -max_heap[0][0], -max_heap[0][1]
        # 현재 최대힙에 존재하는 난이도와 문제 리스트에 존재하는 난이도가 같다면 문제 번호 출력
        if problems[problem] == level:
            print(problem)
            break
        # 만약 현재 최대힙에 존재하는 난이도와 문제 리스트에 존재하는 난이도가 다르다면 해당 문제는 유효하지 않은 것이므로 pop
        heapq.heappop(max_heap)
    # 값이 -1이면 가장 쉬운 문제 + 문제 번호 작은 순서대로
    else:
      while True:
        level, problem = min_heap[0]
        # 현재 최소힙에 존재하는 난이도와 문제 리스트에 존재하는 난이도가 같다면 문제 번호 출력
        if problems[problem] == level:
            print(problem)
            break
        # 만약 현재 최소힙에 존재하는 난이도와 문제 리스트에 존재하는 난이도가 다르다면 해당 문제는 유효하지 않은 것이므로 pop
        heapq.heappop(min_heap)