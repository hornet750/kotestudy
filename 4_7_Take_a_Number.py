# https://dmoj.ca/problem/ecoo13r1p1

# 엄청난 수요로 인해 지각 영수증 줄을 관리할 번호 받기 디스펜서를 설치
#
# 첫 번째 줄에는 정수 N 기계에서 나온 카운트 숫자
# 그 뒷 줄부터 명령어가 들어감 최대 백만 줄  -> 출석 데스크의 활동을 나타냄



next_number = input()
if not next_number.isdigit():
    exit("숫자로 입력되어야 합니다.")
next_number = int(next_number)
if not 0 <= next_number < 1000:
    exit("입력의 범위를 벗어남(0 <= N < 1000)")
# 지연 및 대기에 대한 변수 설정
num_late = 0
num_waiting = 0

done = False

while not done:
    line = input()
    line = line.upper()
    if not line.isalpha():
        exit("문자열로 입력되지 않음")
    next_number_length = len(line)
    if line.count('\n'):
        exit("입력에 개행표시가 있음")
    if line.count(' '):
        exit("입력에 공백이 있음")

    if line == 'EOF':
        done = True
    elif line == 'TAKE':
        num_late = num_late + 1
        num_waiting = num_waiting + 1
        next_number = next_number + 1
        if next_number == 1000:
            next_number = 1
    elif line == 'SERVE':
        num_waiting = num_waiting - 1
    elif line == 'CLOSE':
        print(num_late, num_waiting, next_number)
        num_late = 0
        num_waiting = 0
