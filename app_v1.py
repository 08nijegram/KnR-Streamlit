import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# App title with branding
st.title("Sensa Beauty 🌸✨")

# Section: Metrics
st.header("Metrics")
st.write("Explore key metrics below:")

# Load the data from CSV files
@st.cache_data
def load_data():
    daily_sales_orders = pd.read_csv('daily_sales_orders.csv')
    return daily_sales_orders

# Load the data
data = load_data()

# Convert 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Calculate 7-day rolling cumulative metrics, handling NaN values
data['7_day_sales'] = data['total_sales'].rolling(window=7).sum().fillna(0)
data['7_day_orders'] = data['total_orders'].rolling(window=7).sum().fillna(0)

# Plot the dual-axis chart for daily sales and orders
fig = go.Figure()

# First axis: Sales (left y-axis)
fig.add_trace(go.Scatter(
    x=data['date'],
    y=data['total_sales'],
    name="Total Sales",
    mode='lines',
    line=dict(color='blue'),
    yaxis="y1"  # Left y-axis
))

# Second axis: Orders (right y-axis)
fig.add_trace(go.Scatter(
    x=data['date'],
    y=data['total_orders'],
    name="Total Orders",
    mode='lines',
    line=dict(color='green'),
    yaxis="y2"  # Right y-axis
))

# Update layout for dual-axis without legend
fig.update_layout(
    xaxis_title="Date",
    yaxis=dict(
        title="Total Sales",
        titlefont=dict(color="blue"),
        tickfont=dict(color="blue"),
        side="left"
    ),
    yaxis2=dict(
        title="Total Orders",
        titlefont=dict(color="green"),
        tickfont=dict(color="green"),
        overlaying="y",
        side="right"
    ),
    showlegend=False,
    height=600,
    width=1000
)

# Show the daily chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Section: Rolling 7-Day Cumulative Metrics
st.header("7-Day Rolling Cumulative Metrics")

# Plot the rolling 7-day cumulative metrics chart
fig_rolling = go.Figure()

# First axis: 7-day cumulative sales (left y-axis)
fig_rolling.add_trace(go.Scatter(
    x=data['date'],
    y=data['7_day_sales'],
    name="7-Day Cumulative Sales",
    mode='lines',
    line=dict(color='blue'),
    yaxis="y1"  # Left y-axis
))

# Second axis: 7-day cumulative orders (right y-axis)
fig_rolling.add_trace(go.Scatter(
    x=data['date'],
    y=data['7_day_orders'],
    name="7-Day Cumulative Orders",
    mode='lines',
    line=dict(color='green'),
    yaxis="y2"  # Right y-axis
))

# Update layout for dual-axis without legend
fig_rolling.update_layout(
    xaxis_title="Date",
    yaxis=dict(
        title="7-Day Cumulative Sales",
        titlefont=dict(color="blue"),
        tickfont=dict(color="blue"),
        side="left"
    ),
    yaxis2=dict(
        title="7-Day Cumulative Orders",
        titlefont=dict(color="green"),
        tickfont=dict(color="green"),
        overlaying="y",
        side="right"
    ),
    showlegend=False,
    height=600,
    width=1000
)

# Show the rolling 7-day cumulative chart in the Streamlit app
st.plotly_chart(fig_rolling, use_container_width=True)

# Footer note
st.write("Data powered by Sensa Beauty 🌸✨")
