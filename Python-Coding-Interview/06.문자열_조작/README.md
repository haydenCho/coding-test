## 문자열 조작
### 문자열 관련 파이썬 메서드
- upper(): 문자열을 대문자로 변환
- lower(): 문자열을 소문자로 변환
- isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있으면 True, 아니면 False를 반환
- isalpha(): 문자열이 알파벳으로만 구성되어 있으면 True, 아니면 False를 반환
- isdecimal(): 문자열이 정수이면 True, 아니면 False를 반환
- isdigit(): 문자열이 숫자이면 True, 아니면 False를 반환
- isspace(): 문자열이 공백으로만 구성되어 있으면 True, 아니면 False를 반환
- split(): 문자열을 특정 구분자(공백, 쉼표 등)를 기준으로 분리하여 리스트로 반환

<br/>

### 정규식
- 문자열 전처리 등을 위해 사용하면 유용하다.(많이 쓰는 기호들은 꼭 알아둘 것!)
- row string을 의미하는 r을 항상 쓰는 것이 좋다!(백슬래시(\)를 파이썬이 먼저 해석하지 않게 막아줌)
- [위키독스](https://wikidocs.net/4308)
- [참고 블로그](https://velog.io/@euisuk-chung/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-%ED%99%9C%EC%9A%A9-%EB%B0%A9%EB%B2%95)
- 예시 1: '[^a-z0-9]' → 소문자 알파벳(a–z) 또는 숫자(0–9)가 아닌 문자 1개
    - [ ... ] : 문자 클래스(대괄호 안에 있는 문자 중 하나와 매칭)
    - [^...] → …가 아닌 것
    - re.sub('[^a-z0-9]', '', s): 소문자와 숫자가 아닌 문자를 제거(''로 변경)
- 예시 2: r'[^\w]' → 문자/숫자/언더스코어가 아닌 모든 것
    - \w : 문자 + 숫자 + _
    - re.sub(r'[^\w]', ' ', paragraph): 문장부호(! ? , .)를 공백으로 치환

### re.sub()
- re.sub(pattern, replacement, string)
    - 첫 번째 인자(pattern): 찾을 정규식 패턴
    - 두 번째 인자(replacement): 바꿀 문자열
    - 세 번째 인자(string): 대상 문자열

<br/>

### In-place Algorithm(제자리 알고리즘)
: 입력 크기에 비례하는 추가 공간을 필요로 하지 않고 입력 데이터 구조 에 직접 연산을 수행하는 알고리즘
- 데이터 구조의 별도 복사본을 생성하지 않고 입력 데이터를 제자리에서 수정
- [위키](https://en.wikipedia.org/wiki/In-place_algorithm)

<br/>

### 파이썬 기본 기능
- reverse(): 리스트 제공 기능, 리스트의 값을 반대로 뒤집는다.

<br/>

### sort()와 람다식
- [sort(): 위키독스](https://wikidocs.net/233746)
- [람다식: 위키독스](https://wikidocs.net/64)
- sort()는 기본적으로 오름차순 정렬이며, 내림차순 정렬을 위해선 reverse 매개변수값을 True로 하면 된다.
- 정렬 기준을 지정하기 위해 **key 매개변수와 함께 lambda 함수를 사용**하기도 한다.

#### sorted()
- 기본적으로 sort()와 동일하게 동작하지만 원본 리스트를 변경하지 않는다.
- 원본 리스트 변경 여부가 다르기 때문에 사용방식도 다르니 유의.
- sort(): `people.sort(key=lambda x: x['age'])`
- sorted(): `sorted_people = sorted(people, key=lambda x: x['age'])`

<br/>

#### join()
- [Docs](https://www.w3schools.com/python/ref_string_join.asp)
- 예제 1: `",".join(elements)` → "Fire,Air,Water"
- 예제 2: `"".join(elements)` → "FireAirWater"

<br/>

### 리스트 컴프리헨션
- 직관적으로 리스트를 생성하는 방법
- 컴프리헨션(Comprehension): 파이썬의 자료구조(list, dictionary, set)에 데이터를 좀 더 쉽고 간결하게 담기 위한 문법
- 대괄호 "[", "]"로 감싸고 내부에 for문과 if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성한다.
    - in, not in 등의 조건도 사용할 수 있다.
- [위키독스](https://wikidocs.net/22805)
- [참고](https://bio-info.tistory.com/28#google_vignette)

<br/>

### collections 모듈
- [collections](https://docs.python.org/ko/3/library/collections.html): 파이썬의 내장모듈
- [deque()](https://docs.python.org/ko/3/library/collections.html#collections.deque): 데크 자료형
- [defaultdict()](https://docs.python.org/ko/3/library/collections.html#collections.defaultdict): 키값이 없을 경우 미리 설정해놓은 초기값(default)을 반환하는 딕셔너리 생성
    - (공식 문서)누락된 값을 제공하기 위해 팩토리 함수를 호출하는 딕셔너리 서브 클래스
    - **초기값을 위해 인수를 제공**해야 한다. e.g. counts = collections.defaultdict(int) -> 0이 기본값
    - [사용 예제 참고](https://leapcell.io/blog/ko/understanding-defaultdict-in-python)
- [Counter()](https://docs.python.org/ko/3/library/collections.html#collections.Counter): 객체를 세는 데 사용하는 딕셔너리 서브 클래스

#### Deque(데크) 자료형
- collections 모듈에 포함된 자료형
- popleft() 기능 제공
    - pop(0)이 O(n)의 속도인 반면 popleft()는 O(1)의 속도
- [참고 블로그](https://siloam72761.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EB%8D%B0%ED%81%ACdeque%EC%97%90-%EB%8C%80%ED%95%9C-%EB%AA%A8%EB%93%A0-%EA%B2%83-%EC%A0%95%EC%9D%98-%ED%95%A8%EC%88%98-%ED%99%9C%EC%9A%A9)