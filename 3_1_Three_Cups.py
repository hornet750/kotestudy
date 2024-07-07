# https://dmoj.ca/problem/coci06c5p1
#
# WEB
#
# 미르코가 마을의 수장이라는 지위를 질투한 보르코는 그의 텐트로 쳐들어가 속임수를 써서 라도
# 미르코가 지도자로서 무능하다는 것을 보여주려 했다.
# 보르코는 탁자 위에 불투명한 컵 3개를 나란히 놓고(열린 부분을 아래로 향하게)
# 가장 왼쪽 컵 아래에 작은 공을 놓는다.
# 그런 다음 세 가지 가능한 방법 중 하나로 두 개의 컵을 여러 번 바꾼다.
# 미르코는 공이 어느 컵 아래에 있는지 말해야 한다.
#
# 보르코가 모르는 것은 뒤쪽에 있는 프로그래머들이 그들의 모든 움직임을 기록하고 있고,
# 공이 어디에 있는지 알아내기 위해 간단한 프로그램을 사용할 것이다. 그 프로그램을 작성하라.
#
# 입력사항
# 모든 방향의 기준은 미르코(반대편)에서 보는 것으로 가정
# 첫 번째이자 유일한 줄에는 최대 50자로 구성된 문자열이 들어 있다.
# 각 문자는 A, B, C 이다. <행동을 규정한다>
# A는 왼쪽과 가운데 컵 교환
# B는 가운데와 오른쪽 컵 교환
# C는 왼쪽과 오른쪽 컵 교환 <또 다른 경우의 수는 없는가? 컵의 모서리로 공을 쳐서 다른 컵으로 옮기는 트릭? 같은 행동은 하지 않는가?>
#
# 경우의 수 ABC 일 때
# ABC, ACB, BAC, BCA, CAB, CBA 모두 6가지 경우의 수가 나옴 n*(n-1)*(n-1)* ... *2*1  = 3*2*1 = 6
# 출력 사항
# 공이 있는 컵의 인덱스를 출력하라.
# 왼쪽 컵 아래 있으면 1
# 중간 컵 아래 있다면 2
# 오른쪽 컵 아래 있다면 3
#
# 도메인 분석
# 1. 입력 : 시작할 때 공이 어디있는지 알고 있음 A
# - 컵은 최대 50번 swap 된다.
# - 입력은 ABC이외의 글자, 숫자 허용하지 않는다.
# - 입력(ENTER)는 한 번 만 한다.
# 2. 동작 : 컵을 옮기는 동작(swap)을 카운트한다.
# - A는 왼쪽과 가운데 컵 교환
# - B는 가운데와 오른쪽 컵 교환
# - C는 왼쪽과 오른쪽 컵 교환
#
# swaps 컵을 옮기는 동작, swap_type 컵옮기는 타입(ABC), ball_location 공이 있는 위치
def chech_chr_input(swaps):
    allowed_chars = {'A', 'B', 'C'}
    for char in swaps:
        if char not in allowed_chars:
            return False
    return True

swaps = input("컵을 옮기는 동작(ABC)를 50가지 이내로 입력하세요. : ")
swaps = swaps.upper() #소문자-> 대문자

if not swaps.isalpha():
    exit("문자열로 입력되지 않음")
swaps_length = len(swaps)
if swaps_length == 0 or swaps_length > 50:
    exit("컵 옮기는 횟수가 범위를 벗어남(0 < n <= 50)")
if swaps.count('\n'):
    exit("입력에 개행표시가 있음")
if swaps.count(' '):
    exit("입력에 공백이 있음")

#if swaps.count('A') + swaps.count('B') + swaps.count('C') == 0:
#    exit("컵 옮기는 동작 ABC가 하나도 입력되지 않았습니다.")
#if not ('A' in swaps or 'B' in swaps or 'C' in swaps):
#    exit("컵 옮기는 동작 ABC 이외의 문자가 입력되었습니다.")

if not chech_chr_input(swaps):
    exit("입력한 문자열에 허용되지 않는 문자가 포함되어 있습니다.")

#최초에 공이 왼쪽에 있다고 정의함
ball_location = 1

for swap_type in swaps:
    if swap_type == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 1:
        ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1

print(ball_location)
