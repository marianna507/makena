# Read in the CSV file
#data = pd.read_csv("/home/lornam/Downloads/demo-uber-nyc-pickups-main/pages/LORNA/Victimization.csv")


import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/marianna507/marianna50/main/LORNA/Victimization.csv?token=GHSAT0AAAAAAB4JVG6KIKR2EGV7CXKGGG3AY4YZYIA')

fig = go.Figure(data=go.Scattergeo(
    lat = df['latitude'],
    lon = df['longitude'],
   
        )
    )

fig.update_layout(
    geo = dict(
        scope = 'africa',
        showland = True,
        landcolor = "rgb(212, 212, 212)",
        subunitcolor = "rgb(255, 255, 255)",
        countrycolor = "rgb(255, 255, 255)",
        showlakes = True,
        lakecolor = "rgb(255, 255, 255)",
        showsubunits = True,
        showcountries = True,
        resolution = 50,
        projection = dict(
            type = 'conic conformal',
            rotation_lon = -100
        ),
        lonaxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range= [ -140.0, -55.0 ],
            dtick = 5
        ),
        lataxis = dict (
            showgrid = True,
            gridwidth = 0.5,
            range= [ 20.0, 60.0 ],
            dtick = 5
        )
    ),
    title='US Precipitation 06-30-2015<br>Source',
)
fig.show()
