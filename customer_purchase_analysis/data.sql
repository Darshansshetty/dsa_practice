CREATE TABLE sales_data (
    CustomerName VARCHAR(50),
    Region VARCHAR(20),
    Category VARCHAR(30),
    Sales NUMERIC,
    Profit NUMERIC(10,2)
);

INSERT INTO sales_data VALUES
('Alice', 'East', 'Furniture', 500, 120),
('Bob', 'West', 'Technology', 900, 200),
('Carol', 'East', 'Office Supplies', 300, 50),
('David', 'South', 'Furniture', 700, 100),
('Eve', 'North', 'Technology', 400, 90);

SELECT * FROM sales_data
