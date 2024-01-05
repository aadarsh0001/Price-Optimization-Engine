# Project Name: Price Optimization Engine

## Overview:
The Price Optimization Engine is designed to provide dynamic pricing recommendations for the grocery retail industry. This Python script uses a Random Forest Regressor model to predict product prices based on various features, such as day of the week, month, year, inventory levels, terms of trade, and margins.

## Getting Started:

### Clone the Repository:
```bash
git clone https://github.com/aadarsh0001/Price-Optimization-Engine.git
```

### Install Dependencies:
```bash
pip install pandas numpy
pip install pandas scikit-learn
```

### Run the Code:
```bash
python PriceOE.py
```

## Project Structure:
- `PriceOE.py`: Python script containing the Price Optimization Engine code.  <br>

- `sales_data.csv`: CSV file containing historical sales data.

## Usage:

1. Ensure you have Python and required libraries installed.  <br>
2. Run the script ( `python PriceOE.py` ) to train the model, make predictions, and print the mean squared error.   <br>
3. Customize the `recommend_price` function for real-time usage in your application.  <br>


## Test Cases:

```bash
# Test Cases
# Case 1: Testing with sample input for recommendation
test_case_1 = recommend_price(0, 6, 2023, 150, 0.15, 0.25)
print(f'Test Case 1: ${test_case_1}')

# Case 2: Testing with another set of input parameters
test_case_2 = recommend_price(4, 3, 2024, 80, 0.12, 0.18)
print(f'Test Case 2: ${test_case_2}')

# Case 3: Testing with extreme values
test_case_3 = recommend_price(6, 12, 2022, 200, 0.05, 0.3)
print(f'Test Case 3: ${test_case_3}')

# Case 4: Testing with invalid input (negative values)
test_case_4 = recommend_price(1, 8, 2023, -50, 0.2, 0.15)
print(f'Test Case 4: ${test_case_4}')

# Case 5: Testing with invalid input (out of range values)
test_case_5 = recommend_price(8, 13, 2025, 250, 0.25, 0.4)
print(f'Test Case 5: ${test_case_5}')

```

## Let's connect

We can connect on LinkedIn:

- Aadarsh Tiwari: [LinkedIn Profile](https://www.linkedin.com/in/aadarshtiwari)

  # Happy coding!
