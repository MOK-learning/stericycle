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

# Make sure Monthly and Total Charges are floating point
df.MonthlyCharges = pd.to_numeric(df.MonthlyCharges, errors='coerce')
df.TotalCharges   = pd.to_numeric(df.TotalCharges, errors='coerce')

# Replace NaN with median
df.tenure.fillna(df.tenure.median(), inplace=True)
df.MonthlyCharges.fillna(df.MonthlyCharges.median(), inplace=True)
df.TotalCharges.fillna(df.TotalCharges.median(), inplace=True)

# Rename SeniorCitizen 0/1 as No/Yes
df.SeniorCitizen = df.SeniorCitizen.map({0: 'No', 1: 'Yes'})

# Define Streaming (TV OR Movies) column
df['Streaming'] = 'No'

m1 = (df['StreamingTV'] == 'Yes')
m2 = (df['StreamingMovies'] == 'Yes')
df['Streaming'] = df['Streaming'].mask(m1 | m2, 'Yes')


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
                                title='How many customers churn?'
                                ),
                  style={'display': 'inline-block', 'width': '50%'}
                 ), 
        dcc.Graph(id='pie-gender', 
                  figure=px.pie(df.groupby('gender').count().reset_index(drop=False), 
                                values='customerID', 
                                names='gender', 
                                title='Gender breakdown of customers'
                                ),
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
                  figure=px.histogram(df, x='Churn', color='Partner', title='Partner churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='pie-churn-senior', 
                  figure=px.histogram(df, x='Churn', color='SeniorCitizen', title='Age churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='pie-churn-children', 
                  figure=px.histogram(df, x='Churn', color='Dependents', title='Children churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
    ], style={'text-align': 'center'}),
    

    dcc.Markdown('''
    Customers who do not have partners are about 13% more likely to churn;
    senior citizens are about 18% more likely to churn; 
    customers without dependents are 16% more likely to churn.
    
    Now that we have looked at demographic factors, 
    what about the products which the customers are using?
    Let's find out if this has any impact on the propensity of customers to churn.
    There are many products on offer, we will focus here on the main ones: 
    phone service, internet service and streaming (TV or Movies).
    ''', style={'text-align': 'center'}),

    
    # Product churn graphs
    html.Div(children=[
        dcc.Graph(id='pie-churn-phone', 
                  figure=px.histogram(df, x='Churn', color='PhoneService', title='Phone service churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='pie-churn-internet', 
                  figure=px.histogram(df, x='Churn', color='InternetService', title='Internet service churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='pie-churn-streaming', 
                  figure=px.histogram(df, x='Churn', color='Streaming', title='Streaming service churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
    ], style={'text-align': 'center'}),
    
    dcc.Markdown('''
    Whether or not a customer uses a phone service does not seem to effect
    whether or not they will churn. 
    Fibre optic internet users are most likely to churn out of internet service users,
    they are about 23% more likely to churn than DSL users and about 35% more likely to churn than customers without
    an internet service.
    Customers who use streaming services are roughly 8% more likely to churn than those that do not.

    Finally we will look at the financial aspect, based on a customers tenure, 
    monthly charges and total charges.
    We will also investigate their payment methods, i.e.
    what kind of contract they are on, their billing method and their payment method.
    ''', style={'text-align': 'center'}),
    

    # Financial churn graphs
    html.Div(children=[
        dcc.Graph(id='churn-tenure', 
                  figure=px.histogram(df, x='tenure', color='Churn', title='Customer tenure churn', nbins=10, histnorm='percent'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='churn-month', 
                  figure=px.histogram(df, x='MonthlyCharges', color='Churn', title='Monthly charges churn', nbins=10, histnorm='percent'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='churn-total', 
                  figure=px.histogram(df, x='TotalCharges', color='Churn', title='Total charges churn', nbins=10, histnorm='percent'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
    ], style={'text-align': 'center'}),
    html.Div(children=[
        dcc.Graph(id='churn-contract', 
                  figure=px.histogram(df, x='Churn', color='Contract', title='Contract type churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='churn-billing', 
                  figure=px.histogram(df, x='Churn', color='PaperlessBilling', title='Paperless billing churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
        dcc.Graph(id='churn-payment', 
                  figure=px.histogram(df, x='Churn', color='PaymentMethod', title='Payment method churn', histnorm='percent', barmode='group'),
                  style={'display': 'inline-block', 'width': '33%'}
                 ), 
    ], style={'text-align': 'center'}),
    
    dcc.Markdown('''
    As we can see, customers with low tenure and high 
    monthly charges are significantly more likely to churn than customers
    with lower monthly charges and higher tenure.

    Likewise, customers who have a month-to-month contract are most likely to churn, 
    as are customers who use paperless billing and pay using electronic cheques.
    ''', style={'text-align': 'center'}),


], style={'margin-left': '200px', 'margin-right': '200px'})



if __name__ == "__main__": 
    app.run_server(debug=True)
