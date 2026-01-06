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

"""
        6.2.2 조건을 만족할 동안 반복하기: while 문
"""
# customer = "토르"
# index = 5

# while index >= 1:
#     print(f"{customer} 님, 커피가 준비됐습니다.")
#     index -= 1
#     print(f"{index}번 남았어요.")
#     if index == 0:
#         print("커피를 폐기 처분합니다.")

# customer = "아이언맨"
# index = 1

# while True:
#     print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = None

# while person != customer:
#     print(f"{customer} 님, 커피가 준비됐습니다.")
#     person = input("이름이 어떻게 되세요? ")

"""
        6.2.3 흐름 제어하기: continue와 break
"""
# absent = [2, 5]
# no_book = [7]

# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘 수업은 여기까지. {student}번 학생은 교무실로 따라와요.")
#         break
#     print(f"{student}번 학생, 책을 읽어 보세요.")

"""
        6.2.4 for 문 한 줄로 작성하기(list comprehension)
"""
# students = list(range(1, 6))
# print(students)

# students = [i + 100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "Spider Man"]
# print(students)

# # students = [len(i) for i in students]
# # print(students)

# students = [i.upper() for i in students]
# print(students)

"""
    6.3 실습 문제: 택시 승객 수 구하기
"""
# from random import randrange

# total_count = 0

# for customer in range(1, 51):
    # time = randrange(5, 51)
#     if 5 <= time <= 15:
#         matched = "0"
#         total_count += 1
#     else:
#         matched = " "
#     print(f"[{matched}] {customer}번째 손님 (소요시간 : {time}분)")
# print(f"총 답승객 : {total_count}명")

"""
    마무리
"""
price = 1000
goods = 6
total_price = 0

for count in range(goods):
    print("2+1 상품입니다.")
    # if count % 3 != 0:
    #     total_price += price
    if count % 3 == 0:
        continue
    total_price += price
print("총 가격은 {}원 입니다.".format(total_price))
    
