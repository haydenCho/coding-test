import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)       # 기존의 리스트를 힙으로 생성
    
    while scoville[0] < K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + (min2 * 2)
        heapq.heappush(scoville, new)
        answer += 1
        
        # 만약 하나 남은 스코빌 지수가 K 미만이라면 조건 달성 불가
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer