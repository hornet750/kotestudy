# Boolean 표현식, if 문
#
# question ID : ccc07j1
# Who is in the Middle
# 무게가 각각 다른 3개의 그릇이 있다. 중간 무게의 그릇을 출력하라.
# 단 무게는 100보다 작은 양의 정수
#
# dish_wight = dw

dw1 = int(input())
dw2 = int(input())
dw3 = int(input())


if (dw1 >= dw2 and dw1 <= dw3) or (dw1 <= dw2 and dw1 >= dw3):
    print(dw1)
elif(dw2 >= dw1 and dw2 <= dw3) or (dw2 <= dw1 and dw1 >= dw3):
    print(dw2)
else: print(dw3)