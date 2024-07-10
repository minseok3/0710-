# 조건문

# if 3 > 1 :
#     print("3은 1보다 큽니다.")
#     print("연산을 종료합니다.")
# print("-"*15)
# print("저는 들여쓰기를 하지 않은 라인입니다.")

# 비교연산자

# a = "김민석"
# b = "한원우"
# # if a == b :
# if a != b :
#     print("두 사람의 이름은 다릅니다.")

# 연습문제
# c = input("'안녕하세요'를 입력하세요:")
# if c == "안녕하세요" :
#     print("반갑습니다.")

# a = "김민석"
# b = "한원우"
#
# if a == b :
#     print("두 사람의 이름은 다릅니다.")
# elif a != b :
#     print("두사람의 이름은 다릅니다.")

# num_1 = 10
# num_2 = 3
#
# if num_1 < num_2 :
#     print("num_1은 num_2보다 크기가 작습니다.")
#
# elif num_1 == num_2 :
#     print("num_1은 num_2보다 크기가 같습니다.")
#
# elif num_1 > num_2 :
#     print("num_1은 num_2보다 크기가 큽니다.")

# 연습문제
# text = int(input("숫자를 입력하세요:"))
# text = int(text)
# sum = int(text) + 100

#연습문제
# num = int(input("임의의 숫자를 입력하시오:"))
# if 5 < num < 10 :
#     print("ok")
# else:
#     print("no")
# # elif num >= 10 :
# #     print("no")
# # elif num <= 5 :
# #     print("no")

# and or
# apple = '사과'
# banana = '감자'
#
# if apple == '사과' or banana == '바나나' :
#     print("문자열이 모두 정확합니다.")
#
# # 조회
# var = [1,2,3]
# if 찾고자하는 요소 in 변수:
#     print("숫자 3이 var 변수에 있습니다.")

# fruit = ["사과","포도","홍시"]
# 입력 = input("과일을 입력하세요:")
# if 입력 in fruit :
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# fruit = {"봄" : "사과", "여름" : "포도", "가을" : "홍시"}
# wh = input("계절을 입력하세요:")
# if wh in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

text = input("문자를 입력하세요:")
if len(text) < 20:
    print("요금은 50원 입니다.")
elif len(text) > 20:
    print("요금은 100원 입니다.")