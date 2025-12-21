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

mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(mix_list)
print(num_list)