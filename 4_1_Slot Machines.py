# https://dmoj.ca/problem/ccc00s1
#
# 교재본 반복 횟수는 처음 주어진 집의 수와 슬롯머신이 지불하는 상금의 칩 수에 따라 다르다
# for 루프가 아닌, while 루프를 사용한다.
#
# 마르타는 카지노에 가서 n개의 칩을 교환했다. -> 칩 개수 n개 입력
# 카지노에는 3개의 슬롯머신이 있고, 칩이 다 떨어질 때까지 슬롯머신을 순서대로 플레이한다.
# 예를 들어, 첫 번째 슬롯머신을 플레이하고,
#          두 번째 슬롯머신을 플레이한 다음,
#          세 번째 슬롯머신을 플레이 한다.
#        그리고 다시 첫 번째부터 플레이, 다음 두 번째.. 로 하는 식
# 각 플레이 비용은 칩 1개.
# 슬롯 머신 규칙
# - 첫 번째 슬롯머신에서 35번 플레이할 때마다 칩 30개를 얻는다. 1회 0.85717
# - 두 번째 슬롯머신에서 100번 플레이할 때마다 칩 60개를 얻는다. 1회 0.6
# - 세 번째 슬롯머신에서 10번 플레이할 때마다 칩 9개를 얻는다. 1회 0.9
# - 그 이외에는 플레이에 어떤 상금도 없다.
#
# 더 이상 남은 칩이 없을 때까지 마르타가 슬롯머신을 플레이한 횟수를 계산하라.

chips = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0

while chips >= 1:
    machine = plays % 3
    chips = chips -1
    if machine == 0:
        first = first + 1
        if first % 35 == 0:
            chips = chips + 30
    elif machine == 1:
        second = second + 1
        if second % 100 == 0:
            chips = chips + 60
    elif machine == 2:
        third = third + 1
        if third % 10 == 0:
            chips = chips + 9

    plays = plays + 1

print('Martha plays', plays, 'times before going broke.')
