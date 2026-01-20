# 오름차순 풀이(내 풀이)
'''
- 두 개 숫자의 최솟값을 더하기 때문에 결국 오름차순을 한 상태에서 min값을 더하는게 가장 큰 수이다.
- 내림차순으로 해도 똑같은 결과가 나온다.

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums 정렬
        nums.sort()
        result = 0

        # min 합 구하기
        for i in range(len(nums)):
            if i % 2 == 0:
                result += min(nums[i], nums[i+1])
        
        return result

# ======================================================
# 짝수 번째 값 계산
'''
- 사실 이미 오름차순으로 정렬을 한 상태라면 굳이 min 값을 구할 필요 없이 짝수 번째 숫자를 더하면 된다.

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums 정렬
        nums.sort()
        result = 0

        # 짝수 번째 값으로 합 구하기
        for i in range(len(nums)):
            if i % 2 == 0:
                result += nums[i]
        
        return result

# ======================================================
# 파이썬다운 방식
'''
- sum()과 sorted(), 슬라이싱을 활용하여 한줄로 처리가 가능하다!

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums 정렬 + 슬라이싱으로 짝수 번째 값만 계산
        return sum(sorted(nums)[::2])