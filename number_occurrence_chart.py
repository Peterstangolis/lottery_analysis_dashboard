

def keno_number_count(df):
    import matplotlib.pyplot as plt

    df["start"] = 0
    df_sorted = df.sort_values(by='SELECTED TOTAL')

    my_range = range(1, len(df.index) + 1)

    fig, ax = plt.subplots(figsize=(4, 11),
                           facecolor='lightyellow',
                           linewidth = 5,
                           edgecolor='darkgreen',
                           constrained_layout=True
                           )
    fig.subplots_adjust(top=0.1,
                        bottom=0.1)

    #fig.suptitle("A Running Count Of How Often Each \nKeno # Has Been Picked")

    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off

    ax.hlines(y=my_range, xmin=df_sorted["start"], xmax=df_sorted["SELECTED TOTAL"],
              color='lightgreen', alpha=0.5)

    ax.scatter(df_sorted["SELECTED TOTAL"], my_range,
               # color='skyblue',
               c=df_sorted["SELECTED TOTAL"], cmap='summer_r',
               alpha=1, label='value1',
               s=100, edgecolor='k')

    for line in range(0, df_sorted.shape[0]):
        plt.text(df_sorted['SELECTED TOTAL'][line] + 0.6, my_range[(70 - line - 1)],
                 df_sorted["SELECTED TOTAL"][line],
                 horizontalalignment='left', size='medium', color='black', weight='semibold',
                 verticalalignment='center')

    ax.set_yticks(my_range, df_sorted["KENO NUMBERS"])

    ax.spines.right.set_visible(False)
    ax.spines.bottom.set_visible(False)
    ax.spines.top.set_visible(False)

    ax.set_facecolor("lightyellow")


    return fig