import pandas as pd
import mysql.connector

file_path = r"C:\Users\ASUS\Downloads\Market-Basket-Analysis--main\Market-Basket-Analysis--main\Assignment-1_after_clean.csv"

df = pd.read_csv(file_path)

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="kunmuradstsv12",
    database="retail_project"
)

cursor = conn.cursor()

for _, row in df.iterrows():

    # lấy product_id từ bảng Product
    cursor.execute(
        "SELECT product_id FROM Product WHERE item_name=%s",
        (row["Itemname"],)
    )

    result = cursor.fetchone()

    if result:
        product_id = result[0]

        cursor.execute(
            """
            INSERT INTO InvoiceDetail
            (bill_no, product_id, quantity, price, revenue)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                row["BillNo"],
                product_id,
                int(row["Quantity"]),
                float(row["Price"]),
                float(row["Revenue"])
            )
        )

conn.commit()

print("Inserted invoice details")

cursor.close()
conn.close()