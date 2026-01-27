N, M = map(int, input().split())

listens = set()
sees = set()

# 듣도 못한 사람 집합에 추가
for _ in range(N):
  name = input()
  listens.add(name)

# 보도 못한 사람 집합에 추가
for _ in range(M):
  name = input()
  sees.add(name)

# 교집합 구해서 출력
results = list(listens & sees)
print(len(results))
for result in sorted(results):
  print(result)