import pandas as pd
import mysql.connector

file_path = r"C:\Users\ASUS\Downloads\Market-Basket-Analysis--main\Market-Basket-Analysis--main\Assignment-1_after_clean.csv"

df = pd.read_csv(file_path)

# chỉ lấy 1 dòng cho mỗi BillNo
invoices = df[["BillNo","CustomerID","Date"]].drop_duplicates(subset=["BillNo"])

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="kunmuradstsv12",
    database="retail_project"
)

cursor = conn.cursor()

for _, row in invoices.iterrows():
    cursor.execute(
        "INSERT IGNORE INTO Invoice (bill_no, customer_id, invoice_date) VALUES (%s,%s,%s)",
        (row["BillNo"], int(row["CustomerID"]), row["Date"])
    )

conn.commit()

print("Inserted invoices:", len(invoices))

cursor.close()
conn.close()