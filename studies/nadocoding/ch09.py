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
        print(f"{self.name} 유닛을 생성했습니다.")
    
    def move(self, location: str) -> None:
        # print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage: int) -> None:
        print(f"{self.name} : {damage}만큼 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴됐습니다.")

class AttackUnit(Unit):
    def __init__(self, name: str, hp: int, damage: int, speed: int) -> None:        
        super().__init__(name, hp, speed)
        self.damage = damage

    def attack(self, location: str) -> None:
        print(f"{self.name} : {location} 방향 적군을 공격합니다. [공격력 {self.damage}]")


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
        # print("[공중 유닛 이동]")
        super().fly(self.name, location)

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
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# supply_depot = BuildingUnit("보급고", 500, "7시")
# print(supply_depot.name, supply_depot.hp, supply_depot.location)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

# game_start()
# game_over()

"""
    9.5 부모 클래스 호출하기: super( )
"""
# super.py 파일 참조

"""
    9.6 게임 완성
"""
""" 
        9.6.1 게임 준비하기
"""
class Soldier(AttackUnit):
    def __init__(self):
        super().__init__("보병", 40, 5, 1)

    def booster(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 강화제를 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족해 강화제를 사용할 수 없습니다.")

class Tank(AttackUnit):
    siege_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 35, 1)
        self.siege_mode = False

    def set_siege_mode(self):
        if Tank.siege_developed == False:
            return
        if self.siege_mode == False:
            print(f"{self.name} : 시지 모드로 전환합니다.")
            self.damage *= 2
            self.siege_mode = True
        else:
            print(f"{self.name} : 시지 모드를 해제합니다.")
            self.damage /= 2
            self.siege_mode = False

class Stealth(FlyableAttackUnit):
    def __init__(self):
        super().__init__("전투기", 80, 20, 5)
        self.cloaked = False

    def cloaking(self):
        if self.cloaked == True:
            print(f"{self.name} : 은폐 모드를 해제합니다.")
            self.cloaked = False
        else:
            print(f"{self.name} : 은폐 모드를 설정합니다.")
            self.cloaked = True

""" 
        9.6.2 게임 실행하기
"""
game_start()

so1 = Soldier()
so2 = Soldier()
so3 = Soldier()

ta1 = Tank()
ta2 = Tank()

st1 = Stealth()

attack_units = []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

for unit in attack_units:
    unit.move("1시")

Tank.siege_developed = True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")

for unit in attack_units:
    if isinstance(unit, Soldier):
        unit.booster()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Stealth):
        unit.cloaking()

from random import randint

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()

""" 
    9.8 실습 문제: 부동산 프로그램 만들기
"""
class House:
    
    def __init__(self, location: str, house_type: str, deal_type: str, price: str, completion_year: str) -> None:
        self.locattion = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self) -> None:
        print(f"{self.locattion} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

houses = []
house1 = House("강남", "아파트", "매매", "10억 원", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
house3 = House("송파", "빌라", "월세", "500/50만 원", "2000년")

for i in range(1, 4):
    houses.append(eval("house" + str(i)))

print(f"총 {len(houses)}가지 매물이 있습니다.")
for house in houses:
    house.show_detail()

"""
    마무리
"""
class ParkingManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f"총 {self.capacity}대를 등록할 수 있습니다.")

    def register(self):
        if self.count >= self.capacity:
            print("더 이상 등록할 수 없습니다.")
            return
        # else:
        self.count += 1
        print(f"차량 신규 등록 ({self.count}/{self.capacity})")

manager = ParkingManager(5)
for i in range(6):
    print(f"{i + 1: >5}:", end = " ")
    manager.register()
    