from sys import stdin

N, M = map(int, input().split())
height = list(map(int, input().split()))    # 땅의 높이
rain = set()        # 비가 온 집의 번호

# (주의) 인덱스는 0부터 시작하지만 집 번호는 1부터 시작
for i in range(1, M+1):
	start, end = map(int, stdin.readline().rstrip().split())    # 시작집과 끝집
	# 비가 내리면 해당 땅의 높이를 1 증가하고 비 온 집 리스트에 집 번호 추가
	for j in range(start, end+1):
		height[j-1] += 1
		rain.add(j)
	# 만약 3의 배수 날짜라면 집 리스트에서 집 번호 받아서 해당 집의 높이 1 감소
	if i % 3 == 0:
		while rain:
			drainage = rain.pop()
			height[drainage-1] -= 1

# 구름(+프로그래머스)은 입출력을 철저하게 지켜야 함
for i in height:
	print(i,end=' ')