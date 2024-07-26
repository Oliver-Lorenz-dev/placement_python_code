# Placement python project
Mini python project involving plotting patterns seen in the 11F_like genetic variant samples from the GPS1 dataset

## Description
The `create_plots.py` script currently creates a plot showing the percentage distribution of GPSCs among the dataset. This plot is saved as `GPSC_plot.png`


## Setup
First, setup the repository:

Open Visual Studio Code and click on the "Clone Git Repository" button and provide the following URL: https://github.com/Oliver-Lorenz-dev/placement_python_code


Open a terminal using Visual Studio Code and run the following commands:

Create a python virtual environment to install the dependencies in:
```shell
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:
```shell
pip install -r requirements.txt
```

You can now run the `create_plots.py` script in visual studio or in the terminal by running `python create_plots.py`

Open the `GPSC_plot.png` file. Which is the most common GPSC?


### Task 1:
Create a plot showing the distribution of the 11F_like across the continents.

Edit the `create_plots.py` code by copying the `plot_gpsc_counts` function. You can rename it to `plot_continent_counts`.

You will need to edit x axis to plot `Continents` rather than `GPSCs`, the x axis label and the plot title.

### Task 2:
Create a plot showing the distribution of the 11F_like across the countries.

Edit the `create_plots.py` code by copying the `plot_gpsc_counts` function. You can rename it to `plot_country_counts`.

You will need to edit x axis to plot `Countries` rather than `GPSCs`, the x axis label and the plot title.

Save the plot to a file called `Country_plot.png`


### Task 3:
Create a plot showing the distribution of the 11F_like across time.

Edit the `create_plots.py` code by copying the `plot_gpsc_counts` function. You can rename it to `plot_time_counts`.

You will need to edit x axis to plot `Year` rather than `GPSCs`, the x axis label and the plot title.

Save the plot to a file called `Time_plot.png`

### Task 4:
Create a plot showing the ST distribution across the dataset.

Edit the `create_plots.py` code by copying the `plot_gpsc_counts` function. You can rename it to `plot_st_counts`.

You will need to edit x axis to plot `In_silico_ST` rather than `GPSCs`, the x axis label and the plot title.

Save the plot to a file called `ST_plot.png`


