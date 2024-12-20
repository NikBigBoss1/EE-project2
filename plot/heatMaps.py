import pandas as pd
import matplotlib.pyplot as plt

# Load the shared CSV file
csv_file = 'experiment_results.csv'
df = pd.read_csv(csv_file)


# ========== HEATMAP 1: Mean Time by Programming Experience ==========
def plot_experience_heatmap(df):
    # Calculate the mean time for each combination of experience and type
    mean_times = df.groupby(['experience', 'type'])['time'].mean().unstack(fill_value=0)

    # Plotting the heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(mean_times, cmap='coolwarm', aspect='auto')

    # Add color bar to indicate the scale
    plt.colorbar(label="Mean Time")

    # Set axis labels
    plt.title("Heatmap of Mean Time by Programming Experience")
    plt.xlabel("Identifier Type")
    plt.ylabel("Programming Experience")

    # Set tick labels for x-axis and y-axis
    plt.xticks(range(len(mean_times.columns)), mean_times.columns, rotation=0)
    plt.yticks(range(len(mean_times.index)), mean_times.index)

    # Save and show the heatmap
    plt.tight_layout()
    plt.savefig('heatmap_mean_time_programming.png', dpi=300)
    plt.show()


# ========== HEATMAP 2: Percentage of First Guess (True/False) ==========
def plot_first_true_heatmap(df):
    # Calculate percentages of true/false first guesses for each identifier style
    percentages = df.groupby(['type', 'firstGuess']).size().unstack(fill_value=0)
    percentages = percentages.div(percentages.sum(axis=1), axis=0) * 100

    # Plotting the heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(percentages, cmap='coolwarm', aspect='auto')

    # Add color bar to indicate the scale
    plt.colorbar(label="Percentage (%)")

    # Set axis labels and title
    plt.title("Heatmap of Percentage of First Guess (True/False)")
    plt.xlabel("First Guess")
    plt.ylabel("Identifier Type")

    # Set tick labels for x-axis and y-axis
    plt.xticks(range(len(percentages.columns)), percentages.columns, rotation=0)
    plt.yticks(range(len(percentages.index)), percentages.index)

    # Save and display the heatmap
    plt.tight_layout()
    plt.savefig('first_guess_heatmap.png', dpi=300)
    plt.show()


# ========== HEATMAP 3: Proportion of First Guess by Language Proficiency ==========
def plot_language_heatmap(df):
    # Group by languageProficiency, type, and firstGuess
    grouped = df.groupby(["languageProficiency", "type", "firstGuess"]).size().reset_index(name="count")

    # Pivot to get a table with True/False as separate columns
    pivot_table = grouped.pivot_table(
        index=["languageProficiency", "type"],
        columns="firstGuess",
        values="count",
        fill_value=0
    )

    # Calculate proportions (True/False)
    pivot_table = pivot_table.apply(lambda x: x / x.sum(), axis=1)

    # Convert to percentages
    pivot_table = pivot_table * 100

    # Unstack so rows represent languageProficiency and columns represent (firstGuess, type)
    heatmap_data = pivot_table.unstack(level='type')

    # Plotting the heatmap
    plt.figure(figsize=(12, 6))
    plt.imshow(heatmap_data, cmap='coolwarm', aspect='auto')

    # Adding color bar
    plt.colorbar(label="Percentage (%)")

    # Setting axis labels and title
    plt.title("Heatmap of Proportion of First Guess by Language Proficiency and Type")
    plt.xlabel("FirstGuess, Type")
    plt.ylabel("Language Proficiency")

    # Setting x and y tick labels with no rotation
    plt.xticks(range(len(heatmap_data.columns)), [f"{col[0]}, {col[1]}" for col in heatmap_data.columns], rotation=0)
    plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('language_by_first_guess_heatmap_adjusted_no_rotation.png', dpi=300)
    plt.show()


# Call each heatmap function
plot_experience_heatmap(df)
plot_first_true_heatmap(df)
plot_language_heatmap(df)
