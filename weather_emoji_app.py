# Weather Emoji App - Learning Exercise
# =====================================
# SETUP INSTRUCTIONS:
# 1. Make sure Python is installed on your computer:
#    - Visit https://www.python.org/downloads/ to download and install Python if needed
#    - During installation, check the box "Add Python to PATH"
#
# 2. Install the requests library by running this command in your terminal/command prompt:
#    - On Windows: pip install requests
#    - On Mac/Linux: pip3 install requests
#
# 3. Run this program from your terminal/command prompt with:
#    - On Windows: python weather_emoji_app.py
#    - On Mac/Linux: python3 weather_emoji_app.py

import requests
from datetime import datetime

# STEP 1: Set up your API key
# ---------------------------
# Sign up for a free API key at https://openweathermap.org/api
# Replace the value below with your actual API key
api_key = "YOUR_API_KEY_HERE"  # ← Replace this!


def get_weather_emoji(city):
    """
    Get the current weather for a city and return an appropriate emoji
    
    Parameters:
    city (str): The name of the city to get weather for
    
    Returns:
    dict: A dictionary containing weather information and emojis
    """
    # STEP 2: Build the API URL
    # -------------------------
    # Using string formatting, create the full URL for the OpenWeatherMap API
    # Include the city, your API key, and set units to metric
    # Hint: the base URL is "https://api.openweathermap.org/data/2.5/weather"
    
    url = ""  # YOUR CODE HERE - Create the API URL with f-string formatting
    
    try:
        # STEP 3: Make the API request
        # ---------------------------
        # Use requests.get() to call the API and store the response
        
        response = None  # YOUR CODE HERE - Make the API request
        
        # This raises an exception if the request failed
        response.raise_for_status()
        
        # STEP 4: Parse the JSON response
        # ------------------------------
        # Parse the response into a Python dictionary
        
        data = None  # YOUR CODE HERE - Parse the JSON response
        
        # STEP 5: Extract weather information
        # ----------------------------------
        # Get the main weather condition and temperature from the data
        # Hint: weather condition is in data['weather'][0]['main']
        # Temperature is in data['main']['temp']
        
        weather_main = ""  # YOUR CODE HERE - Get the weather condition
        temp = 0  # YOUR CODE HERE - Get the temperature
        
        # Make weather_main lowercase for easier matching
        weather_main = weather_main.lower()
        
        # STEP 6: Create the emoji mapping
        # -------------------------------
        # Create a dictionary that maps weather conditions to emojis
        # We've provided a starter dictionary - add more weather conditions and emojis!
        
        weather_emojis = {
            'clear': '☀️',
            # YOUR CODE HERE - Add more weather conditions and emojis
        }
        
        # STEP 7: Handle day/night conditions
        # ----------------------------------
        # Get the timezone offset from UTC and calculate local time
        # We'll use this to show different emojis for day and night
        
        timezone_offset = data['timezone']  # offset in seconds from UTC
        # YOUR CODE HERE - Calculate the local time using datetime
        
        # STEP 8: Choose the right emoji based on weather and time
        # ------------------------------------------------------
        # Choose different emojis for day and night for clear weather
        # For other conditions, use the emoji from the dictionary
        
        emoji = ""  # YOUR CODE HERE - Set the emoji based on weather and time of day
            
        # STEP 9: Add temperature indicators
        # --------------------------------
        # Modify the emoji based on temperature ranges
        # e.g., add '🥶' for very cold, '🔥' for hot
        
        # YOUR CODE HERE - Add temperature indicators to the emoji
            
        # STEP 10: Get the city name and prepare the result
        # -----------------------------------------------
        # Get the city name from the response and format the results
        
        city_name = data['name']
        
        # Return all the information in a dictionary
        return {
            'city': city_name,
            'weather': weather_main,
            'temperature': temp,
            'emoji': emoji,
            'datetime': "YOUR CODE HERE - Format the local time as a string"
        }
        
    except requests.exceptions.HTTPError as e:
        # STEP 11: Handle errors
        # ---------------------
        # Return helpful error messages when things go wrong
        
        # YOUR CODE HERE - Handle API errors, especially 404 (city not found)
        return {'error': f"An error occurred: {str(e)}"}
        
    except Exception as e:
        return {'error': f"An error occurred: {str(e)}"}


def main():
    """Main function to run the Weather Emoji App"""
    print("🌈 Weather Emoji App 🌈")
    print("------------------------")
    
    # STEP 12: Create the main loop
    # ---------------------------
    # Create a loop that keeps asking for cities until the user types 'exit'
    
    # YOUR CODE HERE - Create the main loop
    # Hint: use a while True loop with an if/break to exit
    
    # Inside your loop:
    # 1. Ask for a city name
    # 2. Call get_weather_emoji() with the city name
    # 3. Display the results nicely
    # 4. Exit if the user types 'exit'


# STEP 13: Run the main function when the script is executed
# --------------------------------------------------------
# Make sure the main() function only runs when this file is executed directly
if __name__ == "__main__":
    main()