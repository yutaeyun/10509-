# 예제 1번

num = int(input("숫자를 하나 입력해주세요. ::"))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
"""
"""
# 예제 2번

str = input("안녕하세요! 무슨 주제에 대해 말씀하고 싶으세요? :: ")
if str[:6] == "Python":
    print("파이썬 관련된 얘기군요!")

# 예제 3번

MBTI = ""

print("당신은 주말에 보통 무엇을 하며 시간을 보내나요?")
print("1. 집에서 쉬는 편이다")
print("2. 친구들과 약속을 잡아 나가는 편이다")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "I"
elif answer == 2:
    MBTI = MBTI + "E"

print("갑자기 상공에 외계인이 나타난다면?")
print("1. 어쩌면 인간 친화적인 외계인일지도..?")
print("2. 외계인이 왜 나타나냐")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "N"
elif answer == 2:
    MBTI = MBTI + "S"

print("슬픔을 둘로 나누면?")
print("1. 슬과 픔")
print("2. 슬픔이 덜어진다")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "T"
elif answer == 2:
    MBTI = MBTI + "F"

print("계획했던 식당이 갑자기 휴무면?")
print("1. 근처 아무 식당이나 간다")
print("2. 이미 Plan B가 있다")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "P"
elif answer == 2:
    MBTI = MBTI + "J"

print("당신의 MBTI는 -> ", MBTI)