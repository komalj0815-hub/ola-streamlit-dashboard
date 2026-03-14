import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="OLA Dashboard", layout="wide")

st.title("🚖 OLA Ride Data Analysis Dashboard")

# Load data
df = pd.read_excel("OLA_Cleaned_Data.xlsx")

# ---- KPI SECTION ----
total_rides = df.shape[0]
total_revenue = df["Booking_Value"].sum()
avg_driver_rating = df["Driver_Ratings"].mean()
avg_distance = df["Ride_Distance"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", total_rides)
col2.metric("Total Revenue", f"₹ {total_revenue:,.0f}")
col3.metric("Avg Driver Rating", round(avg_driver_rating,2))
col4.metric("Avg Ride Distance", round(avg_distance,2))

st.divider()

# ---- CHARTS ----

col1, col2 = st.columns(2)

# Ride Volume
with col1:
    st.subheader("Ride Volume Over Time")
    rides = df.groupby("Date").size()

    fig, ax = plt.subplots()
    rides.plot(ax=ax)
    st.pyplot(fig)

# Booking Status
with col2:
    st.subheader("Booking Status Breakdown")
    status = df["Booking_Status"].value_counts()

    fig, ax = plt.subplots()
    status.plot(kind="bar", ax=ax)
    st.pyplot(fig)

st.divider()

col3, col4 = st.columns(2)

# Revenue by Payment Method
with col3:
    st.subheader("Revenue by Payment Method")

    revenue = df.groupby("Payment_Method")["Booking_Value"].sum()

    fig, ax = plt.subplots()
    revenue.plot(kind="bar", ax=ax)
    st.pyplot(fig)

# Vehicle Type Distance
with col4:
    st.subheader("Top Vehicle Types by Ride Distance")

    vehicle = df.groupby("Vehicle_Type")["Ride_Distance"].sum().sort_values(ascending=False).head(5)

    fig, ax = plt.subplots()
    vehicle.plot(kind="bar", ax=ax)
    st.pyplot(fig)

st.divider()

# Customer Rating 
st.subheader("Customer Ratings Heatmap")

fig, ax = plt.subplots()

customer_heat = df.pivot_table(
    values="Customer_Rating",
    index="Vehicle_Type",
    columns="Payment_Method",
    aggfunc="mean"
)

sns.heatmap(customer_heat, annot=True, cmap="YlOrRd", ax=ax)

st.pyplot(fig)

#Driver Rating 

st.subheader("Driver Ratings Heatmap")

fig, ax = plt.subplots()

driver_heat = df.pivot_table(
    values="Driver_Ratings",
    index="Vehicle_Type",
    columns="Payment_Method",
    aggfunc="mean"
)

sns.heatmap(driver_heat, annot=True, cmap="Blues", ax=ax)

st.pyplot(fig)