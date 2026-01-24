# 스택 일치 여부 판별
'''
- 괄호는 가장 나중에 열린 괄호가 가장 먼저 닫혀야 한다. = 스택(LIFO) 개념
- 매핑 테이블 table: 닫는 괄호를 키(Key)로, 여는 괄호를 값(Value)으로 설정
    - 닫는 괄호가 나왔을 때 스택에서 꺼낸 값과 비교
- char not in table -> table에 해당하는 값(키)가 없다 = 여는 괄호라는 의미
- 일치 여부 판별
    - not stack: 스택이 비어있는데 닫는 괄호가 나온 경우 → False
    - table[char] != stack.pop(): 스택에서 가장 최근에 넣은 여는 괄호를 꺼냈는데, 현재 닫는 괄호와 짝이 맞지 않는 경우 → False

'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
            
        return len(stack) == 0