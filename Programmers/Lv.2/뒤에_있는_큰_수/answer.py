def solution(numbers):
    num = len(numbers)
    answer = [-1] * num   # 뒤의 큰 수를 찾지 못한 경우를 위해 -1로 초기화
    stack = [0]           # 뒤의 큰 수를 찾지 못한 숫자의 인덱스
    
    for i in range(num):
      while stack and numbers[stack[-1]] < numbers[i]:
          answer[stack.pop()] = numbers[i]
      stack.append(i)
    
    return answer