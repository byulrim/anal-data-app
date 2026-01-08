"""
8장 입출력
"""
"""
    8.1 표준 입력받기: input()
"""
# answer = input("아무 값이나 입력하세요: ")
# print("입력한 값은 " + answer + "입니다.")
# print(type(answer))
# print(type(int(answer)))
# answer = 10
# print(type(answer))

"""
    8.2 표준 출력 시 유용한 기능
"""
"""
        8.2.1 구분자 넣기: sep
"""
# print("파이썬", "자바")
# print("파이썬", "자바", sep = ", ")

# print("파이썬", "자바", "자바스크립트")
# print("파이썬", "자바", "자바스크립트", sep = " vs ")

"""
        8.2.2 문장 끝 지정하기: end
"""
# print("파이썬", "자바", sep = ", ", end = "? ")
# print("무엇이 더 재미있을까요?")

"""
        8.2.3 출력 위치 지정하기: file
"""
# import sys

# print("파이썬", "자바", file = sys.stdout)
# print("파이썬", "자바", file = sys.stderr)

"""
        8.2.4 공간 확보해 정렬하기: ljust()와 rjust()
"""
# scores = {"수학": 0, "영어": 50, "코딩": 100}

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")

"""
        8.2.5 빈칸 0으로 채우기: zfill()
"""
# for num in range(1, 21):
#     # print("대기번호 :" + str(num).zfill(3))
#     print("대기번호 : " + str(num).rjust(3, "0"))

"""
    8.3 다양한 형식으로 출력하기: format()
"""
# print("{0: >+10}".format(500))
# print("{: >+10}".format(-500))

# print("{:_<10}".format(500))

# print(f"{1.2: .20f}")
# print(f"{0.1 + 1.1: .20f}")  
# print(f"{round(1.2, 1) == round(0.1 + 1.1, 1)}")

# print("{:_>+20,.20f}".format(100000000000)) # {인덱스:[[빈칸 채우기]정렬][기호][공간 확보][쉼표][.자릿수][자료형]}
# print("{:+,}".format(100000000000))
# print("{:+,}".format(-100000000000))

# print("{:^<+30,}".format(100000000000))

# print("{:.2f}".format(5 / 3))

"""
    8.4 파일 입출력
"""
"""
        8.4.1 파일 열고 닫기: open(), close()
"""
# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

"""
        8.4.2 파일 쓰기: write( )
"""
# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100\n")
# score_file.close()

"""
        8.4.3 파일 읽기: read( ), readline( ), readlines( )
"""
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# while True:
#     line = score_file.readline()
#     if not line: # 더 이상 읽어올 라인이 없으면 ""(False) 반환.
#         print(line, end="")
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")

# lines = score_file.readlines()
# # print(type(lines))
# for line in lines:
#     print(line, end="")
# score_file.close()

"""
    8.5 데이터를 파일로 저장하기: pickle 모듈
"""
# import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "스누피", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile, type(profile))

# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)

# print(profile, type(profile))
# profile_file.close()

"""
    8.6 파일 한 번에 열고 닫기: with 문
"""
# import pickle

# # with open("profile.pickle", "rb") as profile_file:
# #     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

"""
    8.7 실습 문제: 보고서 파일 만들기
"""
# for weekly in range(1, 51):
#     with open(str(weekly)+"주차.txt", "w", encoding="utf-8") as weekly_templete:
#         weekly_templete.write(f"# {weekly}주차.txt 파일 내용\n")
#         weekly_templete.write(f"- {weekly}주차 주간보고 -\n")
#         weekly_templete.write("부서 : \n")
#         weekly_templete.write("이름 : \n")
#         weekly_templete.write("업무 요약 : ")

# for weekly in range(1, 51):
#     with open(str(weekly)+"주차.txt", "r", encoding="utf-8") as weekly_templete:
#         for line in weekly_templete.readlines():
#             if not line:
#                 break
#             print(f"{line}", end="")
#         print(end="\n\n")

"""
    마무리
"""
with open("class.txt", "tw", encoding="utf-8") as class_file:
    class_file.write("초록반 5세 20명 파랑반 5세 18명 노랑반 7세 20명")

with open("class.txt", "tr", encoding="utf-8") as class_file:
    classes = class_file.read()

    for i in classes.split():
        if i.endswith("명"):
            print(i)
        else:
            print(i, end=" ")

