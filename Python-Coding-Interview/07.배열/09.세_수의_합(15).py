# 브루트 포스로 계산(전체 순회)
'''
- 타임아웃 발생
- 앞 뒤로 같은 숫자가 있는 경우 쉽게 처리(건너뛰기)하기 위해 sort()로 정렬

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 리스트 정렬
        nums.sort()
        results = []

        # 순회하며 전부 더해보기
        for i in range(len(nums) - 2):
            # 중복 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        
        return results

# ======================================================
# 투 포인터로 합 계산
'''
- 리스트를 정렬하고 첫 번째 값(i)를 기준으로 하는 것은 이전 풀이와 동일
- 투 포인터를 이용하여 현재 합의 값에 따라 숫자를 키우거나 작게 하는 것을 피드백할 수 있다.
- 투 포인터는 문제 풀이에 자주 등장한다. 잘 알아두기!

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 리스트 정렬
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            # 중복 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 간격을 좁혀가며 합 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:     # 합이 0보다 작으면 숫자를 더 키워야 함(left를 오른쪽으로)
                    left += 1
                elif sum > 0:   # 합이 0보다 크면 숫자를 더 줄여야 함(right를 왼쪽으로)
                    right -= 1
                else:           # 정답 처리
                    results.append([nums[i], nums[left], nums[right]])

                    # 바로 옆에 같은 숫자가 있다면 스킵
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return results