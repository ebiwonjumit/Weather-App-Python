# Weather Emoji App 🌦️

A beginner-friendly Python project that fetches weather data for any city and displays appropriate emojis based on the current conditions. This project is designed as a learning exercise to practice working with APIs, handling JSON data, and building interactive command-line applications.

## 🎯 Project Overview

The Weather Emoji App:
- Takes a city name as input
- Fetches real-time weather data using the OpenWeatherMap API
- Displays weather conditions with fun, intuitive emojis
- Shows different emojis based on:
  - Weather conditions (sunny, rainy, cloudy, etc.)
  - Temperature ranges (cold, mild, hot)
  - Time of day (day/night)

## 💻 Prerequisites

Before starting this project, make sure you have:

- Python 3.6 or higher installed
- Basic understanding of Python syntax
- Git installed on your computer
- Internet connection to access the weather API

## 🛠️ Setup Instructions

### 1. Install Python

If you don't have Python installed:

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest version for your operating system
3. Run the installer
   - On Windows: Make sure to check "Add Python to PATH" during installation
4. Verify installation by opening a terminal/command prompt and typing:
   ```
   python --version
   ```
   or on some systems:
   ```
   python3 --version
   ```

### 2. Install Git

If you don't have Git installed:

1. Visit [git-scm.com/downloads](https://git-scm.com/downloads)
2. Download the latest version for your operating system
3. Run the installer with default settings
4. Verify installation by opening a terminal/command prompt and typing:
   ```
   git --version
   ```

### 3. Clone the Repository

1. Open a terminal or command prompt
2. Navigate to the directory where you want to store the project
3. Clone the repository by running:
   ```
   git clone https://github.com/ebiwonjumit/weather-app-python.git
   ```
   (Replace "username" with the actual GitHub username or organization name)
4. Navigate into the project directory:
   ```
   cd weather-app-python
   ```

### 4. Set Up a Virtual Environment (Optional but Recommended)

Setting up a virtual environment helps keep your project dependencies isolated:

**On Windows:**
```
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Required Dependencies

Install the `requests` library, which we'll use to make API calls:

```
pip install requests
```
or
```
pip3 install requests
```

### 6. Get an API Key

1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. Generate an API key from your account dashboard
3. Keep this API key handy for use in the app

### 7. Getting Updates from the Repository

If you need to pull the latest updates from the repository:

1. Make sure you're in the project directory
2. Run:
   ```
   git pull origin main
   ```
   (or replace "main" with the name of the primary branch if different)

## 🚀 How to Run the App

1. Make sure you've completed all the setup steps above
2. Open the `weather_emoji_app.py` file and replace `"YOUR_API_KEY_HERE"` with your actual OpenWeatherMap API key
3. Complete all the coding exercises marked with `# YOUR CODE HERE` comments
4. Save the file
5. Run the app:

**On Windows:**
```
python weather_emoji_app.py
```

**On macOS/Linux:**
```
python3 weather_emoji_app.py
```

## 💡 How to Use the App

1. When prompted, enter the name of any city
2. View the current weather conditions, temperature, and emoji representation
3. Enter another city name to check weather elsewhere
4. Type 'exit' when you want to quit the app

## 📝 Project Tasks

The template contains 13 steps for you to complete:

1. Set up your API key
2. Build the API URL
3. Make the API request
4. Parse the JSON response
5. Extract weather information
6. Create the emoji mapping
7. Handle day/night conditions
8. Choose the right emoji based on weather and time
9. Add temperature indicators
10. Get the city name and prepare the result
11. Handle errors
12. Create the main loop
13. Run the main function when the script is executed

## 🐛 Troubleshooting

Common issues and their solutions:

- **ModuleNotFoundError: No module named 'requests'**
  - Run `pip install requests` to install the required library

- **Invalid API key**
  - Double-check that you've correctly copied your API key from OpenWeatherMap

- **City not found**
  - Check the spelling of the city name
  - Try adding the country code after the city name (e.g., "London,UK")
  
- **Git-related issues**
  - "fatal: not a git repository": Make sure you're in the right directory
  - "Permission denied": Ensure you have the correct permissions or use SSH keys
  - "Cannot connect to GitHub": Check your internet connection

## 🔍 Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Working with JSON in Python](https://realpython.com/python-json/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

## 🎓 Extension Ideas

After completing the basic app, try enhancing it with:

1. A more detailed weather forecast (multi-day)
2. Saving favorite cities
3. Converting between temperature units (Celsius/Fahrenheit)
4. Adding a simple graphical user interface
5. Deploying as a web app

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API
- All the emoji designers who make weather reporting more fun!
