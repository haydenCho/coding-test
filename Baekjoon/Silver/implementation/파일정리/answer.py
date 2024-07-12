N = int(input())

type = []
dict = {}

# 파일 확장자만 배열에 추가
for i in range(N):
  file = input().split(".")
  type.append(file[1])

# 확장자를 key, 확장자의 개수를 value로 딕셔너리 채우기 (get(): key값으로 value값 찾는 딕셔너리 함수)
for i in type:
  # 확장자로 값을 찾을 수 있다면 (이미 해당 확장자가 딕셔너리 키로 존재한다면) value(개수) +1
  if dict.get(i):
    dict[i] += 1
  # 해당하는 확장자가 딕셔너리 키에 존재하지 않는다면 추가하기
  else:
    dict[i] = 1

# key를 기준으로 정렬 (리스트로 반환: [('avi', 1), ('jpg', 1), ('png', 1), ('txt', 2)])
answer = sorted(dict.items())

for type, count in answer:
  print(type, count)