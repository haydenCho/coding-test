## 문제 추천 시스템 Version 1
https://www.acmicpc.net/problem/21939
### 문제
tony9402는 최근 깃헙에 코딩테스트 대비 문제를 직접 뽑아서 "문제 번호, 난이도"로 정리해놨다.

깃헙을 이용하여 공부하시는 분들을 위해 새로운 기능을 추가해보려고 한다.

만들려고 하는 명령어는 총 3가지가 있다. 아래 표는 각 명령어에 대한 설명이다.

|명령어|설명|
|------|-----|
|recommend $x$|	$x$가 1인 경우 추천 문제 리스트에서 가장 어려운 문제의 번호를 출력한다. <br/>만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것으로 출력한다. <br/>$x$가 -1인 경우 추천 문제 리스트에서 가장 쉬운 문제의 번호를 출력한다. <br/>만약 가장 쉬운 문제가 여러 개라면 문제 번호가 작은 것으로 출력한다.|
|add $P$ $L$|추천 문제 리스트에 난이도가 $L$인 문제 번호 $P$를 추가한다. <br/>(추천 문제 리스트에 없는 문제 번호 $P$만 입력으로 주어진다. 이전에 추천 문제 리스트에 있던 문제 번호가 다른 난이도로 다시 들어 올 수 있다.)|
|solved $P$|추천 문제 리스트에서 문제 번호 $P$를 제거한다. (추천 문제 리스트에 있는 문제 번호 $P$만 입력으로 주어진다.)|
 	
- 명령어 recommend는 추천 문제 리스트에 문제가 하나 이상 있을 때만 주어진다.
- 명령어 solved는 추천 문제 리스트에 문제 번호가 하나 이상 있을 때만 주어진다.

위 명령어들을 수행하는 추천 시스템을 만들어보자.


<br />

### 입력
첫 번째 줄에 추천 문제 리스트에 있는 문제의 개수 
$N$ 가 주어진다.

두 번째 줄부터 
$N + 1$ 줄까지 문제 번호 
$P$와 난이도 
$L$가 공백으로 구분되어 주어진다.

 
$N + 2$줄은 입력될 명령문의 개수 
$M$이 주어진다.

그 다음줄부터 
$M$개의 위에서 설명한 명령문이 입력된다.

<br />

### 출력
recommend 명령이 주어질 때마다 문제 번호를 한 줄씩 출력한다. 최소 한번의 recommend 명령어가 들어온다.

<br />

### 제한
$1 \le N, P \le 100,000$ 
 
$1 \le M \le 10,000$ 
 
$1 \le L \le 100$, 
$L$은 자연수
 
$x = \pm 1$ 

<br />

## 풀이
- 최소힙과 최대힙으로 문제 정렬
    - heapq 내장 모듈 사용
- 문제 리스트에서 유효한 문제인지 확인 필요
    - 딕셔너리 생성해서 문제 번호에 해당하는 난이도 저장
    - 문제를 풀면(solved 명령어) 해당 번호의 난이도를 -1로 변경하여 풀었음(유효하지 않음)을 표현
    - collections 모듈의 defaultdict 자료형 사용해서 구현

<br />

## 공부한 개념
- 자료 구조
    - https://jin-network.tistory.com/127
- defaultdict
    - https://00h0.tistory.com/24
- 파이썬의 힙
    - heapq 모듈
    - 파이썬은 최소힙만 지원 → 값을 음수로 바꿔서 사용
    - https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99

- ads()
    - https://blockdmask.tistory.com/380

- sys.stdin.readline() : 반복문으로 입력 받기
    - 시간 초과 등의 문제 방지
    - https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

