# https://dmoj.ca/problem/coci18c3p1
#
# Magnus
#
# - HONI 라는 단어가 들어간 갯수를 출력하라
# - 1에서 100,000문자 길이
# - 입력은 대문자여야함. 소문자 및 숫자, 공백 불가
#
# 입력 : 영어 알파벳 대문자 100000 길이 이하인 1줄 짜리 입력
# 출력 : HONI 블록의 수 출력 
# 순차별로 HONI 가 나오는지를 카운트(숫자로), 중간에 어떤 글자가 나오던 패스

word = input()
word = word.upper() #소문자-> 대문자

if not word.isalpha():
    exit("문자열로 입력되지 않음")
word_length = len(word)
if word_length == 0 or word_length > 100000:
    exit("입력 범위를 벗어남(0 < n <= 100,000)")
if word.count('\n'):
    exit("입력에 개행표시가 있음")
if word.count(' '):
    exit("입력에 공백이 있음")

result = 0
match_pos = 0
match_char = 'HONI'

# for 문을 숫자(정수)로만 돌리는 것이 아니다!!! 문자로도 뺑뻉이!
# 원하는 문자와 매칭될 때마다
for index in word:
    match = match_char[match_pos] # 블럭값을 인덱스로 설정
    if match == index: # 입력값과 비교 맞으면 다음 문자로 넘어감
        match_pos = match_pos + 1
        if match_pos == 4:  # match_char 1블럭의 카운트가 다 참 만약 블럭의 단위가 4자가 아니라면 이 숫자도 바꿔줘야함
            match_pos = 0   # 카운트 리셋
            result = result + 1 # 최종 카운트에 1추가 - 1블럭을 찾음

print(result)
