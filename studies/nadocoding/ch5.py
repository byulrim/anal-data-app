"""
5장 자료구조
"""
"""
    5.1 리스트
"""
"""
        5.1.1 리스트 생성하기
"""
# subway1 = 10
# subway2 = 20
# subway3 = 30
# print(f"{subway1}, {subway2}, {subway3}")

# subway = [10, 20, 30]
# print(subway)

# empty_list = []
# print(type(empty_list))
# print(empty_list)

"""
        5.1.2 값 추가/삽입/삭제하기
"""
# subway = ["푸", "피글렛", "티거"]
# print(type(subway))
# print(subway)
# print(subway.index("피글렛"))

# subway.append("이요르")
# print(subway)

# subway.insert(1, "루")
# subway.insert(subway.index("피글렛"), "루")
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# subway.clear()
# print(subway)

"""
        5.1.3 중복 값 확인하기
"""
# subway = ["푸", "피글렛", "티거"]
# subway.append("푸")
# print(subway)
# print(subway.count("푸"))
# subway.sort()
# print(subway)

"""
        5.1.4 리스트 정렬하기
"""
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# num_list.sort(reverse = True)
# print(num_list)

# num_list.reverse()
# print(num_list)

# my_list = [1, 3, 2]
# my_list.sort()
# print(my_list)

# your_list = [1, 3, 2]
# new_list = sorted(your_list)
# print(your_list)
# print(new_list)

"""
        5.1.4 리스트 확장하기
"""
# mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
# print(mix_list)
# print("멍멍이" in mix_list)

# mix_list = ["푸", 20, True]
# num_list = [5, 2, 4, 3, 1]
# num_list.extend(mix_list)
# print(mix_list)
# print(num_list)

"""
    5.2 딕셔너리
"""
"""
        5.2.1 딕셔너리 생성하기
"""
# cabinet = {3: "푸", 100: "피글렛"}

# empty_dict = {}
# print(type(empty_dict))

# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(101))   # 해당 키에 해당하는 데이터가 없으면 None 반환

# print(cabinet.get(5))
# print("hi")
# print(cabinet[5])
# print("hi")

# print(cabinet.get(5, "사용가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3": "푸", "B-100": "피글렛"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print("곰" in "곰돌이")
# print("돌이" in "곰돌이")
# print("푸" in "곰돌이")

"""
        5.2.2 값 변경/추가/삭제하기
"""
# cabinet = {"A-3": "푸", "B-100": "피글렛"}
# print(cabinet, "\n", type(cabinet))
# cabinet["A-3"] = "티거"
# cabinet["C-20"] = "이요르"
# print(cabinet)      

# del cabinet["A-3"]
# print(cabinet)

"""
        5.2.3 값 확인하기
"""
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

"""
    5.3 튜플
"""
# menu = ("돈가스", "치즈돈가스")
# print(menu[0])
# print(menu[1])
# print(menu[-2:])

# name = "피글렛"
# age = 20
# hobby = "코딩"

# (name, age, hobby) = ("피글렛", 20, "코딩")
# print(name, age, hobby)

# (departure, arrival) = ("김포", "제주")
# print(f"{departure} > {arrival}")
# (departure, arrival) =(arrival, departure)
# print(f"{departure} > {arrival}")

"""
    5.4 세트
"""
# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"푸", "피글렛", "티거"}
# python = set(["푸", "이요르"])
# print(java, python)

# empty_set = set()
# print(empty_set, type(empty_set))
# print(java.intersection(python))
# print(java & python)

# print(java | python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))

# print(python - java)
# print(python.difference(java))

# python.add("피글렛")
# print(python)

# java.remove("피글렛")
# print(java)

"""
    5.5 자료구조 변환하기
"""
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

"""
    5.6 실습문제
"""
# from random import shuffle, sample

# users = range(1, 21)
# users = list(users)

# shuffle(users)
# winners = sample(users, 4)

# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {winners[0]}")
# print(f"커피 당첨자 : {winners[1:]}")
# print("-- 축하합니다! --")

"""
    마무리
"""
subjects = ["자료구조", "알고리즘", "자료구조", "운영체계"]
subjects = set(subjects)
subjects = list(subjects)
print(f"신청한 과목은 다음과 같습니다.\n{subjects}")
