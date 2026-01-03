"""
6장 제어문
"""
"""
    6.1 조건에 따라 분기하기: 조건문
"""
# # weather = "맑음" # "미세먼지" # "비"
# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("준비물이 필요 없어요.")

# weather = input("오늘 날씨는 어때요? ")
# print(weather)

# temp = input("오늘 기온은 어때요? ")
# temp = int(temp)

# if 30 <= temp:
#     print("너무 더워요. 外出을 自制하세요.")
# elif 10 <= temp:
#     print("活動하기 좋은 날씨예요.")
# elif 0 <= temp:
#     print("外套를 챙기세요.")
# else:
#     print("너무 추워요. 感氣 操心하세요.")

# if temp >= 30:
#     print("very hot")
# elif temp >= 10:
#     print("good weather")
# elif temp >= 0:
#     print("take a jacket")
# else:
#     print("very cold")

"""
    6.2 같은 일 반복하기: 반복문
"""
"""
        6.2.1 범위 안에서 반복하기: for 문
"""
# waiting_range = [1, 2, 3, 4, 5]
# for waiting_no in range(1, 6, 2):
#     print("대기번호 : {0}".format(waiting_no))

# orders = ["아이언맨", "토르", "스파이더맨"]
# for customer in orders:
#     print(f"{customer} 님, 커피가 준비됐습니다. 픽업대로 와 주세요.")

# customer = "토르"
# index = 5

# while index >= 1:
#     print(f"{customer} 님, 커피가 준비됐습니다.")
#     index -= 1
#     print(f"{index}번 남았어요.")
#     if index == 0:
#         print("커피를 폐기 처분합니다.")

customer = "아이언맨"
index = 1

while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index += 1


