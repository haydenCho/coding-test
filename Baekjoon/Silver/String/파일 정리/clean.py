import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

# 빈 리스트에 확장자만 담아서 Counter에 전달
extensions = []
for _ in range(N):
    extensions.append(input().rstrip().split('.')[1])

# Counter로 개수 세기
results_counts = Counter(extensions)

# 정렬 및 출력
for key in sorted(results_counts.keys()):
    print(key, results_counts[key])