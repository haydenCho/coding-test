# 재귀를 이용한 분리
'''
- 어려운 문제
- 스택 이용 풀이보다 우아한 코드

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

# ====================================================
# 스택을 이용한 문자 제거
'''
- 재귀 이용 풀이보다 시간이 적게 걸린다.
- 사실상 리스트 풀이 방식
    - 스택에 없는 기능인 검색 기능을 활용(그래도 최대한 정석 스택 방식으로 풀이)

'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)