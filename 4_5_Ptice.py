# https://dmoj.ca/problem/coci08c1p2

# Ptice : 쁘띠쩨는 아름다운 노래를 부르는 새들 이라는 의미.
#         유고슬라비아 전통 민속음악을 배우는 학회
#
# 모든 지원자 Adrian, Bruno, Goran 모두 합격을 해야 할 수 있음
# 질문에 대한 답변은 3지 선다 A, B, C 이다
# 불행히도, 찍어야 한다. 세 소년은 어떤 답이 유용할지 이론을 가지고 있다
#
# adrian은 ABC
# Bruno 는 BABC
# Goran은 CCAABB
# 시험의 정답이 주어졌을 때, 세 명중 누가 제일 옳았는지 판별하는 프로그램을 작성
#
# 입력 사항
# 1번 줄 : 시험 문제 수 (1 <= N =< 100 )
# 2번 줄 : 정답 문자 열 (A,B,C) 중 1개가 이것도 100개가 한계
#
# 출력 사항
# M 세 소년 중 한 명이 맞힌 가장 많은 정답 수,
# 그 후 맞춘 순서대로 이름을 출력함

# 아이들의 각자 패턴을 정의
ADRIAN = 'ABC'
BRUNO = 'BABC'
GORAN = 'CCAABB'


n = input()
if not n.isdigit():
    exit("문제수는 숫자로 입력되어야 합니다.")
n = int(n)
if not 0 <= n <= 100:
    exit("문제 수의 범위를 벗어남(0 <= N <= 100)")
answer = input()
answer = answer.upper()
if not answer.isalpha():
    exit("문자열로 입력되지 않음")
answer_length = len(answer)
if not answer_length == n:
    exit("입력 범위를 벗어남 질문갯수 n 과 동일한 개수를 입력하시오")
if answer.count('\n'):
    exit("입력에 개행표시가 있음")
if answer.count(' '):
    exit("입력에 공백이 있음")
if answer.count("A") + answer.count("B") + answer.count("C") != len(answer):
    exit("입력은 A, B, C 만 가능합니다")

# 아이들 각자의 정답인 수를 담을 변수
adrian_count = 0
bruno_count = 0
goran_count = 0
# 정답을 각자의 답변과 맞는지 확 하나씩 확인
for i in range(len(answer)):
    if answer[i] == ADRIAN[i % len(ADRIAN)]:
        adrian_count = adrian_count + 1
    if answer[i] == BRUNO[i % len(BRUNO)]:
        bruno_count = bruno_count + 1
    if answer[i] == GORAN[i % len(GORAN)]:
        goran_count = goran_count + 1
# 누가 제일 많이 맞추었는지 조건 분기 - 세명이 돌아가면서 맞힌 카운트만 체크하면 됨
most = adrian_count
if bruno_count > most:
    most = bruno_count
if goran_count > most:
    most = goran_count

print(most)
# 정답인 수가 동률이면 출력
if adrian_count == most:
    print('Adrian')
if bruno_count == most:
    print('Bruno')
if goran_count == most:
    print('Goran')

