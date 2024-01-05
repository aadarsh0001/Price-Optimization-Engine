# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from datetime import datetime

# Load historical sales data
sales_data = pd.read_csv('sales_data.csv')

# Feature engineering
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['DayOfWeek'] = sales_data['Date'].dt.dayofweek
sales_data['Month'] = sales_data['Date'].dt.month
sales_data['Year'] = sales_data['Date'].dt.year

# Split data into training and testing sets
train_data, test_data = train_test_split(sales_data, test_size=0.2, random_state=42)

# Define features and target variable
features = ['DayOfWeek', 'Month', 'Year', 'Inventory', 'TermsOfTrade', 'Margins']
target = 'Price'

# Train a Random Forest Regressor model
model = RandomForestRegressor()
model.fit(train_data[features], train_data[target])

# Make predictions on test data
predictions = model.predict(test_data[features])

# Evaluate the model
mse = mean_squared_error(test_data[target], predictions)
print(f'Mean Squared Error: {mse}')

# Function to recommend price based on input parameters
def recommend_price(day_of_week, month, year, inventory, terms_of_trade, margins):
    input_data = [[day_of_week, month, year, inventory, terms_of_trade, margins]]
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Example usage
recommended_price = recommend_price(2, 1, 2024, 100, 0.1, 0.2)
print(f'Recommended Price: ${recommended_price}')
