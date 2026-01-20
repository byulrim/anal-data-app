def say_hello(to: str)-> None:
    print(f"안녕, {to}?")

def say_goodbye(to: str) -> None:
    print(f"또 만나, {to}!")

if __name__ == "__main__":
    say_hello("파이썬")
    say_goodbye("나도코딩")
