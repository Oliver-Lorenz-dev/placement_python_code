import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the monocle metadata using the pandas library
df = pd.read_csv("monocle-metadata.csv")

# set the plotting library (seaborn) to have a larger font scale
sns.set(font_scale=2)


def plot_gpsc_counts(df: pd.DataFrame):
    # function to plot the percentage GPSC distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique GPSCs
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["GPSC"])))

    # create the plot
    sns.countplot(
        data=df,
        x="GPSC",
        order=df["GPSC"].value_counts().index,
        palette=colours,
        stat="percent",
        hue="GPSC",
    )

    # add the x and y axis labels
    plt.xlabel("GPSC")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of GPSCs across 11F_like samples in GPS")

    # show the plot
    plt.savefig("GPSC_plot.png", bbox_inches = 'tight')


# plot the GPSC counts
plot_gpsc_counts(df)
