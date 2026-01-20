# 투 포인터를 최대로 이동
'''
- 양끝에서 시작하여 점점 높은 막대를 향해 포인터를 이동
- 이동하는 과정에서 현재 최고 높이와 현재 높이가 정해지는데, 
  이 막대들의 높이 차이가 쌓이는 빗물의 양이다.
- 왼쪽과 오른쪽의 최고 높이를 비교해서 더 높은 쪽으로 포인터를 이동(왼쪽이 높으면 오른쪽 포인터를 이동)하므로 
  결과적으로 가장 높은 막대에서 양 포인터가 만나게 된다.

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # 예외
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # 더 높은 쪽으로 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

# ======================================================
# 스택 쌓기
'''
- 스택에 인덱스를 쌓아가다가 변곡점(이전 높이보다 높은 높이)을 만났을 때 이전 값들을 꺼내 차이만큼 물 높이를 쌓는다.

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            
            stack.append(i)
        return volume