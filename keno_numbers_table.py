

def keno_table():


    import plotly.graph_objects as go
    import pandas as pd

    KENO_NUMBERS = list(range(1, 71))
    df_keno = pd.DataFrame(KENO_NUMBERS,
                           columns=["KENO NUMBERS"])

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>KENO<br>NUMBERS</b>'],
            line_color='lightyellow', fill_color='darkgreen',
            align='center', font=dict(color='white', size=14),
            height=50
        ),
        cells=dict(
            values=[df_keno.values],
            line_color=['darkgreen'],
            fill_color=['lightyellow'],
            align='center',
            font=dict(color='darkgreen', size=13),
            height=30
        ))
    ])

    fig.update_layout(
        autosize=False,
        #paper_bgcolor="forestgreen",
        margin=dict(l=5, r=5, t=5, b=5),
        width=140,
        height=2200)

    # fig.write_image("keno_num_table.jpeg",
    #                 width=200,
    #                 height=2500,
    #                 scale=2
    #                 )

    return fig