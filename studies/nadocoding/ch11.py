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
from travel.thailand import ThailandPackage as tt

trip_to = tt()
trip_to.detail()

from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()

"""
        11.3 모듈 공개 설정하기: __all__        
"""
