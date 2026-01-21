# 리스트로 변환
'''
- 일반적인 스택 구조와 달리 파이썬의 리스트는 pop(0)과 pop()으로 값을 앞뒤로 반환할 수 있다.
- 리스트의 경우 동적 배열로 이루어져 있어 첫 번째 값을 꺼내오기 좋은 구조가 아니다.
    - 값을 꺼내면 모든 값이 한 칸씩 시프팅되어야 해서 시간 복잡도 O(n)이 발생
    -> 양방향 pop이 가능한 데크 자료구조로 수정하는 것이 좋다!

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 큐(리스트) 생성
        q: List = []

        # 예외 처리
        if not head:
            return True
        
        # 리스트 변환
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 확인
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True

# ======================================================
# 데크를 이용한 최적화
'''
- 실행 속도 감소(434ms -> 35ms)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 데크 생성
        q: Deque = collections.deque()

        # 예외 처리
        if not head:
            return True
        
        # 리스트 변환
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 확인
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True

# ======================================================
# 런너를 이용한 우아한 풀이
'''
- 두 칸씩 이동하는 fast runner와 한 칸씩 이동하는 slow runner를 이용한 풀이
    - 이동을 하는 거리가 2배이기 때문에 fast가 끝까지 이동했을 때, slow는 중간까지 이동한 상태이다.
    - fast가 끝까지 이동할 때까지 slow를 통해 역순 연결 리스트를 만든다.
    - 팰린드롬은 데칼코마니와 같기 때문에 역순 연결 리스트와 앞으로 slow가 이동할 값들은 같아야 한다.
    - 값을 비교하고 끝까지 이동에 성공했다면 성공(rev나 slow 모두 None이 나오기 때문에 not rev 혹은 not slow을 반환하면 된다.)
- 속도 자체는 데크 풀이와 비슷하지만 연결 리스트를 활용한다는 점에서 의의가 있다.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수 팰린드롬의 경우 slow를 한칸 넘겨야 함(가운데 제외)
        if fast:
            slow = slow.next
        
        # 팰린드롬 확인
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev