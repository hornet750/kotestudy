# Boolean 표현식, if 문
#
# question ID : dmopc16c1p0
# C.C. and Cheese-kun
# CC는 absolutely 자신이 받은 피자의 너비가 다음과 같으면 만족. 3너비, 최소 치즈95% 이상
# CC는 fairly 자신이 받은 피자 너비가 다음과 같은면 만족 1단위와 최대 여분 치즈 50%
# very  CC는 다른 피자를 받아도 만족
#
# 입력 사항
# 첫 번째 줄에는 단일 정수 W(1 <= W <= 3) 피자의 너비
# 두 번째 줄은 정수 C(0 <= C <= 100) 피자전체에 치즈가 차지하는 비율
#
# 출력 사항
# 만족 ->  C.C. is M satisfied with her pizza. 출력
# 만족도 출력 : absolutely, fairly, very
# 경계 나누기 elif 로 경계를 구분 - 큰 경계부터 먼저 판단한다. 작은 것부터 하면 앞에서 걸린다.
# 잘못된 코드 
#if (w >= 1 or w < 3) and (c >= 50 or c < 95):
#   M = ('fairly')
#elif w >= 3 and c >= 95:
#    M = ('absolutely')
#else:
#    M = ('very')

w = int(input())
c = int(input())

if w == 3 and c >= 95:
    M = ('absolutely')
elif w == 1 and c <= 50:
    M = ('fairly')
else:
    M = ('very')
print('C.C. is',M,'satisfied with her pizza.')