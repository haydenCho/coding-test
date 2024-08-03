from collections import defaultdict

T = int(input())

for _ in range(T):
  N = int(input())
  rank_list = list(map(int, input().split()))
  score_dict = defaultdict(lambda: [0, 0, 0])   # {팀 번호: [들어온 선수의 수, 합산점수, 5위 순서]}
  rank = 0    # 순위
  
  # 조건에 안 맞는 팀 제외
  team = defaultdict(int)
  for i in rank_list:
    team[i] += 1
  removed_team = {team for team, count in team.items() if count < 6}
  
  # 유효한 팀만 리스트에 남기기
  rank_list = [team for team in rank_list if team not in removed_team]
  
  # 순회하며 점수 합산 및 순위 저장
  for i in (rank_list):
    rank += 1
    if score_dict[i][0] < 4:  # 첫 4명의 선수까지만 점수 합산
        score_dict[i][1] += rank
    if score_dict[i][0] == 4:  # 5번째 선수의 순위 저장
        score_dict[i][2] = rank
    score_dict[i][0] += 1  # 선수 수 증가

  # 팀 순위 정렬 (점수합산 -> 5위 등수)
  sorted_teams = sorted(score_dict.items(), key=lambda item: (item[1][1], item[1][2]))
  print(sorted_teams[0][0])