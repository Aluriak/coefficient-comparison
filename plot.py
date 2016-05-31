"""Plotting wrapping"""

from matplotlib import rc
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import savefig


# Data for plotting
TITLE = 'Coefficients scores'
XLABEL = 'Ratio of included element'
YLABEL='Similarity score'


def plot(measures:dict, title:str=TITLE, *, xlabel:str=XLABEL,
         ylabel:str=YLABEL, colors=None, savefile=None,
         dpi=400, show=None):
    """Generate the plot that show all the given data, formated as dict:

        {curve name: {x: y}}

    if savefile is not None and is a filename, the figure will be saved
    in png in given file, with given dpi.

    """
    # convert in pandas data frame for allow plotting
    gx = pd.DataFrame.from_dict(measures)
    # {black dotted,red,yellow,blue} line with marker o
    styles = ['ko-', 'ro-', 'yo-', 'bo-']

    # get plot, and sets the labels for the axis and the right axis (time)
    plot = gx.plot(style=styles)
    lines, labels = plot.get_legend_handles_labels()

    plot.legend(lines, labels, loc='upper left')
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)

    # axis limits : show the 0
    plot.set_ylim(0, 1.)

    # print or save
    if savefile:
        plt.savefig(savefile, dpi=dpi)
    if show or (not show and not savefile):
        plt.show()
