# app/db_test.py
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text

url = URL.create(
    "postgresql+psycopg2",
    username="anal_data_user",
    password="Antigone12!@",
    host="127.0.0.1",
    port="5432",
    database="anal_data_db"
)

engine = create_engine(url, future=True)

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            row = result.fetchone()
            print("테스트 쿼리 결과:", row)
            return row
    except Exception as e:
        print("DB 연결/쿼리 중 오류 발생:")
        raise

if __name__ == "__main__":
    test_connection()