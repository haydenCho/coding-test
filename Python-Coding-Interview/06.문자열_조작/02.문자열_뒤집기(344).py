# 투 포인터를 이용한 스왑(내 풀이)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1


# ====================================================
# 투 포인터를 이용한 스왑(좀 더 간단한 코드)
'''
이렇게만 수정해도 시간이 많이 단축된다(6ms -> 2ms)
변수에 값을 저장하는 과정도 시간이 든다는 걸 명심하기

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# ====================================================
# 파이썬다운 풀이(파이썬의 기본 기능 활용)
'''
reverse(): 리스트에만 제공

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()