import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="OLA Dashboard", layout="wide")

st.title("🚖 OLA Ride Data Analysis Dashboard")

# Load Data
df = pd.read_excel("OLA_Cleaned_Data.xlsx")

# ---------------- KPI SECTION ----------------

total_rides = df.shape[0]
total_revenue = df["Booking_Value"].sum()
avg_driver_rating = df["Driver_Ratings"].mean()
avg_distance = df["Ride_Distance"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", total_rides)
col2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col3.metric("Avg Driver Rating", round(avg_driver_rating,2))
col4.metric("Avg Ride Distance", round(avg_distance,2))

st.divider()

# ---------------- ROW 1 ----------------

col1, col2 = st.columns(2)

# Ride Volume Over Time
with col1:
    st.subheader("Ride Volume Over Time")

rides = df.groupby("Date").size()

fig, ax = plt.subplots(figsize=(6,3))

rides.plot(ax=ax)

ax.set_xlabel("Date")
ax.set_ylabel("Number of Rides")

st.pyplot(fig)

# Booking Status Pie Chart
with col2:
    st.subheader("Booking Status Breakdown")

    status = df["Booking_Status"].value_counts()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.pie(
        status,
        labels=status.index,
        autopct='%1.1f%%',
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

st.divider()

# ---------------- ROW 2 ----------------

col3, col4 = st.columns(2)

# Vehicle Type Horizontal Bar Chart
with col3:
    st.subheader("Vehicle Types by Ride Distance")

    vehicle_distance = (
        df.groupby("Vehicle_Type")["Ride_Distance"]
        .sum()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(6,3))

    vehicle_distance.plot(kind="barh", ax=ax)

    ax.set_xlabel("Total Ride Distance")
    ax.set_ylabel("Vehicle Type")

    st.pyplot(fig)

# Revenue by Payment Method
with col4:
    st.subheader("Revenue by Payment Method")

    revenue = df.groupby("Payment_Method")["Booking_Value"].sum()

    fig, ax = plt.subplots(figsize=(6,3))

    revenue.plot(kind="bar", ax=ax)

    st.pyplot(fig)

st.divider()

# ---------------- ROW 3 ----------------

col5, col6 = st.columns(2)

# Customer Rating Heatmap
with col5:
    st.subheader("Customer Rating ")

    customer_heat = df.pivot_table(
        values="Customer_Rating",
        index="Vehicle_Type",
        columns="Payment_Method",
        aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(6,4))

    sns.heatmap(customer_heat, annot=True, cmap="YlOrRd", ax=ax)

    st.pyplot(fig)

# Driver Rating Heatmap
with col6:
    st.subheader("Driver Rating ")

    driver_heat = df.pivot_table(
        values="Driver_Ratings",
        index="Vehicle_Type",
        columns="Payment_Method",
        aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(6,4))

    sns.heatmap(driver_heat, annot=True, cmap="Blues", ax=ax)

    st.pyplot(fig)