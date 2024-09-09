import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(file_path):
    """
    Load data from CSV, set date as index, and clean outliers.
    """
    # Load data
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')

    # Clean data by removing outliers
    lower_limit = df['value'].quantile(0.025)
    upper_limit = df['value'].quantile(0.975)
    df = df[(df['value'] >= lower_limit) & (df['value'] <= upper_limit)]
    
    return df

def draw_line_plot(df):
    """
    Draw a line plot of daily page views.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot(df):
    """
    Draw a bar plot of average daily page views per month grouped by year.
    """
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    df_bar_grouped.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot(df):
    """
    Draw box plots to show distribution by year and month.
    """
    # Prepare data for box plots
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month_name()

    # Draw Year-wise Box Plot
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Draw Month-wise Box Plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()

def main():
    """
    Main function to run all visualizations.
    """
    file_path = r'C:\Users\arman\OneDrive\Desktop\Coding\fcc-forum-pageviews.csv'  # Your file path
    df = load_and_clean_data(file_path)
    
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)

if __name__ == "__main__":
    main()
