# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
'''
- 숫자 i에 대해서 구해야 하는 값은 i 이전의 값들의 곱 * 이후의 값들의 곱이다.
- 이전의 값들을 누적하여 곱한 값에 대해 인덱스를 1씩 증가하고, 이후의 값들을 역순으로 누적하여 곱한 값에 대해 인덱스를 1씩 감소한다.
- 위의 과정을 좀 정리하면 이전의 값들을 누적곱한 값에 이후의 값을 차례대로 곱한다.

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre = 1

        # 이전값 곱셈
        for i in range(len(nums)):
            result.append(pre)
            pre *= nums[i]
        
        pre = 1
        # 다음값 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            result[i] *= pre
            pre *= nums[i]
        
        return result