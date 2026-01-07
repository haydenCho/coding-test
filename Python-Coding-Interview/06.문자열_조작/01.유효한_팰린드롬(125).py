# 리스트로 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        # 리스트에 소문자 담기
        for i in s:
            if i.isalnum():
                strs.append(i.lower())

        # 팰린드롬 확인
        while(len(strs) > 1):
            left = strs.pop(0)
            right = strs.pop()
            if(left!=right):
                return False
        
        return True
        
# ======================================================
# 데크로 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 데크 자료형으로 생성
        strs: Deque = collections.deque()

        # 리스트에 소문자 담기
        for i in s:
            if i.isalnum():
                strs.append(i.lower())

        # 팰린드롬 확인
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True

# ======================================================
# 슬라이싱으로 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]     # 슬라이싱