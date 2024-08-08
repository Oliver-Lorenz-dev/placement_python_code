import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read in the monocle metadata using the pandas library
df = pd.read_csv("monocle-metadata.csv")

# set the plotting library (seaborn) to have a larger font scale
sns.set(font_scale=0.75)


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


def plot_continent_counts(df: pd.DataFrame):
    # function to plot the percentage Continent distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique Continents
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["Continent"])))

    # create the plot
    sns.countplot(
        data=df,
        x="Continent",
        order=df["Continent"].value_counts().index,
        palette=colours,
        stat="percent",
        hue="Continent",
    )

    # add the x and y axis labels
    plt.xlabel("Continent")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of Continents across 11F_like samples in GPS")

    # show the plot
    plt.savefig("Continents_plot.png", bbox_inches = 'tight')



def plot_country_counts(df: pd.DataFrame):
    # function to plot the percentage GPSC distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique Countries
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["Country"])))

    # create the plot
    sns.countplot(
        data=df,
        x="Country",
        order=df["Country"].value_counts().index,
        palette=colours,
        stat="percent",
        hue="Country",
    )

    # add the x and y axis labels
    plt.xlabel("Country")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of Countries across 11F_like samples in GPS")

    # show the plot
    plt.savefig("Country_plot.png", bbox_inches = 'tight')
  


def plot_time_counts(df: pd.DataFrame):
    # function to plot the percentage time distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique Years
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["Year"])))

    # create the plot
    sns.countplot(
        data=df,
        x="Year",
        palette=colours,
        stat="percent",
        hue="Year",
    )

    # add the x and y axis labels
    plt.xlabel("Year")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of time across 11F_like samples in GPS")

    # show the plot
    plt.savefig("Time_plot.png", bbox_inches = 'tight')


def plot_st_counts(df: pd.DataFrame):
    # function to plot the percentage GPSC distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique STs
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["In_silico_ST"])))

    # create the plot
    sns.countplot(
        data=df,
        x="In_silico_ST",
        order=df["In_silico_ST"].value_counts().index,
        palette=colours,
        stat="percent",
        hue="In_silico_ST",
    )

    # add the x and y axis labels
    plt.xlabel("In_silico_ST")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of STs across 11F_like samples in GPS")

    # show the plot
    plt.savefig("ST_plot.png", bbox_inches = 'tight')


def plot_PCV_type_counts(df: pd.DataFrame):
    # function to plot the percentage PCV type distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique PCVs
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["PCV_type"])))

    # create the plot
    sns.countplot(
        data=df,
        x="PCV_type",
        order=df["PCV_type"].value_counts().index,
        palette=colours,
        stat="percent",
        hue="PCV_type",
    )

    # add the x and y axis labels
    plt.xlabel("PCV_type")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of PCV_type across 11F_like samples in GPS")

    # show the plot
    plt.savefig("PCV_type_plot.png", bbox_inches = 'tight')


def plot_Phenotypic_serotype_counts(df: pd.DataFrame):
    # function to plot the percentage Phenotypic serotype distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique Phenotypic serotypes
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["Phenotypic_serotype"])))

    # create the plot
    sns.countplot(
        data=df,
        x="Phenotypic_serotype",
        palette=colours,
        stat="percent",
        hue="Phenotypic_serotype",
    )

    # add the x and y axis labels
    plt.xlabel("Phenotypic_serotype")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of Phenotypic serotypes across 11F_like samples in GPS")

    # show the plot
    plt.savefig("Phenotypic_serotype_plot.png", bbox_inches = 'tight')


def plot_Vaccine_period_counts(df: pd.DataFrame):
    # function to plot the percentage Vaccine period distribution across the dataset

    # set the colour palette up with the number of colours equal to the number of unique Vaccine periods
    colours = sns.color_palette("bright", n_colors=len(pd.unique(df["Vaccine_period"])))

    # create the plot
    sns.countplot(
        data=df,
        x="Vaccine_period",
        order=df["Vaccine_period"].value_counts().index,
        palette=colours,
        stat="percent",
        hue="Vaccine_period",
    )

    # add the x and y axis labels
    plt.xlabel("Vaccine_period")
    plt.ylabel("Percentage")

    # add the title
    plt.title("Proportion of Vaccine periods across 11F_like samples in GPS")

    # show the plot
    plt.savefig("Vaccine_period_plot.png", bbox_inches = 'tight')

# plot the GPSC counts
plot_gpsc_counts(df)

plt.clf()


# plot the Country counts
plot_country_counts(df)

#clears so they dont all run at once
plt.clf()

# plot the Continent counts
plot_continent_counts(df)

plt.clf()

# plot the time counts
plot_time_counts(df)    

plt.clf()

# plot the ST counts
plot_st_counts(df)

plt.clf()

# plot the PCV type counts
plot_PCV_type_counts(df)

plt.clf()

# plot the Phenotypic Serotype counts
plot_Phenotypic_serotype_counts (df)

plt.clf()

# plot the Vaccine period counts
plot_Vaccine_period_counts (df)
