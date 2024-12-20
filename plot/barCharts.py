import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Load the shared CSV file
csv_file = 'experiment_results.csv'
df = pd.read_csv(csv_file)


# ========== PLOT 1: Mean Time by Programming Experience ==========
def plot_experience_mean(df):
    # Calculate the mean time for each combination of experience and type
    mean_times = df.groupby(['experience', 'type'])['time'].mean().unstack(fill_value=0)

    # Plotting
    mean_times.plot(kind='bar', stacked=False, figsize=(8, 6))

    # Adding labels and title
    plt.title("Mean Time by Programming Experience")
    plt.ylabel("Mean Time")
    plt.xlabel("Programming Experience")
    plt.xticks(rotation=0)  # Rotate x-axis labels if necessary

    # Save the plot
    plt.savefig('mean_time_by_programming.png', dpi=300)
    plt.show()


# ========== PLOT 2: Percentage of First Guess (True/False) ==========
def plot_first_true_guess(df):
    # Calculate percentages of true/false first guesses for each identifier style
    percentages = df.groupby(['type', 'firstGuess']).size().unstack(fill_value=0)
    percentages = percentages.div(percentages.sum(axis=1), axis=0) * 100

    # Plotting
    percentages.plot(kind='bar', stacked=False, figsize=(8, 6))

    # Adding labels and title
    plt.title("Percentage of First Guess (True/False) for camelCase and kebab-case")
    plt.ylabel("Percentage (%)")
    plt.xlabel("Identifier Type")
    plt.xticks(rotation=0)  # Rotate x-axis labels if necessary

    # Save the plot
    plt.savefig('first_guess.png', dpi=300)
    plt.show()


# ========== PLOT 3: Proportion of First Guess by Language Proficiency ==========
def plot_language_first_guess(df):
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

    # Unstack so columns represent (firstGuess, type)
    pivot_table = pivot_table.unstack(level='type')

    # Plot
    ax = pivot_table.plot(kind='bar', figsize=(12, 6))

    # Format y-axis as percentage
    ax.yaxis.set_major_formatter(mticker.PercentFormatter())

    plt.title("Proportion of First Guess (True/False) by Language Proficiency and Type")
    plt.xlabel("Language Proficiency")
    plt.ylabel("Percentage of First Guess")
    plt.xticks(rotation=0)

    plt.legend(title="FirstGuess, Type", loc='upper left')

    plt.tight_layout()
    plt.savefig('language_by_first_guess.png', dpi=300)
    plt.show()


# Call each plot function
plot_experience_mean(df)
plot_first_true_guess(df)
plot_language_first_guess(df)
