## 문제
상근이는 생명과학 연구소에서 염색체가 특정한 패턴인지를 확인하는 일을 하고 있다. 염색체는 알파벳 대문자 (A, B, C, ..., Z)로만 이루어진 문자열이다. 상근이는 각 염색체가 다음과 같은 규칙을 만족하는지 검사해야 한다.

문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
그 다음에는 A가 하나 또는 그 이상 있어야 한다.
그 다음에는 F가 하나 또는 그 이상 있어야 한다.
그 다음에는 C가 하나 또는 그 이상 있어야 한다.
그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
문자열이 주어졌을 때, 위의 규칙을 만족하는지 구하는 프로그램을 작성하시오.

<br/>

## 입력
첫째 줄에 테스트 케이스의 개수 T ≤ 20 이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 최대 200개의 알파벳 대문자로 이루어진 문자열이 주어진다.

<br/>

## 출력
각 테스트 케이스에 대해서, 문제의 규칙을 지키는 문자열인 경우에는  "Infected!"를, 아닌 경우에는 "Good"을 출력한다.

<br/>

## 예제 입력 1
15
AFC
AAFC
AAAFFCC
AAFCC
BAFC
QWEDFGHJMNB
DFAFCB
ABCDEFC
DADC
SDFGHJKLQWERTYU
AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFC
AAAFFFFFBBBBCCCAAAFFFF
ABCDEFAAAFFFCCCABCDEF
AFCP
AAFFCPP

<br/>

## 예제 출력 1
Infected!
Infected!
Infected!
Infected!
Infected!
Good
Good
Good
Good
Good
Good
Good
Good
Good
Good

<br/>

## 🤔
- [정규식(위키독스)](https://wikidocs.net/4308)
- **정규표현식 패턴 정의**
    - ^[A-F]? : 시작은 A-F 중 0개 또는 1개
        - ^: 문자열의 맨 처음과 일치한다는 것을 의미
        - {m}, {n, m}: 앞의 문자를 m번 혹은 n~m번 반복(a{3}: a를 3번 반복)
        - ?: {0, 1}과 같은 의미.
    - A+ : 그 다음 A가 1개 이상
    - F+ : 그 다음 F가 1개 이상
    - C+ : 그 다음 C가 1개 이상
    - [A-F]?$ : 마지막은 A-F 중 0개 또는 1개로 끝남
        - $: 문자열의 끝과 매치한다는 것을 의미
- **정규표현식 메서드**
    - match: 문자열의 처음부터 정규식과 매치되는지 조사
    - search: match와 같은 기능. match가 처음부터 정규식에 매치되는지 확인한다면, search는 해당 문자열 전체에 매치되는 부분이 있는지 검색
    - findall: 매치되는 모든 모든 값을 찾아 리스트로 반환
    - finditer: findall과 동일하지만 반복 가능한 객체(iterator object)를 반환한다는 차이점이 있다.

**👉🏻 정규식을 쓰면 짧고 간결한 코드로 작성할 수 있는 문제. 자주 쓸만한 정규식 패턴과 메소드는 알아두자!**