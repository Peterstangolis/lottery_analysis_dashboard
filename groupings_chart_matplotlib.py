
def groupings_chart(d_groups):
    import  matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import matplotlib.ticker as ticker
    from matplotlib.dates import DateFormatter
    from variables import numbers_breakdown


    colors = ['#540E00', '#095436', '#02A161', '#5d5b5c',
              '#543C05',  '#A17512', '#06136B', '#A11C02' ]

    d_groups = d_groups.tail(40)
    titles = list(numbers_breakdown.keys())
    cols = d_groups.columns
    tick_spacing_x = 1
    tick_spacing_y = 2

    fig, axs = plt.subplots(4 ,2, figsize=(11, 4.5),
                            constrained_layout=True,
                            sharex=True, sharey=False,
                            edgecolor='black',
                            linewidth=5,
                            facecolor='lightyellow')

    fig.suptitle("GROUPING NUMBERS DRAWN INTO LOW - MID - HIGH GROUPS")


    for n, p in enumerate(axs):

        axs[n,0].plot(d_groups.index, d_groups[str(n)], colors[n])
        axs[n,0].set_title(titles[n], loc='left', y=.82, x=0.02,
                            fontsize='medium',
                            weight='bold',
                            color=colors[n])
        # axs[n,0].grid(True)
        axs[n, 0].set_ylim([0, 7])
        axs[n, 0].xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_x))
        axs[n, 0].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_y))
        axs[n, 0].tick_params(axis='y', colors=colors[n])
        top_side = axs[n, 0].spines['top']
        top_side.set_visible(False)
        right_side = axs[n, 0].spines['right']
        right_side.set_visible(False)

        axs[n, 0].set_facecolor("lightyellow")

        ## Second Column of Plots Settings
        axs[n, 1].plot(d_groups.index, d_groups[str(n + 4)], colors[n + 4])
        axs[n, 1].set_title(titles[n + 4], loc='left', y=.85, x=0.02,
                            fontsize='medium',
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
        # axs[n,1].set_edgecolor("ghostwhite")

    axs[3, 0].xaxis.set_major_formatter(mdates.DateFormatter('%y-%b-%d'))
    axs[3, 1].xaxis.set_major_formatter(
        mdates.ConciseDateFormatter(axs[3, 1].xaxis.get_major_locator()))

    for label in axs[3, 0].get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')

    for label in axs[3, 1].get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')

    return fig