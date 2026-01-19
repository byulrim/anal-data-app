"""
10 예외 처리
"""
"""
    10.1 예외 처리하기
"""
"""
        10.1.1 예외 처리란
"""
"""
        10.1.2 예외 처리하기: try-except 문
"""
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print(f"{nums[0]} / {nums[1]} = {nums[2]}")
# except ValueError:
#     print("오류 발생! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 오류가 발생했습니다.")
#     print(err)

"""
        10.1.3 오류 메시지를 예외 처리로 출력하기: as
"""
"""
    10.2 오류 발생시키기(raise)
"""
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print(f"{num1} / {num2} = {int(num1 / num2)}")
# except ValueError:
#     print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

"""
    10.3 사용자 정의 예외 처리하기
"""
"""
    10.4 오류와 상관없이 무조건 샐행하기: finally
"""
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return "[오류 코드 001] " + self.msg
    
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")