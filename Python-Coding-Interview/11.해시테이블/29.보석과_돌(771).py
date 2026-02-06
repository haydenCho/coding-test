# 해시 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # 돌(S)의 빈도 수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        # 보석(J)의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

# ==================================================
# defaultdict를 이용한 비교 전략
'''
- 실행속도는 비슷하고 코드 길이는 많이 줄었음

'''
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # 돌(S)의 빈도 수 계산
        for char in stones:
            freqs[char] += 1
        
        # 보석(J)의 빈도 수 합산
        for char in jewels:
            count += freqs[char]

        return count

# ==================================================
# Counter로 계산 생략
'''
- Counter를 사용하면 개수를 계산하는 과정을 자동으로 처리할 수 있다.
- 빈도 수와 관련된 문제가 나온다면 Counter를 생각하기

'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)     # 돌(sttones)의 빈도 수 계산
        count = 0

        # 비교 없이 보석(J)의 빈도 수 합산
        for char in jewels:
            count += freqs[char]

        return count