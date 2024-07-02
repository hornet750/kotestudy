# Boolean 표현식
#
# question ID : ccc18j1
# Telemarketer or not?
# 텔레마케터들이 마지막 네 자리가 세 가지 속성을 갖는 일곱 자리 전화번호를 사용한다는 것을 알아챘다.
# 마지막 네 자리만 보면, 이러한 속성은 다음과 같다.
#
# - 이 네 자리 숫자 중 첫 번째 숫자는 8 또는 9
# - 마지막 숫자는 8 또는 9
# - 두 번째와 세 번째 숫자는 같다.
#
#  예를 들어, 전화번호 마지막 네 자리가 8229, 8338, 또는 9008이면 이는 텔레마케터 번호이다.
# 마지막 네 자리를 기준으로 전화번호가 텔레마케터 번호인지 아닌지 판단하는 프로그램을 작성하라.
# 번호가 텔레마케터 번호가 아니면 전화를 받고, 그렇지 않으면 무시해아한다.
#
#
# 입력 사항
# 4각 줄이 범위 내에서 정확히 하나의 숫자를 포함하는 줄 0~9까지
#
# 출력 사항
# 텔레마케터 번호 패턴과 일치하면 ignore 출력하고, 그렇지 않으면 answer 출력

phone_num1 = int(input())
phone_num2 = int(input())
phone_num3 = int(input())
phone_num4 = int(input())

# telemarketer 번호 : 첫 번째 자리는 8 또는 9, 네 번째 자리는 8 또는 9,
# 두 번째 자리와 세 번째 자리의 수는 같다.

if ((phone_num1 == 8 or phone_num1 == 9) and
        (phone_num4 == 8 or phone_num4 == 9) and
        (phone_num2 == phone_num3)):
    print('ignore')
else:
    print('answer')