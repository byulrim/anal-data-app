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
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛을 생성했습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 160, 35)

