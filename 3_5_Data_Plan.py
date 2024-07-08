# https://dmoj.ca/problem/coci16c1p1
#
# Data Plan
# 한 달에 x MB 제공하는 데이터 요금제를 사용하고 있다.
# 특정 달에 사용하지 않은 데이터는 다음 달로 이월 된다.
#
# 입력 사항
# 1. 매월 주어지는 데이터량 x  1 <= x <= 100
# 2. 사용한 월 수 n  1 <= n <= 100
# 3. 사용한 데이터량을 월별로 한 줄 씩 입력 한다. 0 <= a <= 매월 사용가능한 데이터량 최대 100 * 100
#
# 출력 사항
# 다음 달 사용할 수 있는 사용량 출력

monthly_mb = input()
if not monthly_mb.isdigit():
    exit("월 데이터량은 숫자로 입력되어야 합니다.")
monthly_mb = int(monthly_mb)
if not 0 <= monthly_mb <= 100:
    exit("월 데이터량의 입력 범위를 벗어남(0 <= 데이터량 <= 100)")

months = input()
if not months.isdigit():
    exit("사용 월수는 숫자로 입력되어야 합니다.")
months = int(months)
if not 0 <= months <= 100:
    exit("사용 월 입력의 범위를 벗어남(0 <= 월 <= 100)")

total_mb = monthly_mb * (months + 1)
# for문 성공적으로돈 것을 확인하기 위한 비교 변수
round = 0 

for i in range(months):
    used = input()
    if not used.isdigit():
        print("숫자로 입력되어야 합니다.")
        break  # exit 명령어로 하지 않는 이유는 n번 입력 중간에 알려주기 위해서 break 문을 사용
    used = int(used)
    if used > total_mb:
        print("이번달 사용량을 초과하였습니다.")
        break
    total_mb = total_mb - used
    round = round + i
# break문으로 빠져나왔을 때는 아래 출력을 하지 않아야 함 -> 성공하였을 때만 출력
if round == months:
    print(f"다음달 사용가능용량 : {total_mb} mb")

