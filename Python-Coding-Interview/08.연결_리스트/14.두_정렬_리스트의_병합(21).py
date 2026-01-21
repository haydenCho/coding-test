# 재귀 구조로 연결
'''
- 215p의 그림을 보며 이해하기
- list1을 계속 이동하며 list2의 값과 비교하여 list1이 가리키는 노드를 list2와 변경한다.
    - 노드를 변경하면 다음 값(list1.next)가 기존의 list2.next로 변경된다.
    - 연결 리스트가 정렬된 상태이기 때문에 list1과 list2 모두 다음값이 큰 값이다.
    - 계속해서 값을 비교하여 노드를 연결하다보면 리스트 병합이 완료된다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1