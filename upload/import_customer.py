import pandas as pd
import mysql.connector

# đọc csv
file_path = r"C:\Users\ASUS\Downloads\Market-Basket-Analysis--main\Market-Basket-Analysis--main\Assignment-1_after_clean.csv"

df = pd.read_csv(file_path)

# lấy customer unique
customers = df[["CustomerID","Country"]].drop_duplicates()

# connect mysql
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="kunmuradstsv12",
    database="retail_project"
)

cursor = conn.cursor()

for _, row in customers.iterrows():

    customer_id = int(row["CustomerID"])
    country_name = row["Country"]

    # lấy country_id
    cursor.execute(
        "SELECT country_id FROM Country WHERE country_name=%s",
        (country_name,)
    )

    result = cursor.fetchone()

    if result:
        country_id = result[0]

        cursor.execute(
            "INSERT IGNORE INTO Customer (customer_id,country_id) VALUES (%s,%s)",
            (customer_id, country_id)
        )

conn.commit()

print("Inserted customers:", len(customers))

cursor.close()
conn.close()