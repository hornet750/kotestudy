# Boolean 표현식, if 문
#
# question ID : ccc15j1
# Special Day
# 올해 2월 18일은 CCC에 특별한 날이다.
# 사용자에게 숫자로 표현된 월과 일을 입력받고 해당 날짜가 2월 18일인지, 이전인지, 이후인지
# 판별하는 프로그램을 작성하시오.
#
# - 해당 날짜가 2월 18일 이전 이면 단어를 출력 Before
# - 해당 날짜가 2월 18일 이후 이면 단어를 출력 After
# - 해당 날짜가 2월 18일 이면 단어를 출력 Special
#
#
# 입력 사항
# 입력은 각각 별도의 줄에 있는 두 개의 정수로 구성 이 정수는 날짜를 나타낸다. 2015.
# 첫 번째 줄에는 월이 포함되며 이는 정수 범위이다. 1(1월), 12(12월)
# 두 번째 줄은 해당 월의 날짜가 포함되며 이는 정수 범위이다. 1에서 31 까지 해당 월의 날짜는
# 해당 월에 유효하다고 가정할 수 있다.
#
# 출력 사항
# Before, After, 또는 Special  한 줄에 인쇄
# 파이썬 입력 제한 사항 만드는 법 알고싶다!!

# 입력 제한 구문이 not working!!!!
mon_num = int(input())
if(mon_num > 12 and mon_num < 1):
    print('월의 입력을 1에서 12까지 입력하세요')
    print(exit())

day_num = int(input())
if(day_num > 31 and day_num < 1):
    print('일자의 입력을 1에서 31까지 입력하세요')
    print(exit())

mon_cal = mon_num * 100
day_cal = day_num
total = mon_cal + day_cal





if (total == 218):
    print('Special')
elif(total > 218):
    print('After')
elif(total < 218):
    print('Before')