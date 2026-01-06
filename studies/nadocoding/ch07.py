"""
7장 함수
"""
"""
    7.1 함수 정의하기
"""
"""
        7.1.1 실습: 은행 계좌 개설하기
"""
# def open_account():
#     print("새로운 계좌를 개설합니다.")

# open_account()

"""
    7.2 전달값과 반환값
"""
"""
        7.2.1 실습: 입금하기
"""
# def deposit(balance, money):
#     print(f"{money}원을 입금했습니다. 잔액은 {balance + money}원 입니다.")
#     return balance + money

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

"""
        7.2.2 실습: 출금하기
"""
# def withdraw(balance, money):
#     if balance >= money:
#         print(f"{money}원을 출금했습니다. 잔액은 {balance - money}원입니다.")
#         return balance - money
#     else:
#         print(f"잔액이 부족합니다. 잔액은 {balance}원입니다.")
#         return balance

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)

"""
        7.2.3 실습: 수수료 부과하기
"""
# def withdraw_night(balance, money):
#     commission = 100
#     print(f"업무 시간 외에 {money}원을 출금했습니다.")
#     return commission, balance - money - commission

# commission, balance = withdraw_night(balance, 500)
# print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))

"""
    7.3 함수 호출하기
"""
"""
        7.3.1 기본값 사용하기
"""
# def profile(name, age = 20, main_lang = "파이썬"):
#     print("이름 : {}\t나이 : {}\t주 사용 언어 : {}".format(name, age, main_lang))

# profile("찰리")
# # profile("루시")
# profile("찰리", 22)
# profile("찰리", 24, "자바")

"""
        7.3.2 키워드 인자 사용하기
"""
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "찰리", main_lang = "파이썬", age = 20)
# profile(main_lang = "자바", age = 25, name = "루시")

# profile("찰리", age = 20, main_lang = "파이썬")
#  profile(name = "루시", 25, "파이썬") # SyntaxError: positional argument follows keyword argument

"""
        7.3.3 가변 인자 사용하기
"""
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {}\t나이 : {}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("찰리", 20, "파이썬", "자바", "씨", "씨뿔뿔", "씨샵")
# profile("루시", 25, "코틀린", "스위프트", "", "", "")

# def profile(name, age, *language):
#     print("이름 : {}\t나이 : {}\t".format(name, age), end = " ")
#     # print(language, type(language))
#     [print(lang, end = " ") for lang in language]
#     # for lang in language:
#     #     print(lang, end = " ")
#     print()

# profile("찰리", 20, "파이썬", "자바", "씨", "씨뿔뿔", "씨샵", "자바스크립트")
# profile("루시", 25, "코틀린", "스위프트")

# def add(item: str) -> str:
#     return item + " 붓기"

# ingredients = ("뜨거운 물", "에스프레소")
# def americano(ingredients: tuple) -> None:
#     sequence = 0
#     for item in ingredients:
#         sequence += 1
#         print(f"{sequence}. {add(item)}")
#     print(f"이 레시피는 총 {sequence}단계로 이루어져 있습니다.")

# print("아메리카노 만드는 법")
# americano(ingredients)

"""
    7.4 변수의 범위: 지역변수와 전역변수
"""
# glasses = 10

# def rent_return(glasses, people):
#     glasses = glasses - people
#     print("[함수 내부] 남은 3D 안경 개수: {}".format(glasses))
#     return glasses

# print("전체 3D 안경 개수: {}".format(glasses))
# glasses = rent_return(glasses, 2)
# print("남은 3D 안경 개수: {}".format(glasses))

"""
    7.5 실습 문제: 표준 체중 구하기
"""

# height = 175
# gender = "남자"

# def std_weight(height: float, gender: str) -> float:
#     if gender == "남자":
#         gender_constant = 22
#     else:
#         gender_constant = 21

#     return round(height * height * gender_constant, 2)

# print(f"키 {height}cm {gender}의 표준 체중은 {std_weight(height = height / 100, gender = gender)}kg입니다.")

# std_weight(1.75, "남자")

"""
    마무리
"""
def get_air_quality(fine_dust: int) -> str:
    if 0 <= fine_dust <= 30:
        air_quality_conditions = "좋음"
    elif 31 <= fine_dust <= 80:
        air_quality_conditions = "보통"
    elif 81 <= fine_dust <= 150:
        air_quality_conditions = "나쁨"
    elif fine_dust >= 151:
        air_quality_conditions = "매우 나쁨"
    else:
        air_quality_conditions = "잘못된 값"
    
    return air_quality_conditions

print(get_air_quality(15))
print(get_air_quality(85))
print(get_air_quality(-1))
