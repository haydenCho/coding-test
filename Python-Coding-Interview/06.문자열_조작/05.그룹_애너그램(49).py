# 정렬하여 딕셔너리 추가
'''
- 반환하기 전에 딕셔너리의 값만 리스트로 변경하는 것도 잊지 말자(출력 형태 잘 확인한기)
- 기본 정렬 방법
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 딕셔너리 생성
        anagrams = collections.defaultdict(list)

        # 단어 정렬하여 딕셔너리에 추가
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        # 딕셔너리의 값을 리스트로 변환
        return list(anagrams.values())