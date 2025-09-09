# Mini Project -ETL pipeline Excel to SQLite

This is a simple **ETL (Extract–Transform–Load) pipeline** built with Python, Pandas, and SQLite.  
The project demonstrates how to:
- Extract data from Excel file
- Transform data (cleaning, aggregation)
- Load structured data into a relational database
- Run SQL queries on the processed data

## 🚀 Project Workflow
1. **Extract**  
   - Reads sales data from ``sales_data.xlsx` 

2. **Transform**  
   - Calculates total sales per order (`quantity × price`)
   - Summarizes sales by product.  

3. **Load**  
   - Stores raw and transformed data into a SQLite database (`sales.db`).  

4. **Query**  
   - Runs SQL queries to fetch insights (e.g., top-selling products).  

---

