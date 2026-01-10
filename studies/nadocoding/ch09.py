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
class Unit:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name: str, hp: int, damage: int):
        Unit.__init__(self, name, hp)
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

flameThrower1 = AttackUnit("화염방사병", 50, 16)
flameThrower1.attack("5시")

flameThrower1.damaged(25)
flameThrower1.damaged(25)

"""
        9.3.2 다중 상속
"""
