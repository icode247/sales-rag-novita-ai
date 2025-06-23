#!/usr/bin/env python3
"""
Advanced Data Generator for Retail Sales Database
Generates large amounts of realistic test data for the chatbot system
"""

import pandas as pd
from datetime import datetime, timedelta
import random
import os

class RetailDataGenerator:
    def __init__(self, output_folder="sample_documents"):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)
        
        # Sample data pools
        self.first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 
                           'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
                           'Thomas', 'Sarah', 'Christopher', 'Karen', 'Charles', 'Nancy', 'Daniel', 'Lisa',
                           'Matthew', 'Betty', 'Anthony', 'Helen', 'Mark', 'Sandra', 'Donald', 'Donna']
        
        self.last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                          'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
                          'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson',
                          'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker']
        
        self.cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 
                      'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
                      'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Seattle',
                      'Denver', 'Washington', 'Boston', 'El Paso', 'Detroit', 'Nashville', 'Portland',
                      'Memphis', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee']
        
        self.states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'FL', 'OH', 'NC', 'WA', 'CO', 'DC', 'MA',
                      'MI', 'TN', 'OR', 'KY', 'MD', 'WI', 'NV', 'LA', 'OK', 'KS', 'MN', 'GA', 'UT',
                      'AL', 'SC', 'IA', 'CT', 'AR', 'MS', 'ND', 'SD', 'DE', 'MT', 'ID', 'WY', 'AK', 'HI']
        
        self.product_categories = {
            'Electronics': ['Smartphones', 'Laptops', 'Tablets', 'Audio', 'Gaming', 'Smart Home'],
            'Fashion': ['Clothing', 'Footwear', 'Accessories', 'Jewelry', 'Bags'],
            'Home & Garden': ['Furniture', 'Decor', 'Kitchen', 'Tools', 'Cleaning', 'Security'],
            'Sports & Outdoors': ['Exercise', 'Team Sports', 'Outdoor Recreation', 'Winter Sports'],
            'Beauty & Health': ['Skincare', 'Makeup', 'Hair Care', 'Supplements', 'Medical'],
            'Books & Media': ['Fiction', 'Non-fiction', 'Educational', 'Comics', 'Music', 'Movies']
        }
        
        self.brands = ['Apple', 'Samsung', 'Sony', 'Microsoft', 'Google', 'Amazon', 'Nike', 'Adidas',
                      'HP', 'Dell', 'Canon', 'Nikon', 'LG', 'Panasonic', 'Bose', 'JBL', 'Razer',
                      'Logitech', 'Corsair', 'ASUS', 'Lenovo', 'Acer', 'Fitbit', 'Garmin']

    def generate_large_sales_csv(self, num_records=10000):
        """Generate a large sales dataset as CSV"""
        print(f"Generating {num_records} sales records...")
        
        sales_data = []
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2024, 12, 31)
        
        for i in range(num_records):
            # Generate random date
            random_days = random.randint(0, (end_date - start_date).days)
            sale_date = start_date + timedelta(days=random_days)
            
            # Generate sales record
            record = {
                'sale_id': i + 1,
                'customer_id': random.randint(1, 1000),
                'customer_name': f"{random.choice(self.first_names)} {random.choice(self.last_names)}",
                'product_name': self.generate_product_name(),
                'category': random.choice(list(self.product_categories.keys())),
                'brand': random.choice(self.brands),
                'quantity': random.randint(1, 10),
                'unit_price': round(random.uniform(10, 2000), 2),
                'total_amount': 0,  # Will calculate after
                'discount_percent': random.choice([0, 5, 10, 15, 20, 25]),
                'payment_method': random.choice(['Credit Card', 'Debit Card', 'Cash', 'PayPal', 'Bank Transfer']),
                'sales_rep': random.choice(['Alice Johnson', 'Bob Smith', 'Carol Davis', 'Dave Wilson', 'Eve Brown']),
                'store_location': random.choice(['New York Store', 'Los Angeles Store', 'Chicago Store', 'Houston Store', 'Miami Store']),
                'sale_date': sale_date.strftime('%Y-%m-%d'),
                'customer_city': random.choice(self.cities),
                'customer_state': random.choice(self.states),
                'rating': random.randint(1, 5),
                'review_text': self.generate_review(),
                'season': self.get_season(sale_date.month)
            }
            
            # Calculate total amount with discount
            subtotal = record['quantity'] * record['unit_price']
            discount_amount = subtotal * (record['discount_percent'] / 100)
            record['total_amount'] = round(subtotal - discount_amount, 2)
            
            sales_data.append(record)
        
        # Create DataFrame and save
        df = pd.DataFrame(sales_data)
        csv_path = os.path.join(self.output_folder, 'large_sales_dataset.csv')
        df.to_csv(csv_path, index=False)
        print(f"Large sales dataset saved to: {csv_path}")
        return df

    def generate_customer_analysis_csv(self, num_customers=2000):
        """Generate customer analysis dataset"""
        print(f"Generating {num_customers} customer records...")
        
        customers = []
        for i in range(num_customers):
            registration_date = datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1460))
            last_purchase = registration_date + timedelta(days=random.randint(1, 365))
            
            customer = {
                'customer_id': i + 1,
                'first_name': random.choice(self.first_names),
                'last_name': random.choice(self.last_names),
                'email': f"customer{i+1}@email.com",
                'age': random.randint(18, 80),
                'gender': random.choice(['Male', 'Female', 'Other']),
                'city': random.choice(self.cities),
                'state': random.choice(self.states),
                'customer_type': random.choice(['Regular', 'Premium', 'VIP']),
                'registration_date': registration_date.strftime('%Y-%m-%d'),
                'last_purchase_date': last_purchase.strftime('%Y-%m-%d'),
                'total_orders': random.randint(1, 50),
                'total_spent': round(random.uniform(50, 5000), 2),
                'average_order_value': 0,  # Will calculate
                'preferred_category': random.choice(list(self.product_categories.keys())),
                'loyalty_points': random.randint(0, 10000),
                'marketing_consent': random.choice([True, False]),
                'customer_lifetime_value': round(random.uniform(100, 10000), 2)
            }
            
            # Calculate average order value
            if customer['total_orders'] > 0:
                customer['average_order_value'] = round(customer['total_spent'] / customer['total_orders'], 2)
                
            customers.append(customer)
        
        df = pd.DataFrame(customers)
        csv_path = os.path.join(self.output_folder, 'customer_analysis.csv')
        df.to_csv(csv_path, index=False)
        print(f"Customer analysis dataset saved to: {csv_path}")
        return df

    def generate_product_inventory_csv(self, num_products=500):
        """Generate product inventory dataset"""
        print(f"Generating {num_products} product records...")
        
        products = []
        for i in range(num_products):
            category = random.choice(list(self.product_categories.keys()))
            subcategory = random.choice(self.product_categories[category])
            
            product = {
                'product_id': i + 1,
                'product_name': self.generate_product_name(),
                'category': category,
                'subcategory': subcategory,
                'brand': random.choice(self.brands),
                'price': round(random.uniform(10, 3000), 2),
                'cost': 0,  # Will calculate as 60-80% of price
                'stock_quantity': random.randint(0, 1000),
                'reorder_level': random.randint(10, 100),
                'supplier_id': random.randint(1, 20),
                'weight_kg': round(random.uniform(0.1, 50), 2),
                'dimensions': f"{random.randint(5,50)}x{random.randint(5,50)}x{random.randint(5,50)}cm",
                'color': random.choice(['Black', 'White', 'Red', 'Blue', 'Green', 'Gray', 'Silver', 'Gold']),
                'material': random.choice(['Plastic', 'Metal', 'Wood', 'Glass', 'Fabric', 'Leather', 'Ceramic']),
                'warranty_months': random.choice([6, 12, 24, 36]),
                'rating_avg': round(random.uniform(2.5, 5.0), 1),
                'review_count': random.randint(0, 1000),
                'is_bestseller': random.choice([True, False]),
                'launch_date': (datetime.now() - timedelta(days=random.randint(1, 1095))).strftime('%Y-%m-%d')
            }
            
            # Calculate cost as 60-80% of price
            product['cost'] = round(product['price'] * random.uniform(0.6, 0.8), 2)
            
            products.append(product)
        
        df = pd.DataFrame(products)
        csv_path = os.path.join(self.output_folder, 'product_inventory.csv')
        df.to_csv(csv_path, index=False)
        print(f"Product inventory dataset saved to: {csv_path}")
        return df

    def generate_monthly_reports_csv(self):
        """Generate monthly sales reports"""
        print("Generating monthly sales reports...")
        
        reports = []
        start_date = datetime(2023, 1, 1)
        
        for month_offset in range(24):  # 24 months of data
            report_date = start_date + timedelta(days=month_offset * 30)
            
            report = {
                'month': report_date.strftime('%Y-%m'),
                'total_sales': random.randint(50000, 200000),
                'total_orders': random.randint(1000, 5000),
                'unique_customers': random.randint(800, 4000),
                'average_order_value': round(random.uniform(80, 150), 2),
                'top_category': random.choice(list(self.product_categories.keys())),
                'new_customers': random.randint(100, 800),
                'returning_customers': random.randint(500, 3000),
                'customer_retention_rate': round(random.uniform(0.6, 0.9), 3),
                'gross_margin': round(random.uniform(0.25, 0.45), 3),
                'marketing_spend': random.randint(5000, 25000),
                'customer_acquisition_cost': round(random.uniform(20, 80), 2),
                'conversion_rate': round(random.uniform(0.02, 0.08), 4)
            }
            
            reports.append(report)
        
        df = pd.DataFrame(reports)
        csv_path = os.path.join(self.output_folder, 'monthly_sales_reports.csv')
        df.to_csv(csv_path, index=False)
        print(f"Monthly reports dataset saved to: {csv_path}")
        return df

    def generate_business_documents(self):
        """Generate various business documents"""
        print("Generating business documents...")
        
        # Business strategy document
        strategy_content = """
# Business Strategy Document 2024-2025

## Executive Summary
Our retail business has shown strong growth over the past year, with total revenue increasing by 25%. 
We are focusing on digital transformation and customer experience enhancement.

## Key Performance Indicators
- Monthly Active Customers: 15,000+
- Customer Retention Rate: 78%
- Average Order Value: $125
- Gross Margin: 35%

## Strategic Initiatives
1. **Digital Experience Enhancement**
   - Improve mobile app performance
   - Implement AI-powered recommendations
   - Enhance checkout process

2. **Inventory Optimization**
   - Implement predictive analytics for demand forecasting
   - Reduce stockouts by 30%
   - Optimize warehouse operations

3. **Customer Loyalty Program**
   - Launch new tier-based loyalty program
   - Increase customer lifetime value by 20%
   - Improve customer engagement

## Market Analysis
Our primary market consists of tech-savvy consumers aged 25-45. 
Competition is intense, particularly in the electronics category.

## Financial Projections
- Projected revenue growth: 30% year-over-year
- Target profit margin: 15%
- Investment in technology: $500,000
        """
        
        with open(os.path.join(self.output_folder, 'business_strategy_2024.txt'), 'w') as f:
            f.write(strategy_content)
        
        # Meeting notes
        meeting_notes = """
# Weekly Sales Team Meeting - Week of March 18, 2024

## Attendees
- Alice Johnson (Sales Manager)
- Bob Smith (Senior Sales Rep)
- Carol Davis (Sales Rep)
- Dave Wilson (Sales Rep)
- Eve Brown (Sales Rep)

## Key Discussion Points

### Sales Performance
- Week's total sales: $45,000 (15% above target)
- Electronics category performing exceptionally well
- Fashion category needs attention

### Customer Feedback
- Positive reviews for new iPhone 15 Pro launch
- Some complaints about shipping delays
- Customer service response time improved to 2 hours average

### Action Items
1. Bob to follow up with enterprise customers for Q2 contracts
2. Carol to organize promotional campaign for fashion items
3. Dave to coordinate with logistics team on shipping improvements
4. Eve to prepare competitive analysis report

### Upcoming Events
- Trade show participation next month
- New product launch event planned for April 15
- Quarterly business review scheduled for April 30

## Next Meeting: March 25, 2024
        """
        
        with open(os.path.join(self.output_folder, 'sales_meeting_notes.txt'), 'w') as f:
            f.write(meeting_notes)
        
        print("Business documents generated successfully!")

    def generate_product_name(self):
        """Generate realistic product names"""
        electronics = ['Pro Max Smartphone', 'Wireless Earbuds', 'Gaming Laptop', 'Smart Watch', 
                      '4K Monitor', 'Mechanical Keyboard', 'Wireless Mouse', 'Tablet Pro']
        fashion = ['Premium Sneakers', 'Designer Jeans', 'Leather Jacket', 'Cotton T-Shirt',
                  'Running Shoes', 'Casual Blazer', 'Sports Watch', 'Backpack']
        home = ['Smart Thermostat', 'Robot Vacuum', 'LED Light Bulbs', 'Coffee Maker',
               'Air Purifier', 'Security Camera', 'Smart Speaker', 'Wireless Charger']
        
        all_products = electronics + fashion + home
        return random.choice(all_products)

    def generate_review(self):
        """Generate realistic review text"""
        reviews = [
            "Great product, exceeded my expectations!",
            "Good value for money, would recommend.",
            "Fast shipping and excellent packaging.",
            "Product quality is outstanding.",
            "Customer service was very helpful.",
            "Exactly what I was looking for.",
            "Works perfectly, no issues so far.",
            "Good build quality and design.",
            "Delivered on time, very satisfied.",
            "Would definitely buy again."
        ]
        return random.choice(reviews)

    def get_season(self, month):
        """Get season based on month"""
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'

    def generate_excel_reports(self):
        """Generate Excel files with multiple sheets"""
        print("Generating Excel reports...")
        
        # Sales summary by category
        categories = list(self.product_categories.keys())
        sales_summary = []
        
        for category in categories:
            summary = {
                'Category': category,
                'Total_Sales': random.randint(50000, 150000),
                'Units_Sold': random.randint(1000, 5000),
                'Avg_Price': round(random.uniform(50, 300), 2),
                'Profit_Margin': round(random.uniform(0.15, 0.40), 3),
                'Top_Product': self.generate_product_name(),
                'YoY_Growth': round(random.uniform(-0.1, 0.5), 3)
            }
            sales_summary.append(summary)
        
        # Create Excel file with multiple sheets
        excel_path = os.path.join(self.output_folder, 'sales_analysis_report.xlsx')
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            pd.DataFrame(sales_summary).to_excel(writer, sheet_name='Category_Summary', index=False)
            
            # Add monthly trends sheet
            monthly_trends = []
            for i in range(12):
                trend = {
                    'Month': f"2024-{i+1:02d}",
                    'Revenue': random.randint(80000, 120000),
                    'Orders': random.randint(1500, 2500),
                    'New_Customers': random.randint(200, 500),
                    'Churn_Rate': round(random.uniform(0.05, 0.15), 3)
                }
                monthly_trends.append(trend)
            
            pd.DataFrame(monthly_trends).to_excel(writer, sheet_name='Monthly_Trends', index=False)
        
        print(f"Excel report saved to: {excel_path}")

    def generate_all_datasets(self):
        """Generate all datasets and documents"""
        print("=== Retail Data Generator ===")
        print(f"Output folder: {self.output_folder}")
        
        # Generate CSV files
        self.generate_large_sales_csv(10000)
        self.generate_customer_analysis_csv(2000)
        self.generate_product_inventory_csv(500)
        self.generate_monthly_reports_csv()
        
        # Generate Excel files
        self.generate_excel_reports()
        
        # Generate text documents
        self.generate_business_documents()
        
        print("\n=== Generation Complete ===")
        print(f"All files have been saved to: {os.path.abspath(self.output_folder)}")
        print("\nGenerated files:")
        for file in os.listdir(self.output_folder):
            print(f"  - {file}")

if __name__ == "__main__":
    generator = RetailDataGenerator()
    generator.generate_all_datasets()