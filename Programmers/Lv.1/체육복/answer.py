def solution(n, lost, reserve):
    student = [1] * (n+2)
    for i in reserve:
        student[i] += 1
    for i in lost:
        student[i] -= 1

    for i in range(1, n+1):
        if student[i-1] == 0 and student[i] == 2:
            student[i-1:i+1] = [1, 1]
        elif student[i] == 2 and student[i+1] == 0:
            student[i:i+2] = [1, 1]

    answer = len([n for n in student[1:n+1] if n > 0])

    return answer