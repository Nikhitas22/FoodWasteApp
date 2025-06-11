import psycopg2
import pandas as pd

# PostgreSQL DB connection
def get_connection():
    return psycopg2.connect(
        dbname="foodmws",
        user="postgres",
        password="Nikhita@22",  # 🔁 Replace with your real password
        host="localhost",
        port="5432"
    )

# For INSERT, UPDATE, DELETE operations (no return expected)
def run_query(query, params=None):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params or ())
                conn.commit()
    except Exception as e:
        print("❌ Error executing query:", e)

# For SELECT operations (returns DataFrame)
def fetch_query(query, params=None):
    try:
        with get_connection() as conn:
            return pd.read_sql_query(query, conn, params=params)
    except Exception as e:
        print("❌ Error fetching data:", e)
        return pd.DataFrame()
