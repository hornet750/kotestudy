# https://dmoj.ca/problem/coci08c3p2
#
# 과제 반복 횟수와 각 반복에서 수행해야 할 작업은 문자열에서 모음이 있는 위치마다 다르다
# 비밀 문장을 쓴다.
# 다른 사람이 읽을 수 없도록 원래의 문장을 쓰는 대신 어떤 인코딩을 한다
# 문장의 각 모음(a,e, i, o, u) 뒤에 문자 p와 해당 모음을 다시 추가한다
# I like you -> ipi likikepe yopoupu
#
# 입력
# 한 줄의 텍스트 소문자와 공백으로 이루어짐
# 각 단어 사이에 정확히 하나의 공백이 있음
# 최대 길이는 100자
#
# 입력 체크
# 0. 인코딩(비밀 문장)인 문장이 입력됨
# 1 대문자가 입력되었을 때 소문자로 변경
# 2. 공백이 하나 이상 있을 때 공백을 하나로 줄여줌
# 3. 최대 길이 넘지 않도록 알림(100자)
#
# 출력
# 디코딩 된 원래 문장을 출력(비밀문 해석)

sentence = input()

result = ''
i = 0

while i < len(sentence):
    result = result + sentence[i]
    if sentence[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1

print(result)
