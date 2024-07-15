# https://dmoj.ca/problem/ccc02j2

# 미국과 캐나다의 영어 사용 철자가 다르다
#
# 미국은 neighbor, color 를 쓰고
# 캐나다는 neighbour, colour 를 쓴다.
# 미국인이 캐나다언어로 번역하는 프로그램을 만들어라
#
# 사용자는 단어를 입력한다 (최대 64자)
# 단어가 미국식 철자를 사용하면 캐나다 언어로 바꾸고,
# 캐나다 언어로 사용하면 그대로 출력한다
# 사용자가 quit!이라는 것을 입력하면 프로그램이 종료 되어야 한다
#
# 미국식 철자를 감지하는 법
# 단어가 4 글자 이상이고 자음 뒤에 or 접미사가 있다

done = False
vowels = list('aeiouy')


while not done:
    word = input()
    if word == 'quit!':
        done = True
    elif len(word) > 4 and not (word[-3] in 'aeiouy') and word[-2:] == 'or':
        print(word[:-2] + 'our')
    else:
        print(word)