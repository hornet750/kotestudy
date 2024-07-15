# https://dmoj.ca/problem/ecoo15r1p1

# Smarties : 각자 색이 다른 초콜릿 캔디 m&m이랑 비슷함
#
# 먹는 순서를 정했다
# 색상순서 : 오렌지-파란색-초록색-노란색-분홍색-보라색-갈색-빨간색
# 한 번에 최대 7개 집을 수 있다
#
# 가끔 마지막 한 줌의 색상이 전 부 다 채워지지 않는 경우가 있다
#
# 색 분류를 마친 후 먹는 시간을 측정 하라
#
# 입력
# 10 테스트 케이스
# N (50 <= N <= 200)
# 각 줄은 단일 색상으로 입력
# 마지막 줄은 end of box로 출력
#
# 출력
# 전체 상자를 먹는데 걸리는 시간을 단일 행으로 출력

for dataset in range(10):
    num_orange = 0
    num_blue = 0
    num_green = 0
    num_yellow = 0
    num_pink = 0
    num_violet = 0
    num_brown = 0
    num_red = 0

    done = False

    while not done:
        line = input()
        if line == 'end of box':
            done = True
        elif line == 'orange':
            num_orange = num_orange + 1
        elif line == 'blue':
            num_blue = num_blue + 1
        elif line == 'green':
            num_green = num_green + 1
        elif line == 'yellow':
            num_yellow = num_yellow + 1
        elif line == 'pink':
            num_pink = num_pink + 1
        elif line == 'violet':
            num_violet = num_violet + 1
        elif line == 'brown':
            num_brown = num_brown + 1
        elif line == 'red':
            num_red = num_red + 1

    handfuls = ((num_orange + 6) // 7 + (num_blue + 6) // 7 +
                (num_green + 6) // 7 + (num_yellow + 6) // 7 +
                (num_pink + 6) // 7 + (num_violet + 6) // 7 +
                (num_brown + 6) // 7)

    print(handfuls * 13 + num_red * 16)


