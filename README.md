# **Retail Sales Analysis and Insights Using SQL**

## **Project Overview**
This project focuses on analyzing retail sales data to extract valuable business insights using SQL. The analysis helps identify top-selling products, revenue trends, month-over-month growth, and profit growth across different product categories and regions. The results can be used to optimize sales strategies, inventory management, and overall business performance.

## **Dataset**
The dataset used in this project is sourced from Kaggle:
- **Dataset Name:** Retail Orders Dataset
- **File:** `orders.csv`
- **Source:** [Kaggle Dataset](https://www.kaggle.com/retail-orders)

## **Installation**
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/retail-sales-analysis.git
   cd retail-sales-analysis
   ```

2. **Install the required libraries:**
   Install the required Python libraries using `pip`:
   ```bash
   pip install pandas sqlalchemy pyodbc kaggle
   ```

3. **Download the dataset:**
   Download the retail orders dataset from Kaggle:
   ```bash
   kaggle datasets download ankitbansal06/retail-orders -f orders.csv
   ```

4. **Extract the dataset:**
   ```python
   import zipfile
   zip_ref = zipfile.ZipFile('orders.csv.zip') 
   zip_ref.extractall() 
   zip_ref.close()
   ```

## **Data Preprocessing**
1. **Load and Clean the Data:**
   - Load the dataset using Pandas.
   - Handle null values.
   - Rename columns for consistency (lowercase and underscores).

2. **Derive New Columns:**
   - Calculate `profit` based on `sale_price` and `cost_price`.
   - Convert `order_date` to datetime format.

3. **Drop Unnecessary Columns:**
   - Drop columns like `list_price`, `cost_price`, and `discount_percent` that are no longer needed after calculations.

## **Analysis**
The SQL scripts in this project perform the following analyses:

1. **Top 10 Highest Revenue-Generating Products:**
   - Identifies the products that generate the most revenue.

2. **Top 5 Highest-Selling Products by Region:**
   - Finds the top 5 selling products in each region.

3. **Month-over-Month Sales Growth Comparison (2022 vs. 2023):**
   - Compares sales growth month by month between the years 2022 and 2023.

4. **Best Performing Month for Each Category:**
   - Identifies the month with the highest sales for each product category.

5. **Sub-Category Profit Growth (2022 vs. 2023):**
   - Determines which sub-category saw the highest profit growth in 2023 compared to 2022.

## **Results**
The analysis provides actionable insights such as:
- Identification of high-revenue products and top-selling items by region.
- Comparison of sales performance across different time periods.
- Insights into peak sales months for various categories.
- Detection of sub-categories with significant profit growth.

## **Technologies Used**
- **Python:** Pandas, SQLAlchemy, pyodbc for data processing and database interaction.
- **SQL:** Core language for performing data analysis.
- **SQL Server:** Database used for storing and querying the data.
- **Kaggle:** Data source for the retail orders dataset.

## **Usage**
1. **Running the Analysis:**
   - Load the dataset into SQL Server.
   - Run the provided SQL scripts to perform the analysis and generate insights.

2. **Connecting to SQL Server:**
   - Ensure you have a SQL Server instance running.
   - Update the connection string in the script to point to your SQL Server instance.

3. **Viewing Results:**
   - Query the SQL Server database to view the results of the analysis.

## **Contributing**
Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.
