# 사용자에게 수학점수를 입력받아
# 상/중/하 반으로 분류 해주기
# 상 - 90점 이상인 사람
# 중 - 70점 이상인 사람
# 하 - 나머지

"""
size = int(input("수학 시험 점수를 입력해주세요"))
print(size)

if size > 100 or size < 0:
    print("점수를 잘못입력하셨습니다")
elif size >= 90:
    print("당신은 상반입니다")
elif size >= 70:
    print("당신은 중반입니다")
else:
    print("당신은 하반입니다")


if size > 100 or size < 0:
        print("점수를 잘못입력하셨습니다")
else:
    if size >= 90:
            print("당신은 상반입니다")
    elif size >= 70:
            print("당신은 중반입니다")
    else:
            print("당신은 하반입니다")
"""

# 예제 1번
# 사용자에게 숫자를 입혁받아서 홀수면 "홀수입니다", 짝수면 "짝수입니다"

# 예제 2번
# 사용자에게 문장 하나를 입력받아서
# "파이썬"이라는 글자로 시작하면
# "파이썬 관련된 얘기군요!"라고 답해주기

# 예제 3번
# "당신은 주말에 집에서 혼자 쉬는것을 선호하나요? (Y/N)" I/E
# "꼬리에 꼬리를 무는 밸런스 게임을 하면 힘든가요? (Y/N)"  S/N
# "슬픔을 둘로 나누면 슬과 픔이다? (Y/N)" T/J
# "계획했던 식당이 갑자기 휴무면 오히려 새로운 식당을 가볼수 있어서 개이득인가요?(Y/N)" P/J

"""
size = int(input("숫자를 입력해주세요"))
print(size)

if (size%2) == 1:
    print("홀수입니다")
else:
    print("짝수입니다")
"""

size = int(input(문장을 입력해주세요))