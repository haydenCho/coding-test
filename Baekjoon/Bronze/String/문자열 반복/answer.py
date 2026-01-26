T = int(input())

for _ in range(T):
  R, S = input().split()   # 입력값 받아서 저장
  P = ''    # 답안 문자열

  # R만큼 곱해서 문자열 P에 저장
  for s in S:
    P += s * int(R)

  # 답안 출력
  print(P)