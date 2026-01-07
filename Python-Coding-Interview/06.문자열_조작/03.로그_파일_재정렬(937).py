# 람다식과 + 연산자 사용
'''
람다식 작성법도 알아야 하지만 기본적으로 sort() 기능에 대해서도 알아야 함
sort()는 오름차순, 내림차순 외에 key로 원하는 기준을 설정할 수 있다.
이 기준을 설정할 때 람다식을 많이 사용한다. 잘 알아두자.

'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        # 숫자 로그와 문자 로그 분리
        for i in range(len(logs)):
            if logs[i].split()[1].isdigit():
                digits.append(logs[i])
            else:
                letters.append(logs[i])
        
        # 문자 로그 정렬
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        ''' 정렬 기준
            1. x.split()[1:] → 본문
            2. x.split()[0] → 식별자(본문이 같으면 식별자로 구분)
        '''

        return letters + digits

# ====================================================
# 반복문 단순화(리스트에서는 바로 값을 꺼내 쓰자...)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        # 숫자 로그와 문자 로그 분리
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # 문자 로그 정렬
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))

        return letters + digits