"""
7장 함수
"""
"""
    7.1 함수 정의하기
"""
"""
        7.1.1 실습: 은행 계좌 개설하기
"""
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

"""
    7.2 전달값과 반환값
"""
"""
        7.2.1 실습: 입금하기
"""
def deposit(balance, money):
    print(f"{money}원을 입금했습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

"""
        7.2.2 실습: 출금하기
"""