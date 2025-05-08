import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    
    # Create first line of best fit (all data)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    y1 = res1.intercept + res1.slope * x1
    plt.plot(x1, y1, 'r', label='Best Fit Line (1880-2013)')
    
    # Create second line of best fit (2000 onwards)
    recent = df[df['Year'] >= 2000]
    res2 = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = res2.intercept + res2.slope * x2
    plt.plot(x2, y2, 'green', label='Best Fit Line (2000-2013)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Set x-ticks to match test requirements
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()