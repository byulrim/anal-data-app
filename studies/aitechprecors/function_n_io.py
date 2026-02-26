def calculate_rectangle_area(x: float, y: float) -> float:
    result = float(x * y)
    return result


rectangle_x = 10
rectangle_y = 20
result = calculate_rectangle_area(x=rectangle_x, y=rectangle_y)
print(f"사각형 x의 길이: {rectangle_x}")
print(f"사각형 y의 길이: {rectangle_y}")
print(f"사각형의 넓이: {result}({type(result)})")


def f(x:int) -> int:
    return 2 * x + 7


def g(x:int) -> int:
    return x ** 2


x = 2
print(f"{f(x) + g(x) + f(g(x)) + g(f(x))}")

def test_function(text: str) -> None:
    print(f"\"{text}\"를 입력하셨습니다.")


result = test_function("안녕하세요!")
print(result)


temp = float(input("온도를 입력하세요: "))
print(f"온도는 {temp}도 입니다.")
print(type(temp))