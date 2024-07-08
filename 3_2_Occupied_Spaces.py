# https://dmoj.ca/problem/ccc18j2
#
# WEB
#
# 당신은 주차장 감독이다.
# 주차공간 N 
# 어제, 어느 주차 공간에 차가 주차되어 있고 어느 주차 공간이 비어 있는지 기록하였다. 
# 오늘도 기록 함
# 어제와 오늘 모두 주차 공간이 몇 개나 차지했는가?
#
# 입력 사항
# 첫 번째 입력은 총 주차 공간의 값 = N
# 1 <= N <= 100
# 두 번째 입력은 어제 주차 공간 정보 : 점유 공간 C, 빈 주차 . 으로 입력
# 세 번째 입력은 오늘 주차 공간 정보 : 점유 공간 C, 빈 주차 . 으로 입력
#
# 출력 사항
# 어제 and 오늘 이틀간 사용한 주차공간의 수를 출력하라.
# 어제 or 오늘 사용하지 않은 주차공간은 카운트 하지 않음

# 변수 설명 
# parking_space 주차 공간 수(정수)
# yesterday_use 어제 점유된 주차 공간
# today_use     오늘 점유된 주차 공간
# occupied      어제 오늘 이틀간 사용한 주차 공간의 수(정수)



parking_space = input()
if not parking_space.isdigit():
    exit("주차공간 수는 숫자로 입력되어야 합니다.")
parking_space = int(parking_space)
if not 0 <= parking_space <= 100:
    exit("주차공간 수의 범위를 벗어남(0 <= N <= 100)")

def check_input_use1(yesterday_use):
    allowed_chars = {'C', '.'}
    for char in yesterday_use:
        if char not in allowed_chars:
            return False
    return True

yesterday_use = input()
yesterday_use = yesterday_use.upper()
if not check_input_use1(yesterday_use):
    exit("입력한 문자열에 허용되지 않는 문자가 포함되어 있습니다.")
if not len(yesterday_use) == parking_space:
    exit(f"주차공간의 수만큼 주차기록을 입력해주어야 합니다. :  {parking_space}")

def check_input_use2(today_use):
    allowed_chars = {'C', '.'}
    for char in today_use:
        if char not in allowed_chars:
            return False
    return True

today_use = input()
today_use = today_use.upper()
if not check_input_use2(today_use):
    exit("입력한 문자열에 허용되지 않는 문자가 포함되어 있습니다.")
if not len(today_use) == parking_space:
    exit(f"주차공간의 수만큼 주차기록을 입력해주어야 합니다. :  {parking_space}")

occupied = 0
yesterday_occupied = 0
today_occupied = 0

for i in range(len(yesterday_use)):
    if yesterday_use[i] == 'C' and today_use[i] == 'C':
        occupied = occupied + 1
    elif yesterday_use[i] != 'C' and today_use[i] == 'C':
        yesterday_occupied = yesterday_occupied + 1
    elif yesterday_use[i] == 'C' and today_use[i] != 'C':
        today_occupied = today_occupied + 1
print(f"이틀간 사용한 총 주차공간은 : {occupied}")
print(f"어제 사용한 총 주차공간은 : {yesterday_occupied}")
print(f"오늘 사용한 총 주차공간은 : {today_occupied}")
