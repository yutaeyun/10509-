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
# 사용자한테 숫자하나를 입력>
# 해당 숫자의 구구잔을 출력
# 2 를 입력받으면
# 2*1=2  ~ 2*9=18

import random

alphabet = []

for i in range(0, 10):
    alphabet.append(chr(random.randrange(65, 91)))

print(alphabet[0])
user_input = input()