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
subway = ["푸", "피글렛", "티거"]
# print(type(subway))
# print(subway)
# print(subway.index("피글렛"))

subway.append("이요르")
# print(subway)

# subway.insert(1, "루")
subway.insert(subway.index("피글렛"), "루")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.clear()
print(subway)