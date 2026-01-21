# 재귀 구조로 뒤집기
'''
- next는 현재 노드의 다음 연결리스트(남은 기존 연결 리스트)
- node.next는 역순 리스트 방향(변경된 역순 연결 리스트)
- prev가 역순 연결 리스트의 앞 방향이고, next가 남은 연결 리스트라고 생각하면 된다.
    - 1) pre(None) / 1 → 2 → 3 → 4 → 5
    - 2) pre(None) ← 1 / 2 → 3 → 4 → 5
    - 3) pre(None) ← 1 ← 2 / 3 → 4 → 5
    - 4) pre(None) ← 1 ← 2 ← 3 / 4 → 5
    - 5) pre(None) ← 1 ← 2 ← 3 ← 4 / 5
    - 6) pre(None) ← 1 ← 2 ← 3 ← 4 ← 5
- 유형 자체를 알아두는 편이 좋겠다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 재귀함수
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            # next는 현재 노드의 다음 연결리스트(남은 기존 연결 리스트)
            # node.next는 역순 리스트 방향(변경된 역순 연결 리스트)
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)

# ======================================================
# 반복 구조로 뒤집기
'''
반복 구조로 뒤집기
- node는 next를 이용하여 다음 노드로 이동
- 기존의 node는 prev를 이용하여 역순으로 연결
- 실행 속도나 공간 복잡도가 재귀 방식보다 미세하지만 더 좋은 편이다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        # node는 next를 이용하여 다음 노드로 이동
        # 기존의 node는 prev를 이용하여 역순으로 연결
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev