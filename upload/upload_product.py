import pandas as pd
import mysql.connector

# đọc csv
file_path = r"C:\Users\ASUS\Downloads\Market-Basket-Analysis--main\Market-Basket-Analysis--main\Assignment-1_after_clean.csv"

df = pd.read_csv(file_path)

# lấy item unique
items = df["Itemname"].dropna().unique()

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="kunmuradstsv12",
    database="retail_project"
)

cursor = conn.cursor()

for item in items:
    cursor.execute(
        "INSERT IGNORE INTO Product (item_name) VALUES (%s)",
        (item,)
    )

conn.commit()

print("Inserted items:", len(items))

cursor.close()
conn.close()