# 자판기 내용 가지고 dictionary개념 배워볼 예정 (가격 추가)

# 자판기 프로그램 짤 것
# 사용자 모드 / 관리자 모드

"""
음료 종류: 코카콜라, 민트초코 우유, 코코팜, 망고 주스, 몬스터 

1. 사용자 모드
- 남아있는 음료가 없으면 "재고가 없습니다"
- 현금 또는 카드로 음료 결제
- 현금 결제시 돈이 부족하면 "잔액부족"


2. 관리자 모드
- 물건 추가
- 가격 변경
- 물건 추가
- 관리자 모드에서는 음료 마음것 마실 수 있음
"""

# 각각의 dictionary

inventory = {'coke': 10, 'cider': 5, 'mintchoco-milk': 3}

price = {'coke': 800, 'cider': 700, 'mintchoco-milk': 1000}

mode = "manager"


def print_menu():
    print("menu를 출력합니다.")

    for i in inventory.keys():
        print(i, "가격:", price[i], " 잔여수량:", inventory[i])


def buy_drink():
    print("음료를 선택하고, 구매합니다.")


def switch_mode():
    print("모드를 전환합니다.")

    global mode

    if mode == "manager":

        mode = "user"

    else:

        mode = "manager"


def manager_login():
    print("관리자 모드에 진입합니다.")


def print_function():
    print("관리자가 사용가능한 기능을 출력합니다.")

    print("1. 음료를 등록하기")

    print("2. 음료를 추가하기")

    print("3. 음료를 빼기")

    print("4. 음료를 삭제하기")

    print("5. 사용자 모드로 전환")


def change_price():
    print("음료의 가격을 변경합니다.")


def add_drink():
    print("음료를 추가합니다.")


def register_drink():
    print("음료를 등록합니다.")


def delete_drink():
    print("음료를 삭제합니다.")


def extract_drink():
    print("음료를 뺍니다.")


while True:

    if mode == "manager":

        manager_login()

        user_input = int(input("메뉴를 선택하세요"))

        if user_input == 1:

            register_drink()

        elif user_input == 2:

            add_drink()

        elif user_input == 3:

            extract_drink()

        elif user_input == 4:

            delete_drink()

        elif user_input == 5:

            switch_mode()



    else:

        print_menu()

        user_input = input("메뉴를 선택하세요")