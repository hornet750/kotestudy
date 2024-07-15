# https://dmoj.ca/problem/ccc08j2
#
# 문자열 자르기 (String Slicing) 반복 횟수는 얼마나 많은 버튼이 눌렸는지에 따라 다르다
# 교재본
# 각각 A, B, C, D, E라는 5곡의 노래가 있다. 재생 목록을 만들어 앱에서 관리 함.
# 처음에는 노래가 A, B, C, D, E 순서로 재생된다.
# 앱에는 4개의 버튼이 있다.
# 버튼 1 : 첫 번째 곡을 재생목록의 끝으로 이동
# 버튼 2 : 마지막 곡을 재생목록의 시작 부분(버튼1 의 반대)
# 버튼 3 : 처음 두 곡의 위치를 바꿈
# 버튼 4 : 재생
#
# 입력
# 입력은 한 쌍의 라인들로 구성.
# 1. 어떤 버튼인지
# 2. 몇 번 눌렀는지
#
# 출력
# 재생목록의 노래 순서를 출력. 한 줄로 출력 및 각 노래를 구분하는 공백이 있어야 함

# songs = 'ABCDE'
# songs = songs[0] + songs[1] + songs[2] + songs[3] + songs[4]
#           A        B          C           D          E

# 이 방법은 곡이 딱 5개만 있을 때 쓸 수 있는 방법 -> 문자열 자르기를 하면 더 일반적이고 오류가 적은 프로그램을 만들 수 있다.


# songs = 'abcde'
# songs[0:4] 문자열 전체는 songs[:]로도 표현 가능 앞, 혹은 뒤부터 전부를 선택하는 것은 숫자로 지정해주지 않아도 된다.
# 자르기에는 음수 인덱스도 사용가능 음수의 기준은 오른쪽부터

songs = 'ABCDE'
button = 0

while button != 4:
    button = int(input())
    if not 0 <= button <= 4:
        exit("버튼 번호를 제대로 입력해주세요")

    presses = int(input())
    for i in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''
for song in songs:
    output = output + song + ' '

print(output[:-1])