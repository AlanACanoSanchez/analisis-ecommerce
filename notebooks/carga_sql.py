import pandas as pd
import pyodbc
# print(pyodbc.drivers())


# Leer el archivo limpio
df = pd.read_csv('../data/online_retail_clean.csv')

# Conexión a SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=ecommerce_db;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Cargar datos a la tabla
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO ventas_ecommerce (
            InvoiceNo, StockCode, Description, Quantity,
            InvoiceDate, UnitPrice, CustomerID, Country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    row['InvoiceNo'], row['StockCode'], row['Description'], int(row['Quantity']),
    row['InvoiceDate'], float(row['UnitPrice']), int(row['CustomerID']), row['Country'])

    if index % 1000 == 0:
        print(f"Insertadas {index} filas...")
        conn.commit()

# Confirmar y cerrar
conn.commit()
cursor.close()
conn.close()

print("✅ Carga completada.")
