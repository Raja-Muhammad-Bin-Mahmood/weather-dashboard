import streamlit as st
import requests

# OpenWeatherMap API configuration
api_key = "ec5dff3620be8d025f51f648826a4ada"  # Your actual OpenWeatherMap API key
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Fetch weather data
response = requests.get(url)
data = response.json()

# Streamlit app
st.set_page_config(page_title="Weather Dashboard for PD Khan", page_icon=":sunny:", layout="wide")

st.title("Weather Dashboard for PD Khan")
st.write("Live weather data from OpenWeatherMap API")

# Check if data is retrieved successfully
if 'main' in data:
    current_temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    humidity = data['main']['humidity']

    # Using Streamlit's built-in table functionality
    st.write("### Current Weather Data")
    table_data = {
        "Parameter": ["Temperature", "Feels like", "Minimum Temperature", "Maximum Temperature", "Humidity"],
        "Value": [f"{current_temp}°C", f"{feels_like}°C", f"{min_temp}°C", f"{max_temp}°C", f"{humidity}%"]
    }
    st.write(table_data)

else:
    st.error(f"Error: {data.get('message', 'Unexpected error occurred')}")

# Custom styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f0f0;
            color: #333;
        }
        .stTitle {
            color: #ff6600;
            font-size: 2.5em;
        }
    </style>
""", unsafe_allow_html=True)
