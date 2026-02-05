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