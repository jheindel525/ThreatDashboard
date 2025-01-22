import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

# Generate a bar chart for analysis stats
def plot_analysis_stats(dataframe):
    # Sum the analysis stats across all domains
    stats = dataframe[["malicious", "suspicious", "harmless", "undetected"]].sum()

    # Plot the stats as a bar chart
    plt.bar(stats.index, stats.values, color='skyblue')
    plt.title("Overall Analysis Stats for Domains")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig("visuals/analysis_chart.png")  # Save the chart as an image
    plt.show()
    print("Visualization saved as visuals/analysis_chart.png")

if __name__ == "__main__":
    # Load the data
    csv_file = "data/domain_data.csv"
    df = load_data(csv_file)

    # Check if the data was loaded successfully
    if df is not None:
        plot_analysis_stats(df)
