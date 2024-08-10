N = int(input())
max_num = list(map(int, input().split()))
init_num = list(map(int, input().split()))
K = int(input())

for _ in range(K):
	init_num[N-1] += 1
	
	# 맨 왼쪽은 따로 확인(N-1부터 1까지만 확인)
	for i in range(N - 1, 0, -1):
		if init_num[i] > max_num[i]:
			init_num[i] = 0
			init_num[i-1] += 1
	
	# 맨 왼쪽 확인
	if init_num[0] > max_num[0]:
		init_num[0] = 0

print(''.join(map(str, init_num)))
