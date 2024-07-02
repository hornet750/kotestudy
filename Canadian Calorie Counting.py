# 조건부 실행, Boolean 타입, 관계 연산자 IF 문
#
# question ID : ccc06j1
#
# 캐나다 칼로리 계산
# 메뉴
# 버거     1. 치즈버거(461kcal) 2.피쉬버거(431kcal) 3.채식버거(420kcal) 4.버거 없음
# 사이드   1. 감자튀김(100kcal) 2.구운감자(57kcal) 3.샐러드(70kcal) 4. 사이드 주문 없음
# 음료     1. 청량음료(130kcal) 2. 오렌지주스(160kcal) 3. 우유(118kcal) 4. 음료 없음
# 디저트   1. 사과파이(167kcal) 2. 순대(266kcal) 3. 과일컵(75kcal) 4. 디저트 없음
# 한 끼의 총 칼로리를 계산하는 프로그램을 작성하시오.
# 상세 입력 사항
#
# 프로그램은 각 항목 유형에 대한 숫자를 입력한 다음 총 칼로리를 계산하고 표시해야 한다.
# 첫 번재 줄은 고객이 선택한 버거, 두 번째 줄은 사이드,
# 각 입력은 1부터 4까지의 숫자.
#
# 상세 출력 사항
#
# 선택된 식사의 총 칼로리를 출력하고 출력 이후 실행을 멈춤

burger_input = int(input())
side_input = int(input())
drink_input = int(input())
desert_input = int(input())
calories = 0

if burger_input == 1:
    calories = calories + 461
elif burger_input == 2:
    calories = calories + 431
elif burger_input == 3:
    calories = calories + 420
elif burger_input == 4:
    calories = calories
else: print(f'버거 선택의 범위가 넘었습니다.')
#여기서 프로그램이 종료되는 명령어가 있으면 좋겠다.

if side_input == 1:
    calories = calories + 100
elif side_input == 2:
    calories = calories + 57
elif side_input == 3:
    calories = calories + 70
elif side_input == 4:
    calories = calories
else: print(f'사이드 선택의 범위가 넘었습니다.')

if drink_input == 1:
    calories = calories + 130
elif drink_input == 2:
    calories = calories + 160
elif drink_input == 3:
    calories = calories + 118
elif drink_input == 4:
    calories = calories
else: print(f'음료 선택의 범위가 넘었습니다.')

if desert_input == 1:
    calories = calories + 167
elif desert_input == 2:
    calories = calories + 266
elif desert_input == 3:
    calories = calories + 75
elif desert_input == 4:
    calories = calories
else: print(f'디저트 선택의 범위가 넘었습니다.')

print(f'Your total Calorie count is {calories}.')
