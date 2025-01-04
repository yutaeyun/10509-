## 1부터 10까지 숫자를 출력한다.

for i in range(10):
    print(i+1)

print("##########")

for i in range(1, 11):
    print(i)

print("##########")
print(list(range(1, 11)))

## 여기서 부터는 조건을 같이
# 369 게임
# 1, 2, 짝(3)
# 1~100
# .include
# 33 -> 짝 or 짝짝

for i in range(1, 101):
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("짝짝")
    else:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("짝")
        else:
            print(i)

print("########################################################")

for i in range(1, 101):
    clap = ""
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        clap = clap + "짝"
    if i % 10 == 3 or i % 10 == 6 or i %  10 == 9:
        clap = clap + "짝"

if len(clap) == 0:
    print(i)
else:
    print(clap)

print("########################################################")

# 문제 1
# 사용자한테 숫자하나를 입력>
# 해당 숫자의 구구잔을 출력
# 2 를 입력받으면
# 2*1=2  ~ 2*9=18

user_input = int(input("숫자를 입력해주세요"))

for i in range(2, 10):
    print(user_input, "*", i, "=", user_input * i)

print("########################################################")

# 문제 2
# 10 개의 랜덤 알파벳을 배열로 생성
# [Q,W,A,F,S,C,G,D,E,T]
# 하나씩 출력되며, 사용자가 해당 알파벳을 빠르게 입력하는 게임
# 출력 : Q
# 사용자 입력 : Z  <- 넘어가지 않음
# 사용자 입력 : Q <- 다음문제인 W가 출력됨


import random

alphabet = []

for i in range(0, 10):
    alphabet.append(chr(random.randrange(65, 91)))

for alpha in alphabet:
    print(alphabet[0])
    while user_input != alpha:
        user_input = input("")
