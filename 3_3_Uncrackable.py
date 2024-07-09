# https://dmoj.ca/problem/wc17c3j3
#
# Uncrackable
#
# 당신은 웹사이트에 계정을 등록하려함
# 이미 사용자 이름을 선택하고, 비밀번호를 만들어야 한다.
# - 비밀번호 문자열
# - 8에서 12문자 길이
# - 각 문자는 소문자, 대문자, 숫자 가 있어야 한다.
# - 소문자 3개 이상, 대문자 2개 이상, 숫자 1개 이상 포함 해야한다.
#
# 입력 : 한 줄 입력
# 출력 : 조건에 맞으면 valid, 맞지 않으면 Invalid 출력

# upper() 문자열을 대문자로 변경, lower() 문자열을 소문자로 변경
# isupper() 문자열이 대문자인지 확인, islower() 문자열이 소문자인지 확인, isdigit() 숫자인지 확인

# 먼저 INPUT을 정의하려니 계속 패스하지 못해서 아래 IF 문에 합침
#if not 8 <= len(password) <= 12:
#    exit("Invalid")
# 변수 정의 소문자 lower, 대문자 upper 숫자 digit

password = input()

# 카운트 변수들 초기화
lower_input = 0
upper_input = 0
digit_input = 0

for char in password:
    if char.islower():
        lower_input = lower_input + 1
    elif char.isupper():
        upper_input = upper_input + 1
    elif char.isdigit():
        digit_input = digit_input + 1
# 입력에 소문자 3, 대문자 2, 숫자 1개 이상 AND 입력 길이가 8 이상 12이하 검사
if (lower_input >= 3 and upper_input >= 2 and digit_input >= 1) and (len(password) >= 8) and (len(password) <= 12):
    print('Valid')
else:
    print('Invalid')
