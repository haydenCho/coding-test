record = list(input())
cnt = {'q':0, 'u':0, 'a':0, 'c':0, 'k':0}
active_ducks = 0      # 현재 울고 있는 오리 수 ('quack'이 미완성인 울음수)
answer_ducks = 0      # 오리의 마릿수

# 애초에 틀린 경우(문자열의 길이가 5의 배수가 아님) 제거
if len(record) % 5 != 0:
  print(-1)
  exit()

# 문자열을 순회하며 딕셔너리 값 증가 & 문자 개수 비교(올바른 순서라면 앞의 글자가 뒤의 글자보다 개수가 많아야 한다.)
for char in record:
    if char == 'q':
        cnt['q'] += 1
        active_ducks += 1
        # 전체 오리의 수는 현재 울고 있는 오리의 최대값
        answer_ducks = max(answer_ducks, active_ducks)
    elif char == 'u':
        if cnt['q'] > cnt['u']:
            cnt['u'] += 1
        else:
            print(-1)
            exit()
    elif char == 'a':
        if cnt['u'] > cnt['a']:
            cnt['a'] += 1
        else:
            print(-1)
            exit()
    elif char == 'c':
        if cnt['a'] > cnt['c']:
            cnt['c'] += 1
        else:
            print(-1)
            exit()
    elif char == 'k':
        if cnt['c'] > cnt['k']:
            cnt['k'] += 1
            active_ducks -= 1
        else:
            print(-1)
            exit()
    else:
        print(-1)
        exit()

# 모든 'quack'이 완성되었는지 확인
if cnt['q'] == cnt['u'] == cnt['a'] == cnt['c'] == cnt['k']:
    print(answer_ducks)
else:
    print(-1)