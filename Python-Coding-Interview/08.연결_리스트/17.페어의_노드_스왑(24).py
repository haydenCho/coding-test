# 값만 교환
'''
- 쉽게 풀기 위해 변칙적인 방식으로 풀이
- 코딩 테스트 자체에선 사용해도 괜찮지만 인터뷰나 추후 상세 평가에서는 감점일 수도 있음
    - 쉽게 풀기 위해 이렇게 푼 것이며, 연속 리스트 변경 과정을 알고 있다고 할 수 있어야 한다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        
        return head

# ======================================================
# 반복 구조로 스왑
'''
- 연결 리스트의 head를 가리키는 노드가 직접 바뀌는 풀이 → 기존 값을 root로 별도 설정해서 반환해야 한다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # b가 head를 가리키도록 변경
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        
        return root.next

# ======================================================
# 재귀 구조로 스왑
'''
- 포인터 역할을 하는 변수가 p 하나면 충분하고 더미 노드도 필요없어 공간 복잡도가 낮다.
- 다른 연결 리스트 문제들의 풀이와 마찬가지로 백트래킹되면서 연결 리스트 연결
- 그냥 외워야 할 듯... 그림으로 이해 필요

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head