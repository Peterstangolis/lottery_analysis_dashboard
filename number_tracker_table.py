

def number_track_table(df):

    import plotly.graph_objects as go
    from plotly.colors import n_colors
    import numpy as np
    import pandas as pd

    df_track = pd.read_csv(df,
                           index_col=0,
                           skiprows=0,
                           )


    cols_full = df_track.columns

    col_types = dict()
    for col in cols_full:
        col_types[col] = 'Int64'

    df_track = pd.read_csv(df,
                           index_col=0,
                           skiprows=0,
                           dtype=col_types)

    df_track = df_track.iloc[1:]
    df_track_10 = df_track.iloc[0:, -20:]

    cols = df_track_10.columns
    cols_2 = []
    for col in cols:
        col = '<b>' + col + '</b>'
        cols_2.append(col)

    colors = ['#EBC410', '#6A8E02']

    header_color = '#F0E29F'

    color_fill = []
    col_values = []

    for n, c in enumerate(cols):
        l = np.array(colors)[list(df_track_10[c].values)]
        v = df_track_10[c].values
        col_values.append(v)
        color_fill.append(l)

    fig = go.Figure(data=[go.Table(
        columnwidth=[1 * len(cols_2)],
        header=dict(
            values=[cols_2[0], cols_2[1], cols_2[2], cols_2[3], cols_2[4], cols_2[5],
                    cols_2[6], cols_2[7], cols_2[8], cols_2[9], cols_2[10], cols_2[11],
                    cols_2[12], cols_2[13], cols_2[14], cols_2[15], cols_2[16], cols_2[17],
                    cols_2[18], cols_2[19]],
            line_color='white', fill_color='royalblue',
            align='center',
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[col_values[0], col_values[1], col_values[2], col_values[3], col_values[4], col_values[5],
                    col_values[6], col_values[7], col_values[8], col_values[9], col_values[10], col_values[11],
                    col_values[12], col_values[13], col_values[14], col_values[15], col_values[16], col_values[17],
                    col_values[18], col_values[19]],
            line_color=['white'],
            fill_color=[color_fill[0], color_fill[1], color_fill[2], color_fill[3], color_fill[4], color_fill[5],
                        color_fill[6], color_fill[7], color_fill[8], color_fill[9], color_fill[10], color_fill[11],
                        color_fill[12], color_fill[13], color_fill[14], color_fill[15], color_fill[16], color_fill[17],
                        color_fill[18], color_fill[19]],
            align='center',
            font=dict(color='white', size=13),
            height=30
        ))
    ])

    fig.update_layout(
        autosize=True,
        width=1900,
        height=1700)

    return fig