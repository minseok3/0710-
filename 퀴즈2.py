text = int(input("점수를 입력하세요:"))
if 0 <= text <= 20:
    print("E")
elif 21 <= text <= 40:
    print("D")
elif 41 <= text <= 60:
    print("C")
elif 61 <= text <= 80:
    print("B")
elif 81 <= text <= 100:
    print("A")