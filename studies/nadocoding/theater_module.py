"""
        11.1.1 모듈 만들기
"""
def price(people):
    print(f"{people}명, 영화표 가격은 {people * 10000}원입니다.")

def price_morning(people):
    print(f"{people}명, 조조 할인 영화표 가격은 {people * 6000}원입니다.")

def price_soldier(people):
    print(f"{people}명, 군인 할인 영화표 가격은 {people * 4000}원입니다.")
