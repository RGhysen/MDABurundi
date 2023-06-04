import plotly.graph_objects as go

def create_fig(df):
    fig = go.Figure()
    # Add density mapbox trace
    fig.add_trace(
        go.Densitymapbox(
            lat=[50.875809],
            lon=[4.700110],
            z = df[1].voi,
            radius=10
        )
    )
    # Add scattermapbox trace for individual markers
    fig.add_trace(
        go.Scattermapbox(
            lat=[50.875809],
            lon=[4.700110],
            mode='markers',
            marker=dict(
                size=5,
                color='red',
                opacity=0.7
            ),
            hovertemplate="Naamsestraat 62",
            showlegend = False
        )
    )

    # Add density mapbox trace
    fig.add_trace(
        go.Densitymapbox(
            lat=[50.8738250],
            lon=[4.7001178],
            z=df[2].voi,
            radius=10
        )
    )

    # Add scattermapbox trace for individual markers
    fig.add_trace(
        go.Scattermapbox(
            lat=[50.8738250],
            lon=[4.7001178],
            mode='markers',
            marker=dict(
                size=5,
                color='red',
                opacity=0.7
            ),
            hovertemplate="Naamsestraat 81",
            showlegend = False
        )
    )

    # Add density mapbox trace
    fig.add_trace(
        go.Densitymapbox(
            lat=[50.8745267],
            lon=[4.6999168],
            z=df[3].voi,
            radius=10
        )
    )

    # Add scattermapbox trace for individual markers
    fig.add_trace(
        go.Scattermapbox(
            lat=[50.8745267],
            lon=[4.6999168],
            mode='markers',
            marker=dict(
                size=5,
                color='red',
                opacity=0.7
            ),
            hovertemplate="Calveriekapel",
            showlegend = False
        )
    )

    # Add density mapbox trace
    fig.add_trace(
        go.Densitymapbox(
            lat=[50.8741177],
            lon=[4.7000138],
            z=df[4].voi,
            radius=10
        )
    )

    # Add scattermapbox trace for individual markers
    fig.add_trace(
        go.Scattermapbox(
            lat=[50.8741177],
            lon=[4.7000138],
            mode='markers',
            marker=dict(
                size=5,
                color='red',
                opacity=0.7
            ),
            hovertemplate="Parkstraat 2",
            showlegend = False
        )
    )

    fig.update_layout(
        mapbox_style="stamen-terrain",
        mapbox_center={"lon": 180},
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox={
            'zoom': 15,
            'center': {'lon': df[0].long.mean(), 'lat': df[0].lat.mean()}
        }
    )

    return fig


