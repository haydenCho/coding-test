# 첫 번째 수를 뺀 결과를 in으로 조회(내 풀이)
'''
- in을 사용하면 빠른 속도로 값의 존재 유무를 확인할 수 있다.
- 슬라이싱을 하면 인덱스도 줄어들기 때문에 값을 반환할 때 값을 더해주어야 한다.

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 순회하며 타겟에서 해당 값을 뺀 값이 존재하는지 확인
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target - nums[i])+(i+1)]

# 코드 정리
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 순회하며 타겟에서 해당 값을 뺀 값이 존재하는지 확인
        for i, n in enumerate(nums):
            complement = target - n
        
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i + 1)]

# ======================================================
# 첫 번째 수를 뺀 결과 키 조회
'''
- 딕셔너리를 활용한 조회
- 인덱스와 값을 반대로 딕셔너리에 저장(인덱스 - 값, 값 - 키)

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and nums_map[target-num] != i:
                return [i, nums_map[target-num]]

# 하나의 for문으로 통합
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target-num]]
            nums_map[num] = i
