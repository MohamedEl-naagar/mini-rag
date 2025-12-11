# import psycopg2

# try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="postgres",  # Replace with your database name
#             user="postgres",          # Replace with your PostgreSQL username
#             password="root"       # Replace with your PostgreSQL password
#         )
#         print("Connected to PostgreSQL successfully!")

#         # You can now perform database operations using the 'conn' object

# except psycopg2.Error as e:
#         print(f"Error connecting to PostgreSQL: {e}")

# finally:
#         if 'conn' in locals() and conn:
#             conn.close()
#             print("Connection closed.")

from fastapi import FastAPI
from routes import base
from dotenv import load_dotenv
load_dotenv(".env")
app = FastAPI()

app.include_router(base.base_router)