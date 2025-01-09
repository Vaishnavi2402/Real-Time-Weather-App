import streamlit as st
import requests

# Function to fetch weather data from OpenWeather API
def get_weather_data(city, api_key):
    """
    Fetch current weather data from OpenWeather API
    
    Parameters:
        city (str): The name of the city.
        api_key (str): OpenWeather API key.
        
    Returns:
        dict: Weather data including temperature, humidity, description.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching weather data: {response.status_code}")
        return None

# Streamlit App Layout
st.title("Real-Time Weather App")

# User Input for City
city = st.text_input("Enter city name:")
st.button("Submit")
# User Input for API Key (optional: You can hard-code your key)
api_key = "04b941e4fb5b07fa30734aa01fa92f29"

# Fetch and display weather data if API key is provided and city is entered
if api_key and city:
    weather_data = get_weather_data(city, api_key)
    
    if weather_data:
        # Extracting specific data from API response
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        
        # Displaying the weather details
        st.subheader(f"Weather in {city}")
        st.write(f"Temperature: {temperature}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Weather: {description.capitalize()}")
        st.write(f"Wind Speed: {wind_speed} m/s")
        
        if "clear" in description:
            st.image("https://www.istockphoto.com/photos/sunny-day")  # Replace with actual image URL
        elif "rain" in description:
            st.image("https://images.app.goo.gl/tuFtoRjy1WucPW8Z7")  