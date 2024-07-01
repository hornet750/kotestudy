# 조건부 실행, Boolean 타입, 관계 연산자 IF 문
#
# question ID : ccc19j1
# Winning Score
# You record all of the scoring activity at a basketball game. 농구 게임의 모든 득점을 기록하라.
# Points are scored by a 3-point shot, a 2-point field goal, or a 1-point free throw. 3점, 2점, 1점짜리 포인트가 있다.
#
# You know the number of each these types of scoring for the two teams:  2개의 팀이 있다.
# the Apples and the Bananas.
# Your job is to determine which team won, or if the game ended in a tie. 너의 일은 어떤 팀이 이겼는지, 아니면 동점인지 결정하는 것이다.
#
# 상세 입력 사항
#
# The first three lines of input describe the scoring of the Apples, 첫 3개의 입력인자는 Apples의 점수
# and the next three lines of input describe the scoring of the Bananas. 다음 3개의 입력인자는 Bananas의 점수
# For each team, the first line contains the number of successful 3-point shots, 각 팀의 첫 라인은 3점슛
# the second line contains the number of successful 2-point field goals, 각 팀의 두번 째 라인은 2점 필드골
# and the third line contains the number of successful 1-point free throws. 세번 째 라인은 1점 프리드로우
# Each number will be an integer between 0 and 100, inclusive. 각 입력값은 0부터 100까지이다. 0과 100을 포함.
#
# 상세 출력 사항
#
# The output will be a single charactor. 출력은 1개의 문자로 출력
# If the Apples scored more points than the Bananas, output A. 만약 애플 점수가 바나나보다 크면 A
# If the Bananas scored more points than the Apples, output B. 만약 바나나 점수가 애플보다 크면 B
# Otherwise, output T, to indicate a tie. 다른  경우, 동점일경우,  T가 출력 된다.

# 입력값이 없이 엔터를 쳤을 경우 에러가 발생, 이럴때는 어떻게 오류처리를 할까? 변수 초기값 입력 def 라는게 있다는데?

# Apple팀의 스코어 변수값
apple_three = int(input())
apple_two = int(input())
apple_one = int(input())
# Banana팀의 스코어 변수값
banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

if apple_three > 100 or apple_three < 0:
    print('입력값이 0보다 작거나 100이상입니다. apple_three의 값=' + str(apple_three))
if apple_two > 100 or apple_two < 0:
    print('입력값이 0보다 작거나 100이상입니다. apple_two의 값=' + str(apple_two))
if apple_one > 100 or apple_one < 0:
    print('입력값이 0보다 작거나 100이상입니다. apple_one 값=' + str(apple_one))
if banana_three > 100 or banana_three < 0:
    print('입력값이 0보다 작거나 100이상입니다. banana_three의 값=' + str(banana_three))
if banana_two > 100 or banana_two < 0:
    print('입력값이 0보다 작거나 100이상입니다. banana_two의 값=' + str(banana_two))
if banana_one > 100 or banana_one < 0:
    print('입력값이 0보다 작거나 100이상입니다. banana_one의 값=' + str(banana_one))

#총 점수 합
apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one

if apple_total < banana_total:
    print('B')
elif apple_total > banana_total:
    print('A')
else:
    print('T')