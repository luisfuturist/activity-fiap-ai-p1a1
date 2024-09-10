# Install packages if not already installed
suppressMessages(suppressWarnings({
  if (!require("readr")) {
    install.packages("readr")
  }
}))

# Read data from CSV file
csvData <- read_csv('./data.csv', show_col_types = FALSE)

# Ensure data is numeric
data <- as.numeric(csvData[[1]])

# Calculate mean
dataMean <- mean(data)

# Calculate standard deviation
standardDeviation <- sd(data)

# Print results
cat("Média:", dataMean, "\n")
cat("Desvio Padrão:", standardDeviation, "\n")
