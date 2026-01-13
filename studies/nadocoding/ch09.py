"""
9장 클래스
"""
"""
    9.1 게임소개
"""
# name = "보병"
# hp = 40
# damage = 5

# print(f"{name} 유닛을 생성했습니다.")
# print(f"체력 {hp}, 공격력 {damage}\n")

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print(f"{tank_name} 유닛을 생성했습니다.")
# print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print(f"{tank2_name} 유닛을 생성했습니다.")
# print(f"체력 {tank2_hp}, 공격력 {tank2_damage}\n")


# def attack(name, location, damage):
#     print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

"""
    9.2 클래스와 객체 생성하기
"""
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name} 유닛을 생성했습니다.")
#         print(f"체력 {self.hp}, 공격력 {self.damage}")

# soldier1 = Unit("보병", 40, 5)
# soldier2 = Unit("보병", 40, 5)
# tank = Unit("탱크", 160, 35)

"""
        9.2.1 생성자: __init__( )
"""
# soldier3 = Unit("보병")
# soldier3 = Unit("보병", 40)

"""
        9.2.2 인스턴스 변수
"""
# stealth1 = Unit("전투기", 80, 5)
# print("유닛 이름 : {}, 공격력 : {}".format(stealth1.name, stealth1.damage))
# # stealth1.clocking = True

# stealth2 = Unit("업그레이드한 전투기", 80, 5)
# stealth2.clocking = True

# if stealth2.clocking == True:
#     print("{}는 현재 은폐 상태입니다.".format(stealth2.name))

# # if stealth1.clocking == True:
# #     print("{}는 현재 은폐 상태입니다.".format(stealth1.name))

"""
        9.2.3 메서드
"""
# class AttackUnit:
#     def __init__(self, name: str, hp: int, damage:int):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location: str) -> None:
#         print("{} : {} 방향 적군을 공격합니다. [공격력 {}]" \
#               .format(self.name, location, self.damage))

#     def damaged(self, damage: int) -> None:
#         print(f"{self.name} : {damage}만큼 피해를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp}입니다.")
#         if self.hp <= 0:
#             print(f"{self.name} : 파괴됐습니다.")

# flameThrower1 = AttackUnit("화염방사병", 50, 16)
# flameThrower1.attack("5시")

# flameThrower1.damaged(25)
# flameThrower1.damaged(25)

"""
    9.3 클래스 상속(인헤리턴스)하기
"""
"""
        9.3.1 상속이란
"""
# class Unit:
#     def __init__(self, name: str, hp: int) -> None:
#         self.name = name
#         self.hp = hp
class Unit:
    def __init__(self, name: str, hp: int, speed: int) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location: str) -> None:
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
              .format(self.name, location, self.speed))
class AttackUnit(Unit):
    # def __init__(self, damage, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def __init__(self, name: str, hp: int, damage: int, speed: int) -> None:        
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location: str) -> None:
        print("{} : {} 방향 적군을 공격합니다. [공격력 {}]" \
              .format(self.name, location, self.damage))

    def damaged(self, damage: int) -> None:
        print(f"{self.name} : {damage}만큼 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴됐습니다.")

# flameThrower1 = AttackUnit("화염방사병", 50, 16, 1)
# flameThrower1.attack("5시")

# flameThrower1.damaged(25)
# flameThrower1.damaged(25)

"""
        9.3.2 다중 상속
"""
class Flyable:
    def __init__(self, flying_speed: int) -> None:
        self.flying_speed = flying_speed

    def fly(self, name: str, location: str) -> None:
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
              .format(name, location, self.flying_speed))
        
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name: str, hp: int, damage: int, flying_speed: int) -> None:
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# interceptor = FlyableAttackUnit("요격기", 200, 6, 5)
# interceptor.fly(interceptor.name, "3시")

"""
        9.3.3 메서드 오버라이딩
"""        
# hoverbike = AttackUnit("호버 바이크", 80, 20, 10)
# hoverbike.move("11시")

# spacecruiser = FlyableAttackUnit("우주 순양함", 500, 25, 3)
# spacecruiser.move("9시")

"""
    9.4 동작 없이 일단 넘어가기: pass
    ("인덴테이션(indentation)이 필요한 곳에서는 모두 사용 가능"하다고 젬미니가 알려줬음)
"""
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("보급고", 500, "7시")
# print(supply_depot.name)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()