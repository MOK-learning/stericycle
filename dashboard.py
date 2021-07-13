#!/usr/bin/env python3

import os
import pandas as pd
import numpy as np

import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# external CSS stylesheets
external_stylesheets = [dbc.themes.SUPERHERO]

# Initialise the server
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)
application = app.server

# Open the csv and get list of runs


# Define the layout of our dashboard
app.layout = html.Div([

    dcc.Markdown('''
    # Title
    I am testing some text.
    ''', style={'text-align': 'center'}),

    # Dropdown menu definitions
    html.Div([
        dcc.Dropdown(id='year-select', 
                     options=[{'label': i, 'value': i} for i in ['2015','2016','2017','2018']], 
                     value='TOR', 
                     placeholder='Select a year', 
                     style=dict(width='100%', verticalAlign="middle", color='black')),
        dcc.Dropdown(id='some-select', 
                     options=[{'label': i, 'value': i} for i in ['2015','2016','2017','2018']], 
                     value='TOR', 
                     placeholder='Select something', 
                     style=dict(width='100%', verticalAlign="middle", color='black')),
    ], style=dict(display='flex')),
    

    # Define our graphs
    html.Div(children=[
        dcc.Graph(id='zee-lumi', style={'display': 'inline-block', 'width': '50%'}), 
        dcc.Graph(id='zmm-lumi', style={'display': 'inline-block', 'width': '50%'}), 
    ], style={'text-align': 'center'})

    ], style={'margin-left': '200px', 'margin-right': '200px'})


@app.callback(
    Output('zee-lumi', 'figure'),
    [Input('year-select', 'value')]
)
def update_zee(grpname):
    fig = make_subplots(rows=1, cols=1)
    fig1 = go.Scatter(mode='markers', x=np.linspace(1, int(grpname), 10), y=np.linspace(1, int(grpname), 10))
    fig.add_trace(fig1, row=1,col=1)
    return fig


if __name__ == "__main__": 
    app.run_server(debug=True)
