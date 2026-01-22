# 자료형 반환
'''
- 역순 연결 리스트를 리스트로 변환하고 리스트 값들을 문자열 합 -> 숫자로 변환하여 연산
- 연산 후 다시 한글자씩 역순 리스트로 저장
- 긴 코드 길이와 달리 실제 실행 속도는 괜찮지만 이 문제는 이 방식으로 풀이할 문제가 아니다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node:ListNode) -> List:
        li: List = []
        while node:
            li.append(node.val)
            node = node.next
        return li

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(int(r))
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 반환
        return self.toReversedLinkedList(str(resultStr))

# ======================================================
# 전가산기 구현
'''
- 실제 전가산기 구현X → 전가산기의 개념을 이용한 풀이
- 두 개의 입력값과 이전 자리수에서 나온 올림수를 더하고 해당 값을 다시 현재 값과 자리 올림수로 나눈다.
- 각각의 연결 리스트의 값을 더한 결과 sum을 나눈 몫은 자리 올림수가 되고, 나머지는 현재 자리의 값이 된다.
- divmod() 함수를 잘 알아두자.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            # 두 입력값의 합
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next