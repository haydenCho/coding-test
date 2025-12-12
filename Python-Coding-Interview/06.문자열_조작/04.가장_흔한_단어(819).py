# 리스트 컴프리헨션, defaultdict() 사용
'''
collections 모듈의 defaultdict(딕셔너리) 사용
최대값을 반환하는 과정을 파이썬 내장 라이브러리에서는 제공하지 않는다.
-> Counter() 클래스를 사용하면 더 깔끔하게 사용 가능

'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        
        return max(counts, key=counts.get)

# ====================================================
# Counter 클래스 사용
'''
most_common(): 빈도수가 가장 높은 상위 n개의 요소와 그 개수(튜플 형태)를 내림차순으로 반환
e.g. most_common(1): 가장 흔한 단어 1개 반환 / most_common(2): 가장 흔한 단어 2개 반환

'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]