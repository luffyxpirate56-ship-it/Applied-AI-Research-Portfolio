-- ==============================================================================
-- SQL Data Cleaning & Aggregation Script
-- Author: Yuvraj Singh, PhD
-- Description: Queries used to extract, clean, and transform raw multi-platform 
-- database records into a structured format for dashboard visualization.
-- ==============================================================================

-- 1. Create a cleaned view of the sales table, filtering out anomalies
CREATE OR REPLACE VIEW cleaned_sales_data AS
SELECT 
    order_id,
    customer_id,
    platform,
    order_date,
    CAST(revenue AS DECIMAL(10,2)) as revenue,
    TRIM(UPPER(status)) as delivery_status
FROM 
    raw_sales_transactions
WHERE 
    revenue > 0 
    AND status NOT IN ('CANCELLED', 'RETURNED');

-- 2. Aggregate data to identify top revenue channels by month
SELECT 
    EXTRACT(MONTH FROM order_date) as sales_month,
    platform,
    SUM(revenue) as total_revenue,
    COUNT(order_id) as total_orders
FROM 
    cleaned_sales_data
GROUP BY 
    EXTRACT(MONTH FROM order_date),
    platform
ORDER BY 
    sales_month DESC, 
    total_revenue DESC;