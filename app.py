import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("OLA Ride Data Dashboard")

# Load dataset
df = pd.read_excel("C:\Users\HP\Desktop\KOMAL JADHAV\Projects\Labmentix\OLA\OLA_Cleaned_Data")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# 1 Ride Volume Over Time
st.subheader("Ride Volume Over Time")
rides = df.groupby("Date").size()

fig1, ax1 = plt.subplots()
rides.plot(ax=ax1)
st.pyplot(fig1)

# 2 Booking Status Breakdown
st.subheader("Booking Status Breakdown")
status = df["Booking_Status"].value_counts()

fig2, ax2 = plt.subplots()
status.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# 3 Top 5 Vehicle Types by Ride Distance
st.subheader("Top Vehicle Types by Ride Distance")
vehicle = df.groupby("Vehicle_Type")["Ride_Distance"].sum().sort_values(ascending=False).head(5)

fig3, ax3 = plt.subplots()
vehicle.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

# 4 Average Customer Rating by Vehicle Type
st.subheader("Average Customer Rating by Vehicle Type")
rating = df.groupby("Vehicle_Type")["Customer_Rating"].mean()

fig4, ax4 = plt.subplots()
rating.plot(kind="bar", ax=ax4)
st.pyplot(fig4)

# 5 Revenue by Payment Method
st.subheader("Revenue by Payment Method")
revenue = df.groupby("Payment_Method")["Booking_Value"].sum()

fig5, ax5 = plt.subplots()
revenue.plot(kind="bar", ax=ax5)
st.pyplot(fig5)

# 6 Top 5 Customers by Booking Value
st.subheader("Top 5 Customers")
top_customers = df.groupby("Customer_ID")["Booking_Value"].sum().sort_values(ascending=False).head(5)

st.dataframe(top_customers)

# 7 Driver Ratings Distribution
st.subheader("Driver Ratings Distribution")

fig6, ax6 = plt.subplots()
df["Driver_Ratings"].hist(ax=ax6)
st.pyplot(fig6)

# 8 Customer vs Driver Ratings
st.subheader("Customer vs Driver Ratings")

fig7, ax7 = plt.subplots()
ax7.scatter(df["Customer_Rating"], df["Driver_Ratings"])
ax7.set_xlabel("Customer Rating")
ax7.set_ylabel("Driver Rating")

st.pyplot(fig7)