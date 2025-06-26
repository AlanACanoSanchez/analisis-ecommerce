# 📁 Carpeta `data/`

Esta carpeta contiene los archivos de datos utilizados en el proyecto **Análisis de Ventas E-commerce (2010–2011)**.

## Archivos

### `online_retail.csv`
- 📥 **Fuente original de datos**.
- Contiene los datos crudos de transacciones del e-commerce.
- Incluye columnas como:
  - `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.

### `online_retail_clean.csv`
- 🧼 **Versión depurada del dataset**.
- Se eliminaron:
  - Transacciones anuladas o vacías.
  - Registros con datos faltantes.
  - Valores no válidos (ej. precios negativos, cantidades inválidas).
- Este archivo fue el que se usó para cargar en la base de datos SQL Server.

## Notas
- Todos los datos provienen del dataset público de UCI Machine Learning Repository.
- Fecha de las transacciones: **diciembre 2010 a diciembre 2011**.

