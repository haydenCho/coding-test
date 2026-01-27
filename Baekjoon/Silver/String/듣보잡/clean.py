import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listens = {input().rstrip() for _ in range(N)} # 듣도 못한 사람 집합에 추가
sees = {input().rstrip() for _ in range(M)}    # 보도 못한 사람 집합에 추가

# 교집합
results = sorted(listens & sees)

# 출력
print(len(results))
print('\n'.join(results))