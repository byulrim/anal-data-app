"""
4장 문자열 다루기
"""
"""
    4.1 문자열이란
"""
# sentence1 = "나는 소년입니다."
# print(sentence1, type(sentence1))

# sentence2 = '파이썬은 쉬워요.'
# print(sentence2, type(sentence2))

# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3, type(sentence3))

"""
    4.2 원하는 만큼 문자열 자르기: 슬라이싱
"""
# jumin = "990229-1234567"
# print("성별 식별번호: " + jumin[7])
# print("년: " + jumin[0:2])  # 0부터 2 직전까지 (0, 1)
# print("월: " + jumin[2:4])  # 2부터 4 직전까지 (2, 3)
# print("일: " + jumin[4:6])  # 4부터 6 직전까지 (4, 5)
# print("생년월일: " + jumin[:6])  # 처음부터 6 직전까지
# print("주민등록번호 뒷자리: " + jumin[7:])  # 7부터 끝까지

# print("주민등록번호 뒷자리(뒤에서부터): " + jumin[-7:])  # 뒤에서 7번째부터 끝까지

"""
    4.3 함수로 문자열 처리하기
"""
# python = "Python is Amazing"

# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(python[1:3].islower())
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
# index = python.index("n", 2, 6)
# print(index)
# index = python.index("Java")
# print(index)

# find = python.find("n")
# print(find)
# find = python.find("n", find + 1)
# print(find)
# find = python.find("Java")
# print(find)

# print(python.count("n"))
# print(python.count("v"))

# print(len(python))

"""
    4.4 문자열 포매팅
"""
# print("ab" + "ab")
# print("ab", "ab")

"""
        4.4.1 서식 지정자 사용하기
"""
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아합니다." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")
# print("나는 %s살입니다." % "20")

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

"""
        4.4.2 format() 함수 사용하기
"""
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

"""
        4.4.3 f-문자열 사용하기
"""
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") # formatted string

"""
    4.5 탈출 문자
"""
"""
        4.5.1 \n
"""
# print("백문이 불여일견 백견이 불여일타")
# print("""백문이 불여일견
# 백견이 불여일타""")
# print("백문이 불여일견\n백견이 불여일타")

"""
        4.5.2 \"와 \'
"""
# print("저는 "나도코딩"입니다.") # SyntaxError
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')

# print("저는 \'나도코딩\'입니다.")
# print("저는 \"나도코딩\"입니다.")

"""
        4.5.3 \\
"""
# print("C:\Users\Nadocoding\Desktop\PythonWorkspace") # SyntaxError
# print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
# print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace") #  raw string

"""
        4.5.4 \r
"""
# print("Red Apple\rPine") # carriage return

"""
        4.5.5 \b
"""
# print("Redd\bApple") # backspace

"""
        4.5.6 \t
"""
# print("Red\tApple") # Tab

# url = "http://naver.com"
# url = "http://daum.net"
# url = "http://google.com"
# url = "http://youtube.com"

# password = url.replace("http://", "")
# password = password[0 : password.find(".")]
# password = password[0 : 3] + str(len(password)) + str(url.count("u")) + "!"
# print(f"{url}의 비밀번호는 {password}입니다.")

# sentance = "the early bird catches the worm."
# sentance = "Actions Speak Louder Than Words."
sentance = "PRACTICE MAKES PERFECT."
print(sentance[0].upper() + sentance[1:].lower())
