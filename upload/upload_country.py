import pandas as pd
import mysql.connector

# đọc file csv
file_path = r"C:\Users\ASUS\Downloads\Market-Basket-Analysis--main\Market-Basket-Analysis--main\Assignment-1_after_clean.csv"

df = pd.read_csv(file_path)

# lấy danh sách country không trùng
countries = df["Country"].dropna().unique()

# kết nối mysql
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="kunmuradstsv12",
    database="retail_project"
)

cursor = conn.cursor()

# insert country
for country in countries:
    cursor.execute(
        "INSERT INTO Country (country_name) VALUES (%s)",
        (country,)
    )

conn.commit()

print("Inserted", len(countries), "countries")

cursor.close()
conn.close()