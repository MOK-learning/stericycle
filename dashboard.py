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
df = pd.read_csv('data/CustomerChurn.csv')

# Rename SeniorCitizen 0/1 as No/Yes
df.SeniorCitizen = df.SeniorCitizen.map({0: 'No', 1: 'Yes'})


# Define the layout of our dashboard
app.layout = html.Div([

    dcc.Markdown('''
    # Customer churn 
    Here we will do some basic data visualisation of the customer churn data.
    ''', style={'text-align': 'center'}),
    
    # Basic churn and gender graphs
    html.Div(children=[
        dcc.Graph(id='pie-churn', 
                  figure=px.pie(df.groupby('Churn').count().reset_index(drop=False), 
                                values='customerID', 
                                names='Churn', 
                                title='How many customers churn?'),
                  style={'display': 'inline-block', 'width': '50%'}
                 ), 
        dcc.Graph(id='pie-gender', 
                  figure=px.pie(df.groupby('gender').count().reset_index(drop=False), 
                                values='customerID', 
                                names='gender', 
                                title='Gender breakdown of customers'),
                  style={'display': 'inline-block', 'width': '50%'}
                 ), 
    ], style={'text-align': 'center'}), 
    
    dcc.Markdown('''
    It looks like most (73.5%) of the customers are loyal, yay! 
    A small minority (26.5%) have churned, we need to figure out why.
    Our customer base is almost evenly split between males and females, 
    lets check if they are equally likely to churn?
    ''', style={'text-align': 'center'}),

    # Male/Female churn graphs
    html.Div(children=[
        dcc.Graph(id='pie-churn-male', 
                  figure=px.pie(df[df.gender == 'Male'].groupby('Churn').count().reset_index(drop=False), 
                                values='customerID', 
                                names='Churn', 
                                title='Percentage of males that churn'),
                  style={'display': 'inline-block', 'width': '50%'}
                 ), 
        dcc.Graph(id='pie-churn-female', 
                  figure=px.pie(df[df.gender == 'Female'].groupby('Churn').count().reset_index(drop=False), 
                                values='customerID', 
                                names='Churn', 
                                title='Percentage of females that churn'),
                  style={'display': 'inline-block', 'width': '50%'}
                 ), 
    ], style={'text-align': 'center'}), 
    
    dcc.Markdown('''
    There is a negligible difference between the sexes when it comes to 
    predicting churn.
    What about other demographic factors such as relationship status (Partner),
    age (SeniorCitizen) or having children (Dependents)?
    ''', style={'text-align': 'center'}),
    

    # Demographic churn graphs
    html.Div(children=[
        dcc.Graph(id='pie-churn-partner', 
                  figure=px.histogram(df, x='Churn', color='Partner', title='Partner churn', barnorm='percent'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='pie-churn-senior', 
                  figure=px.histogram(df, x='Churn', color='SeniorCitizen', title='Age churn', barnorm='percent'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='pie-churn-children', 
                  figure=px.histogram(df, x='Churn', color='Dependents', title='Children churn', barnorm='percent'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
    ], style={'text-align': 'center'}),
    

    dcc.Markdown('''
    Customers who do not have partners are about 30% more likely to churn;
    senior citizens are about 50% less likely to churn; 
    customers without dependents are 55% more likely to churn.
    Now that we have looked at demographic factors, 
    what about the products which the customers are using?
    Let's find out if this has any impact on the propensity of customers to churn.
    ''', style={'text-align': 'center'}),


], style={'margin-left': '200px', 'margin-right': '200px'})



if __name__ == "__main__": 
    app.run_server(debug=True)
