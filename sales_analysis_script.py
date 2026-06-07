"""
Data Pipeline & Synthesis for Vrinda Store
Author: Yuvraj Singh, PhD
Description: Automated data cleaning and analysis workflow to identify 
top revenue channels. Demonstrates data curation capabilities.
"""

import pandas as pd

def analyze_sales_data():
    # Simulated raw data extraction (represents multi-platform data)
    data = {
        'Order_ID': [101, 102, 103, 104, 105],
        'Platform': ['Amazon', 'Flipkart', 'Direct', 'Amazon', 'Direct'],
        'Revenue': [1200, 850, 2100, 1500, 3000],
        'Status': ['Delivered', 'Returned', 'Delivered', 'Delivered', 'Delivered']
    }
    
    df = pd.DataFrame(data)
    
    print("--- Raw Data Sample ---")
    print(df)
    
    # Data Cleaning: Remove returned items
    cleaned_df = df[df['Status'] == 'Delivered'].copy()
    
    # Aggregation: Group by platform to find top channels
    revenue_by_platform = cleaned_df.groupby('Platform')['Revenue'].sum().reset_index()
    revenue_by_platform = revenue_by_platform.sort_values(by='Revenue', ascending=False)
    
    print("\n--- Processed Dashboard Output ---")
    print("Top Revenue Channels Identified:")
    print(revenue_by_platform)
    
    return revenue_by_platform

if __name__ == "__main__":
    analyze_sales_data()