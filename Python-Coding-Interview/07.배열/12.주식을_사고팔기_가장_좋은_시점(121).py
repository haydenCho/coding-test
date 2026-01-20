# 저점과 현재 값과의 차이 계산(내 풀이)
'''
- 순회하며 최소값을 설정하고 최소값과 현재값의 차이를 구하여 가장 큰 값을 반환한다.
- 최소값 이전의 값들을 의미 없으므로 순서대로 계산하면 된다.

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = sys.maxsize

        for price in prices:
            # 최솟값 설정
            if price < min_price:
                min_price = price

            # 최솟값과 현재값 차이 구하기
            if result < price - min_price:
                result = price - min_price
        
        return result

# ======================================================
# 저점과 현재 값과의 차이 계산(코드 정리)
'''
- min()과 max()를 사용하면 여러값들 중 최소값, 최대값을 활용해야 할 때 쉽게 처리할 수 있다!
- 의외로 실행 시간은 더 걸리는 듯 하다.(큰 차이는 X)

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = sys.maxsize

        for price in prices:
            # 최솟값 설정
            min_price = min(min_price, price)

            # 최솟값과 현재값 차이 구하기
            result = max(result, price - min_price)
        
        return result