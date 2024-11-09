
#수학 성적이 비전상적인 입력인 경우 다시 입력을 받는다
num = -1

while num > 100 or num <0:
    num = int(input("수학 성적을 입력해주세요, ::"))

if num >80:
    print("A반입니다")
elif num > 60:
    print("B반입니다")
else:
    print("C반입니다")


print("===========================")

count = int(input("숫자 하나를 입력하세요 >>"))
i  = 0

while i < count:
    print("*")
    i = i + 1


import random
value = random.randrange(1,100)
print(value)

