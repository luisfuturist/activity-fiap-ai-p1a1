# Load the required packages
library(httr)
library(jsonlite)
library(dotenv)

# Load environment variables from the .env file
dotenv::load_dot_env(".env")

# Access the API key
api_key <- Sys.getenv("OPEN_WEATHER_API_KEY")

# Check if the API key was loaded correctly
if (!nzchar(api_key)) {
  stop("OPEN_WEATHER_API_KEY not set.\n")
}

# Define the city and country for which you want to get weather data
city <- "Itajaí"
country <- "BR"

# Create the URL for the API request
url <- paste0(
  "http://api.openweathermap.org/data/2.5/weather?q=",
  city, ",", country, "&appid=", api_key, "&units=metric&lang=pt_br"
)

# Make the request to the API
response <- GET(url)

# Check if the request was successful
if (status_code(response) == 200) {
  # Parse the response content to JSON
  data <- fromJSON(content(response, "text", encoding = "UTF-8"))

  # Extract and format the desired data
  temperature <- data$main$temp
  description <- data$weather[[3]]
  humidity <- data$main$humidity
  wind_speed <- data$wind$speed
  city_name <- data$name

  # Display the data in the terminal
  cat("Clima em", city_name, ":\n")
  cat("Temperatura:", temperature, "°C\n")
  cat("Condição:", description, "\n")
  cat("Umidade:", humidity, "%\n")
  cat("Velocidade do Vento:", wind_speed, "m/s\n")
} else {
  cat("Falha ao obter dados meteorológicos. Status code:", status_code(response), "\n")
}
