# 중앙을 중심으로 확장하는 풀이
'''
- 중앙을 찾기 위해 투 포인터(윈도우)를 사용한다.
- cddc와 같이 짝수 단위의 팰린드롬과 abcba와 같이 홀수 단위의 팰린드롬을 모두 찾아야 한다.
    → expand(i, i+1)와 expand(i, i+2)
- 예외는 길이가 1이거나 전체가 팰린드롬인 경우
- expand()는 투 포인터의 값이 유효하고, 같을 때(윈도우 크기가 2든 3이든 값이 같으면 팰린드롬) 범위를 확장한다.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # 예외 처리
        if len(s) < 2 or s == s[::-1]:
            return s
        
        # 슬라이딩 우측으로 이동하며 확인
        result = ''
        for i in range(len(s)-1):
            result = max(result,
                            expand(i, i+1),
                            expand(i, i+2),
                            key=len)
        
        return result