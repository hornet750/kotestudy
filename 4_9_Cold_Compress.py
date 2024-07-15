# https://dmoj.ca/problem/ccc19j3


# 새로운 휴대폰 요금제는 모든 문자에 대해 과금
#
# 각 기호에 대해 연속적으로 나타나는 회수를 적고 그 뒤에 기호를 적는다
# 이 압축 기술을 인코딩이라 한다
#
# 블록은 가능한 긴 동일한 심볼의 하위 문자열이다
# 블록은 블록의 길이 다음에 해당하는 블록의 심볼이 오는 압축된 형태로 표현된다
# 문자열의 인코딩은 문자열의 각 블록을 문자열에 나타나는 순서대로 표현한 것이다
#
# 입력 사항
# 첫 번째 : 입력 줄의 수
# 다음 줄 부터 입력 최소 하나 이상 80이하
#
# 출력 사항
# i+1 입력이 되고 줄의 인코딩은 공백으로 구분된 쌍의 시퀀스가 나오고
# 각 쌍은 정수 뒤에 공백, 그 뒤에 문자가 옴
#
# 입력된 문자의 갯수를 확인하고 그 문자를 뒤에 출력한다

input_line_cnt = int(input())
if not 0 <= input_line_cnt < 1000:
    exit("입력의 범위를 벗어남(0 <= N < 1000)")

for dataset in range(input_line_cnt):
    result = ''
    line = input("보낼 메시지를 입력하시오 : ")
    total = 1

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            total = total + 1
        else:
            result = result + f'{total} {line[i]} '
            total = 1

    result = result + f'{total} {line[-1]}'

    print(result)
