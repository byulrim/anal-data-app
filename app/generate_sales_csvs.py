import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# 설정: 재현 가능하도록 시드 고정
random.seed(42)
np.random.seed(42)

branches = [
    "광주광역시","대구광역시","대전광역시","부산광역시",
    "서울특별시","세종특별자치시","수원시","울산광역시","인천광역시","창원시"
]

# 공통 상품 목록 (제품코드, 제품명)
common_products = [
    ("P0001","아메리카노"),("P0002","카페라떼"),("P0003","카푸치노"),
    ("P0004","에스프레소"),("P0005","플랫화이트"),("P0006","아포가토"),
    ("P0007","바닐라라떼"),("P0008","카라멜마키아토"),("P0009","콜드브루"),
    ("P0010","모카")
]

# 각 지점별 특상품(지점 한정)
unique_products_by_branch = {
    "광주광역시":[("GJ100","광주떡라떼")],
    "대구광역시":[("DG100","대구핫팩커피")],
    "대전광역시":[("DJ100","대전밤라떼")],
    "부산광역시":[("BS100","부산씨앗라떼")],
    "서울특별시":[("SL100","한강블렌드")],
    "세종특별자치시":[("SJ100","세종허브티")],
    "수원시":[("SW100","수원왕갈비라떼")],
    "울산광역시":[("US100","울산포항혼합")],
    "인천광역시":[("IC100","인천바다라떼")],
    "창원시":[("CW100","창원딸기프라푸치노")]
}

# 제품별 고정 단가 맵 (모든 지점에서 동일하게 적용)
# 기본 공통제품은 대략적 평균가로 설정, 특상품은 좀 더 높게 설정
product_price_map = {
    "P0001": 4500,
    "P0002": 5200,
    "P0003": 4800,
    "P0004": 3000,
    "P0005": 5600,
    "P0006": 7500,
    "P0007": 5800,
    "P0008": 6500,
    "P0009": 7000,
    "P0010": 6200,
    "GJ100": 9800,
    "DG100": 9200,
    "DJ100": 8800,
    "BS100": 9400,
    "SL100": 10500,
    "SJ100": 7600,
    "SW100": 12000,
    "US100": 9000,
    "IC100": 9600,
    "CW100": 8200
}

# 판매수량 분포 정의: -5..20 (반품 포함)
def _qty_prob():
    probs = []
    for v in range(-5, 21):
        if v < 0:
            probs.append(0.006)  # 반품 소수
        elif v == 0:
            probs.append(0.07)
        elif 1 <= v <= 5:
            probs.append(0.12)
        elif 6 <= v <= 10:
            probs.append(0.06)
        else:
            probs.append(0.01)
    arr = np.array(probs)
    arr = arr / arr.sum()
    return arr

# 데이터 생성 함수
def generate_branch_data(branch_name, n_rows=100, start_date="2025-11-01", days_range=30):
    rows = []
    start = datetime.strptime(start_date, "%Y-%m-%d")
    products = common_products + unique_products_by_branch.get(branch_name, [])
    qty_probs = _qty_prob()
    qty_values = np.arange(-5, 21)
    for i in range(n_rows):
        # 날짜 랜덤 선택
        d = start + timedelta(days=random.randint(0, days_range-1))
        sale_date = d.strftime("%Y-%m-%d")
        prod_code, prod_name = random.choice(products)
        # 판매수량 샘플링
        qty = int(np.random.choice(qty_values, p=qty_probs))
        # 제품별 고정 단가 사용 (맵에 없으면 기본 가격 사용)
        unit_price = product_price_map.get(prod_code, random.randint(3000, 8000))
        amount = qty * unit_price
        rows.append({
            "판매일자": sale_date,
            "제품코드": prod_code,
            "제품명": prod_name,
            "판매수량": qty,
            "제품단가": unit_price,
            "판매금액": amount,
            "지점명": branch_name
        })
    df = pd.DataFrame(rows)
    return df

# 메인: 각 지점별 파일 생성
def main():
    out_dir = "sales_csvs"
    os.makedirs(out_dir, exist_ok=True)
    for b in branches:
        df = generate_branch_data(b, n_rows=100, start_date="2025-11-01", days_range=30)
        filename = f"{b}.csv"
        path = os.path.join(out_dir, filename)
        df.to_csv(path, index=False, encoding="utf-8-sig")
        print(f"생성: {path} ({len(df)} rows)")
    print("모든 파일 생성 완료!")

if __name__ == "__main__":
    main()