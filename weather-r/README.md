# Weather

The Weather App is a simple command-line tool written in R that allows users to fetch and display current weather information for any city in the world. The application interacts with the OpenWeatherMap API to retrieve real-time weather data, offering an easy way to check temperature, conditions, humidity, and wind speed directly from the terminal.

## Key Features

- **Real-Time Weather Data:** Get up-to-date weather information, including temperature, weather conditions, humidity, and wind speed.
- **Global Coverage:** Search for weather data by city name with optional state and country specification.
- **Interactive User Interface:** The app provides an intuitive command-line interface with options to refresh weather data, search for new locations, or exit the application.

## Usage Instructions

Using the Weather App is straightforward:

1. **Run the Script:** Start the application by running the R script in your terminal. It will prompt you with a main menu.
2. **Search for Weather:** Choose the "Iniciar" option to search for weather data. Enter the city name, with optional state and country, when prompted.
3. **View and Interact:** After retrieving the weather information, you can choose to update the data, search for another location, or exit the application.

## Installing

> **Note:**  
> Before running the Weather App, ensure you have the following prerequisites installed on your system:
> 
> - **R:** Ensure that R is installed on your system. You can download R from [here](https://cran.r-project.org/mirrors.html).
> - **Required Packages:** The script will automatically install the necessary R packages (`httr`, `jsonlite`, `dotenv`, `crayon`) if they are not already installed.

### Steps to Install and Run

1. **Obtain an API Key:** Register for an OpenWeatherMap account at [openweathermap.org](https://home.openweathermap.org/users/sign_up) and obtain an API key.

2. **Set Environment Variables:**
   - Create a `.env` file in the root directory of your project.
   - Add the following line to your `.env` file, replacing `YOUR_API_KEY` with your actual OpenWeatherMap API key:
     ```
     OPEN_WEATHER_API_KEY="YOUR_API_KEY"
     ```

3. **Run the Script:**
   Execute the script in your terminal by running:
   ```bash
   Rscript weather.R
   ```

   This command will start the Weather App, allowing you to fetch and display weather data for any location.

## License

This project is licensed under the [MIT License](../LICENSE).
