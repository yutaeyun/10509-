
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

# 100 미만의 피보나치 수열 출력하기

"""
fibonacci = 1
n = 0
m = 0

while fibonacci < 100:
    print(fibonacci)
    m = n
    n = fibonacci
    fibonacci = m + n
"""

fibonacci_list = {1,1}
n = 1

while fibonacci_list[n-1]+fibonacci_list[n] < 100:
    fibonacci_list.append(fibonacci_list[n-1]+fibonacci_list[n])
    n = n+1
