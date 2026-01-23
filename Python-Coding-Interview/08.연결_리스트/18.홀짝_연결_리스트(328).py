# 반복 구조로 홀짝 노드 처리
'''
- 공간 복잡도와 시간 복잡도의 제약사항이 있다.
- 홀수는 홀수끼리 묶고 짝수는 짝수끼리 묶은 다음 홀수 마지막 노드의 next를 짝수 첫번째(even_head)로 연결하는 방식

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head