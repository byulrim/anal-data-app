"""
    9.5 부모 클래스 호출하기: super( )
"""
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)
        # super().__init__()

troopship = FlyableUnit()

"""
    1분 퀴즈
"""
class Noodle:
    def cook(self) -> None:
        print("끓는 물에 라면을 넣어요.")

class EggNoodle(Noodle):
    def cook(self) -> None:
        super().cook()
        print("계란을 넣어요.")

egg_noodle = EggNoodle()
egg_noodle.cook()