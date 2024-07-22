import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

car_prices=pd.read_csv("\\Users\ADMIN\Downloads\car_prices.csv")
st.title("Car Prices Analysis Dashboard")

# Display the dataset
st.write("Dataset Preview:")
st.dataframe(car_prices.head())

#  Number of car models
num_car_models = car_prices['model'].nunique()
st.write(f"Number of car models: {num_car_models}")

# Seller with the most cars sold
seller_most_cars_sold = car_prices['seller'].value_counts().idxmax()
st.write(f"Seller with the most cars sold: {seller_most_cars_sold}")

# Most expensive car
most_expensive_car = car_prices.loc[car_prices['sellingprice'].idxmax()]
st.write("Most expensive car details:")
st.write(most_expensive_car)

# Plot: Distribution of car prices
plt.figure(figsize=(10, 6))
plt.hist(car_prices['sellingprice'], bins=50, color='blue', edgecolor='black')
plt.title('Distribution of Car Prices')
plt.xlabel('sellingPrice')
plt.ylabel('Number of Cars')
st.pyplot(plt)

# Number of cars sold per year
car_prices['year'] = pd.to_datetime(car_prices['saledate']).dt.year
cars_sold_per_year = car_prices['year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
cars_sold_per_year.plot(kind='bar', color='green')
plt.title('Number of Cars Sold Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Cars Sold')
st.pyplot(plt)

# Car with the most unique interior
most_unique_interior_car = car_prices['interior'].value_counts().idxmax()
st.write(f"Car with the most unique interior: {most_unique_interior_car}")

# Year with the most car sales
year_most_sales = car_prices['year'].value_counts().idxmax()
st.write(f"Year with the most car sales: {year_most_sales}")

# Car that travelled the most distance
car_most_distance = car_prices.loc[car_prices['odometer'].idxmax()]
st.write("Car that travelled the most distance:")
st.write(car_most_distance)

# Most popular car
most_popular_car = car_prices['model'].value_counts().idxmax()
st.write(f"Most popular car: {most_popular_car}")

# Seller of the most expensive SUV
suv_data = car_prices[car_prices['body_type'].str.contains('SUV', na=False, case=False)]
most_expensive_suv = suv_data.loc[suv_data['sellingprice'].idxmax()]
seller_most_expensive_suv = most_expensive_suv['seller']
st.write(f"The seller who sold the most expensive SUV is: {seller_most_expensive_suv}")
