# Boolean 표현식, if 문
#
# question ID : ccc15j2
# Happy or Sad
# :-) 행복한 얼굴, :-( 슬픈 얼굴
# 메시지의 전반적인 분위기를 결정하는 프로그램을 작성하시오.
#
# 입력 사항
# 1~255자의 문자입력
#
# 출력 사항
# - 입력 줄에 행복한 이모티콘이나 슬픈이모티콘이 없으면 none 을 출력
# - 그렇지 않은 경우, 입력 줄에 행복, 슬픈 이모티콘이 같은 수로 포함되어있으면 unsure. 출력
# - 행복 > 슬픈 = happy 출력
# - 행복 < 슬픈 = sad 출력

# 이문제의 포인트는 이모티콘을 카운트하는 conut 명령어의 사용이다.

feeling = input()

happy_count = feeling.count(':-)')
sad_count = feeling.count(':-(')

if happy_count == 0 and sad_count == 0:
    print('none')
elif happy_count > sad_count:
    print('happy')
elif sad_count > happy_count:
    print('sad')
else:
    print('unsure')