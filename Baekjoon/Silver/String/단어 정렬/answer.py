N = int(input())

# 중복 제거를 위해 set 사용
words_set = set()
for _ in range(N):
  item = input()
  words_set.add(item)

# 리스트로 바꾸고 정렬
words = sorted(list(words_set), key= lambda x: (len(x), x))
for word in words:
  print(word)