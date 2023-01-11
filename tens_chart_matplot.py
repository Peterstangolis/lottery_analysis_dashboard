

def tens_charts(df):
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.dates import DateFormatter
    import matplotlib.ticker as ticker

    #pd.to_datetime(df.index, unit='s')

    ## Set Variables Options
    colors = ['#540E00', '#095436', '#02A161', '#5d5b5c',
              '#543C05', '#A17512', '#06136B', '#A11C02']
    titles = ['0-9', '10-19', '20-29', '30-39',
              '40-49', '50-59', '60-69', '70']
    cols = df.columns
    tick_spacing_x = 1
    tick_spacing_y = 2

    fig, axs = plt.subplots(4, 2, figsize=(11, 4.5),
                            constrained_layout=True,
                            sharex=True, sharey=False,
                            edgecolor='darkgreen',
                            linewidth=5,
                            facecolor='lightyellow')

    #fig.suptitle("TOTAL OCCURRENCES OF 10'S DIGITS")

    for n, p in enumerate(axs):

        ## COLUMN 1 CHART SETTINGS
        axs[n, 0].plot(df.index, df[str(n)], colors[n])
        axs[n, 0].set_title(titles[n], loc='left', y=.72, x=0.02,
                            fontsize='small',
                            weight='bold',
                            color=colors[n])

        axs[n, 0].set_ylim([0, 7])
        axs[n, 0].xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_x))
        axs[n, 0].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_y))
        axs[n, 0].tick_params(axis='y', colors=colors[n])
        top_side = axs[n, 0].spines['top']
        top_side.set_visible(False)
        right_side = axs[n, 0].spines['right']
        right_side.set_visible(False)
        axs[n, 0].set_facecolor("lightyellow")


        ## COLUMN 2 CHART SETTINGS
        axs[n, 1].plot(df.index, df[str(n + 4)], colors[n + 4])
        axs[n, 1].set_title(titles[n + 4], loc='left', y=.75, x=0.02,
                            fontsize='small',
                            weight='bold',
                            color=colors[n + 4])
        if n + 4 != 7:
            axs[n, 1].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_y))
        axs[n, 1].tick_params(axis='y', colors=colors[n + 4])
        top_side_2 = axs[n, 1].spines['top']
        top_side_2.set_visible(False)
        right_side_2 = axs[n, 1].spines['right']
        right_side_2.set_visible(False)
        axs[n, 1].set_facecolor("lightyellow")

        axs[3, 0].xaxis.set_major_formatter(mdates.DateFormatter('%y-%b-%d'))

        axs[3, 1].xaxis.set_major_formatter(
            mdates.ConciseDateFormatter(axs[3, 1].xaxis.get_major_locator()))

        for label in axs[3, 0].get_xticklabels(which='major'):
            label.set(rotation=30, horizontalalignment='right')

        for label in axs[3, 1].get_xticklabels(which='major'):
            label.set(rotation=30, horizontalalignment='right')


    return fig