# https://dmoj.ca/problem/ccc11s1
#
# English or French
# 영어 텍스트와 프랑스어 텍스트를 구별할 수 있는 시스템 만들어라.
# 1. 주어진 텍스트에 t 및 T 문자가 s 및 S 문자보다 많은 경우 == English
# 2. 주어진 텍스트에 s 및 S 문자가 t 및 T 문자보다 많은 경우 == French
# 3. t의 문자수와 T의 문자수, s의 문자수와 S의 문자수가 같으면 == French
#
# 입력사항
# 첫 번째 입력 line 수를 입력한다.
# 각 라인에는 최소 한 문자 이상 있다.

# 몇 줄을 사용할 것인지 정수를 입력받는다.
line_count = int(input())
# s와 t의 수를 담을 변수 선언
s_cnt = 0
t_cnt = 0

for i in range(line_count):
    # 각 줄의 문자를 입력 받는다.
    text = input()
    # s와 t를 count 명령어로 몇개가 있는지 찾는다.
    s_cnt = s_cnt + text.count('s') + text.count('S')
    t_cnt = t_cnt + text.count('t') + text.count('T')

if t_cnt > s_cnt:
    print('English')
elif t_cnt < s_cnt:
    print('French')
elif t_cnt == s_cnt:
    print('French')
