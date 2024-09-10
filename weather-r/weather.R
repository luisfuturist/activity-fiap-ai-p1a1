# Install packages if not already installed
suppressMessages(suppressWarnings({
  if (!require("httr")) {
    install.packages("httr")
  }
  if (!require("jsonlite")) {
    install.packages("jsonlite")
  }
  if (!require("dotenv")) {
    install.packages("dotenv")
  }
  if (!require("crayon")) {
    install.packages("crayon")
  }
}))

# Load the required packages
library(httr)
library(jsonlite)
library(crayon)
suppressWarnings(library(dotenv))

# Define a function to get user input
input <- function(...) {
  cat(...)
  readLines("stdin", n = 1)
}

# Load environment variables from the .env file
suppressWarnings(dotenv::load_dot_env(".env"))

# Access the API key
api_key <- Sys.getenv("OPEN_WEATHER_API_KEY")

# Check if the API key was loaded correctly
if (!nzchar(api_key)) {
  stop(red("OPEN_WEATHER_API_KEY não foi definida no arquivo .env\n"))
}

get_weather <- function(city, state = NULL, country = NULL) {
  # Construct the query parameters
  location <- URLencode(paste(city, state, country, sep = ","))

  url <- paste0("http://api.openweathermap.org/data/2.5/weather?q=", location, "&appid=", api_key, "&units=metric&lang=pt_br")

  response <- GET(url)

  if (response$status_code == 404) {
    cat(red("\nErro: localização não encontrada\n"))
    prompt_location()
    return(NULL)
  }

  if (response$status_code != 200) {
    cat(red("Erro:\n"))
    cat(red(content(response, "text"), "\n"))
    cat(red("Tente novamente.\n"))
    return(NULL)
  }

  # Parse the response as JSON
  data <- fromJSON(content(response, "text"))

  # Extract and format the desired data
  weather_info <- list(
    city_name = data$name,
    temperature = data$main$temp,
    description = data$weather[[3]],
    wind_speed = data$wind$speed,
    humidity = data$main$humidity
  )

  return(weather_info)
}

prompt_city <- function() {
  city <- input("Cidade: ")

  # Check if the city is empty, ignore leading and trailing whitespaces
  if (trimws(city) == "") {
    cat(red("Erro: cidade deve ser preenchida.\n"))
    return(prompt_city())
  }

  return(city)
}

display_weather <- function(city, state, country) {
  cat(silver("Buscando informações meteorológicas...\n"))
  weather <- get_weather(city, state, country)

  if (is.null(weather)) {
    main()
    return()
  }

  cat("\n--------------------------------\n")
  cat(paste0("Cidade: ", blue(weather$city_name), "\n"))
  cat(paste0("Temperatura: ", blue(weather$temperature), " °C\n"))
  cat(paste0("Condição: ", blue(weather$description), "\n"))
  cat(paste0("Umidade: ", blue(weather$humidity), blue("%\n")))
  cat(paste0("Velocidade do vento: ", blue(weather$wind_speed), blue(" m/s\n")))
  cat("--------------------------------\n\n")

  cat(bold("1."), "Atualizar dados\n")
  cat(bold("2."), "Pesquisar outra localização\n")
  cat(bold("3."), "Sair\n\n")

  choice <- input("Escolha uma opção: ")

  if (choice == "1") {
    display_weather(city, state, country)
  } else if (choice == "2") {
    prompt_location()
  } else if (choice == "3") {
    cat(silver("Saindo...\n"))
    q("no")
  } else {
    cat(red("Erro: Opção inválida. Tente novamente.\n"))
  }
}

prompt_location <- function() {
  cat("\n")

  city <- prompt_city()
  state <- input("Estado:", silver("(opcional) "))
  country <- input("País:", silver("(opcional) "))

  display_weather(city, state, country)
}

# Display the welcome message
cat(blue("# Weather App\n\n"))
cat(silver("Obtenha dados meteorológicas de qualquer cidade do mundo.\n\n"))

main <- function() {
  cat(bold("1."), "Iniciar\n")
  cat(bold("2."), "Sair\n\n")

  choice <- input("Escolha uma opção: ")

  if (choice == "1") {
    prompt_location()
  } else if (choice == "2") {
    cat(silver("Saindo...\n"))
    q("no")
  } else {
    cat(red("Erro: Opção inválida. Tente novamente.\n"))
  }
}

while (TRUE) {
  main()
}
