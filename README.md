Description of time_series_visualizer.py
The time_series_visualizer.py script performs data visualization on a dataset containing daily page views for the freeCodeCamp forum from May 9, 2016, to December 3, 2019. The script utilizes Pandas for data manipulation, Matplotlib for creating line and bar charts, and Seaborn for generating box plots. The visualizations help to understand trends, seasonal patterns, and outliers in the dataset.

Functions
load_and_clean_data(file_path)

Purpose: Load and clean the dataset.
Parameters: file_path (str) – The path to the CSV file containing the dataset.
Operations:
Reads the CSV file into a Pandas DataFrame.
Sets the date column as the index and parses it as dates.
Filters out the top 2.5% and bottom 2.5% of page view values to remove outliers.
Returns: A cleaned DataFrame with outliers removed.
draw_line_plot(df)

Purpose: Generate a line plot of daily page views.
Parameters: df (DataFrame) – The cleaned DataFrame.
Operations:
Creates a line plot of page views over time.
Sets the x-axis label to "Date" and the y-axis label to "Page Views".
Titles the plot "Daily freeCodeCamp Forum Page Views 5/2016-12/2019".
Output: Saves the plot as line_plot.png and displays it.
draw_bar_plot(df)

Purpose: Create a bar plot showing average daily page views for each month, grouped by year.
Parameters: df (DataFrame) – The cleaned DataFrame.
Operations:
Extracts the year and month from the index and computes the average page views for each month, grouped by year.
Creates a bar plot with years on the x-axis and average page views on the y-axis.
Adds a legend with month labels and titles the plot "Average Daily Page Views per Month".
Output: Saves the plot as bar_plot.png and displays it.
draw_box_plot(df)

Purpose: Produce two box plots to visualize the distribution of page views by year and by month.
Parameters: df (DataFrame) – The cleaned DataFrame.
Operations:
Extracts year and month information for creating box plots.
Generates a box plot showing the distribution of page views for each year.
Generates a second box plot showing the distribution of page views for each month.
Titles the plots "Year-wise Box Plot (Trend)" and "Month-wise Box Plot (Seasonality)" respectively.
Output: Saves the plots as box_plot.png and displays them.
main()

Purpose: Orchestrates the loading of data and the creation of visualizations.
Operations:
Defines the file path to the dataset.
Calls load_and_clean_data to load and clean the data.
Invokes draw_line_plot, draw_bar_plot, and draw_box_plot to generate the respective visualizations.
