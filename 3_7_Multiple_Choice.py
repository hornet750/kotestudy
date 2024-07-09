# https://dmoj.ca/problem/ccc11s2
#
# Multiple Choice
#
# 객관식 시험 5지 선다형
# 객관식 시험 하나를 채점하는 데 사용할 수 있는 프로그램을 작성하라
#
# 입력사양
# 1. 문제 수 입력 (숫자) 0 < N < 10000
# 2. 학생의 답안 입력 (A, B, C, D, E 중 1개)
# 3. 학생의 답안 입력이 끝나면 정답안 입력(A, B, C, D, E 중 1개)
#
# 출력사항
# 답을 맞춘 개수를 숫자로 출력하라


# 문제 수를 기준으로 학생 답안의 문자열, 정답의 문자열 2개의 문자열을 만들고,
# 2 개의 문자열을 서로 비교하여 맞으면 score가 하나씩 올라가도록 만들자.
num_problems = int(input("문제수를 입력하세요 : "))
if not 0 < num_problems < 100000:
    exit("입력 범위를 벗어남(0 < n <= 10,000)")


# 학생의 답안 열
# ABCDE만 입력받는 방법을 찾아야한다.
student_answer = ''
for i in range(num_problems):
    student_answer = student_answer + input("학생의 답안을 입력하세요 : ")
# 정답안 열
correct_answer = ''
for i in range(num_problems):
    correct_answer = correct_answer + input("정답을 입력하세요 : ")
# 점수계산
score = 0
for i in range(num_problems):
    if student_answer[i] == correct_answer[i]:
        score = score + 1

print(f"정답을 맞힌 개수는 : {score}")

