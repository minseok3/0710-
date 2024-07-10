text = input("문자를 입력하세요:")
if len(text) <= 20:
    print("요금은 50원 입니다.")
elif len(text) > 20:
    print("요금은 100원 입니다.")
# else:
#     print("요금은 100원 입니다.")