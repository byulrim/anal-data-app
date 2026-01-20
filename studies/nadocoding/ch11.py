"""
11장 모듈과 패키지
"""
"""
    11.1 모듈 다루기
"""
"""
        11.1.1 모듈 만들기
"""
# theater_module.py 참조

"""
        11.1.2 모듈 사용하기
"""
# import theater_module as tm

# tm.price(3)
# tm.price_morning(4)
# tm.price_soldier(5)

# from theater_module import price, price_morning, price_soldier

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price_soldier as price

# price(5)

"""
    11.2 패키지 다루기
"""
""" 
        11.2.1 패키지 만들기
"""
# ..\travel\__init__.py, thailand.py, vietnam.py 참조

"""
        11.2.2 패키지 사용하기            
"""
# import travel.thailand as tt
# from travel.thailand import ThailandPackage as tt

# trip_to = tt()
# trip_to.detail()

# from travel import vietnam

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

"""
    11.3 모듈 공개 설정하기: __all__        
"""
# __init__.py 참조

# from travel import *

# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

"""
    11.4 모듈 직접 실행하기
"""
"""
    11.5 패키지와 모듈 위치 확인하기
"""
# import inspect
# import random
# from travel import *
# import pandas

# # print(inspect.getfile(random))
# print(inspect.getfile(thailand))
# # print(inspect.getfile(pandas))

"""
    11.6 패키지 설치하기
"""
# from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

"""
    11.7 내장 함수 사용하기
"""
# language = input("어떤 언어를 좋아하세요? ")
# print(f"{language}은/는 아주 좋은 언어입니다!")

# import random

# for lst in dir(random):
#     print(lst)

# lst = [1, 2, 3]
# for item in dir(lst):
#     print(item)

# name = "Jim"
# for lst in dir(name):
#     print(lst)

# import pickle
# for lst in dir(pickle):
#     print(lst)

"""
    11.8 외장 함수 사용하기
"""
"""
        11.8.1 폴더 또는 파일 목록 조회 모듈
"""
# from glob import glob

# path_name = ".\\studies\\nadocoding\\"
# file_name = "*.py"

# file_list = glob(path_name + file_name)
# for lst in file_list:
#     print(lst)

"""
        11.8.2 운영체제의 기본 기능 모듈
"""
# import os

# # func_list = dir(os)
# # for lst in func_list:
# #     print(lst)

# # print(os.getcwd())
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("폴더가 이미 존재합니다.")
#     os.rmdir(folder)
#     print(f"폴더 {folder}을/를 삭제했습니다.")
# else:
#     os.makedirs(folder)
#     print(f"폴더 {folder}을/를 생성했습니다.")

# print(os.listdir())

"""
        11.8.3 시간 관련 모듈
"""
# import time

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime

# print("오늘 날짜는", datetime.date.today())

# # for lst in dir(datetime.datetime):
# #     print(lst)

# today = datetime.date.today()
# delta = datetime.timedelta(days=100)
# print(delta)
# print(f"우리가 만난 지 100일째 되는 날은 {today + delta}일")

"""
    11.9 실습 문제: 나만의 모듈 만들기
"""
import byme

byme.sign()

"""
    마무리
"""
