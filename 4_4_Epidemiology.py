# https://dmoj.ca/problem/ccc20j2

# Epidemiology
#
# 질병의 확산을 분석하기 위해 모델을 사용한다.
#
# 1. 사람이 질병에 걸리면 100% 감염
# 2. 바로 다음 날에 감염
# 3. 1 번 이상 감염 안됨
# 4. 총 감염자 수가 1 번 이상인 경우
# 5. P 질병을 앓은 사람의 수
#
# 입력 사항
# 3줄 (정수)
# 첫 번째 : P 는 10,000,000 천만 보다 작은 정수. 질병을 앓은 사람의 총 수 (기준점)
# 두 번째 : N 오늘 질병을 앓고 있는 사람의 수 - 이 사람들이 R의 배수로 감염시킨다.
# 세 번째 : R 감염된 사람의 수
#
# 출력 사항
# 질병을 앓은 사람의 총 수가 감염된 사람보다 많아진 첫 날의 데이 카운트를 하시오
# 무언가 조치를 취해야하는 기준점. 혹은 목표
threshold_for_new_measures = int(input())
# 지금 질병을 앓고 있는 사람
current_infected_count = int(input())
# 확산 속도 = 매일 늘어나는 감염자의 수 (속도 기울기)
daily_new_infections = int(input())
#감염 이후 지나가는 날짜 day = 결과값이기도 함 이 날짜 이후에 기준점 이상의 감염자가 생김
day = 0
# 내일 감염자를 계산하기 위한 변수(어제 감염자수)-실제로는 상수 (두 번째 입력값)
prev_day = current_infected_count


# 매일 N + R*날짜 를 계산하고 값이 기준점 P를 넘었을 때의 날짜를 출력한다.
while current_infected_count <= threshold_for_new_measures:
    current_infected_count = current_infected_count + prev_day * daily_new_infections
    prev_day = prev_day * daily_new_infections
    day = day + 1
    print(f"당국은 이번 전염병에 대해 {threshold_for_new_measures}명을 기준으로 A조치 할 예정이며, 발생 {day}일차 날 발생한 감염자수는 {current_infected_count}명입니다")

print(day)
