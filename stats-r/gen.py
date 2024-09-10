# Import the necessary libraries
import pandas as pd
import numpy as np

# Generate a DataFrame with 5 random numbers
df = pd.DataFrame(np.random.randint(0, 100, (5, 1)), columns=['number'])

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)
